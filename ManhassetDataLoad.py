#This file will load an excel file containing historical store data into the RETAIL_MART_MERGE.RETAIL_SALES_HISTORY_CUSTOM.
#This will allow the data to show up in the Daily Flash
#ARay 5-18-16

import cx_Oracle
import os
from datetime import timedelta, date
import pandas as pd

os.environ['ORACLE_HOME'] = '/oracle_64/orahome11g/'
os.environ['LD_LIBRARY_PATH'] = '/oracle_64/orahome11g/lib'
#construct = 'qad/mfg@ny-oracle-ts-01.Yurman.com:1521/dwtest01'  #TEST
construct = 'qad/mfg@ny-oracle-pr-02.Yurman.com:1521/dwprod01' #PRODUCTION


conn = cx_Oracle.connect(construct)
cursorOracle = conn.cursor()

#Load Excel file
excelData = pd.ExcelFile('trans-1586.xls')

#Place data into Data Frame
df = excelData.parse(excelData.sheet_names[0])

#Get the highest ticket number from table - will be something like "H74961". Cut off H.
selectStatement = ("select  from RETAIL_MART_MERGE.RETAIL_SALES_HISTORY_CUSTOM_bk ")
selectResults = cursorOracle.execute(selectStatement)
for maxTicketValue in selectResults:
    ticketNumber = str(maxTicketValue[0])
ticketNumber = ticketNumber[1:]
ticketNumber = int(ticketNumber) + 1 

#Iterate through all rows in Data Frame
#for row in df.iterrows():
for row_index, row in df.iterrows():
    #Set up ticketNumber with "H" preappended
    fullTicketNumber = 'H'+str(ticketNumber)
    ticketNumber += 1 
    vDtTransDate = row['DtTransDate']
    vDtTransDate = str(vDtTransDate).split()
    #Transform into correct format
    vDtTransDate= "to_char(to_date('"+vDtTransDate[0]+"','YYYY-MM-DD'),'DD-MON-YYYY')"
     
    #Logic for DOCUMENT_TYPE
    if (row['Type'] == 'S'):
       DOCUMENT_TYPE = 'SLC'
    elif (row['Type'] == 'R'):
       DOCUMENT_TYPE = 'CRD'
    else:
       DOCUMENT_TYPE = 'XXX'
    
    #Set Price and Quantity
    price = row['Price']
    quantity = row['Qty']

    #Set up UPC CODE
    upcCode = row['UPC']
    #Fix bad UPC CODES
    if (len(str(upcCode)) < 12 or (str(upcCode).isdigit()  == False)): 
        upcCode = '883932627398'
    
    #Set up KWI UPC Code- cut off end and beginning
    kwiUpcCode = str(upcCode)
    kwiUpcCode = kwiUpcCode[:-1]
    kwiUpcCode = kwiUpcCode[1:]
    
    #Insert Statement
    insertStatement = ("insert into RETAIL_MART_MERGE.RETAIL_SALES_HISTORY_CUSTOM "+
                       "(BATCH_NUMBER, TICKET_NUMBER, LINE_NUMBER, SALESPERSON, STORE_LOCATION, TRANSACTION_DATE, SYSTEM_DATE, DOCUMENT_TYPE, " +
                       "SPLIT_SALE, CUSTOMER_NUMBER, UNIT_PRICE, QUANTITY_SOLD, EXT_VALUE_SOLD_USD, EXT_COST_SOLD, TAXABLE_FLAG, TAX_VALUE, STATION_NUMBER, OWNERSHIP, LOAD_DATE, CURRENT_UNIT_RETAIL_PRICE, "+
                       "DISCOUNT_CODE, SALE_COUNT, TICKET_REFERENCE, RETAIL_UNIT_PRICE, UPC_CODE, EXT_STD_COST_SOLD, KWI_UPC_CODE, KWI_EMPLOYEE_NBR, COMPANY, LOCAL_EXT_VALUE_SOLD) "+     
                       "values "+
                       "('KWI', "+                     #BATCH_NUMBER
                       "'"+ fullTicketNumber + "', " + #TICKET_NUMBER
                       "'1', "+                        #Line_number
                       "'300101', " +                  #SALESPERSON
                       "'269350', " +                  #STORE_LOCATION 
                       " " + vDtTransDate + ", " +     #TRANSACTION_DATE
                       " " + vDtTransDate + ", " +     #SYSTEM_DATE 
                       "'" + DOCUMENT_TYPE + "', " +   #DOCUMENT_TYPE
                       "'N','0', "+                    #SPLIT_SALE and CUSTOMER_NUMBER
                       "'" + str(price) +"', " +       #UNIT_PRICE
                       "'" + str(quantity)   +"'," +   #QUANTITY_SOLD 
                       "'" + str(price) +"'," +        #EXT_VALUE_SOLD_USD
                       "'" + str(price) +"'," +        #EXT_COST_SOLD
                       "'Y','" + str(price) +"', " +   #TAXABLE_FLAG and TAX_VALUE
                       "'1', 'PD', trunc(sysdate)," +  #STATION_NUMBER and OWNERSHIP and LOAD_DATE
                       "'" + str(price)+ "'," +        #CURRENT_UNIT_RETAIL_PRICE
                       "'0','0','0'," +                #DISCOUNT_CODE, SALE_COUNT, TICKET_REFERENCE 
                       "'" + str(price)+ "', " +       #RETAIL_UNIT_PRICE 
                       "'" + str(upcCode)+ "'," +      #UPC_CODE
                       "'" + str(price)+  "'," +       #EXT_STD_COST_SOLD
                       "'" + str(kwiUpcCode)+ "', "+   #KWI_UPC_CODE 
                       "'300101', '269', " +           #KWI_EMPLOYEE_NBR and COMPANY
                       "'" + str(price) + "')")        #LOCAL_EXT_VALUE_SOLD
 
    #Load Data
    productionValue = cursorOracle.execute(insertStatement)
    conn.commit()

#Clean up database connections
cursorOracle.close()
conn.close()
