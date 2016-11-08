#draft version of codefromfrom __future__ import division
import datetime
import calendar
import cx_Oracle
import sys
import os
from datetime import timedelta, date
import csv
import pandas as pd
from pandas import DataFrame

os.environ['ORACLE_HOME'] = '/oracle_64/orahome11g/'
os.environ['LD_LIBRARY_PATH'] = '/oracle_64/orahome11g/lib'
#construct = 'aray/ar@ny-oracle-ts-01.Yurman.com:1521/dwtest01'
#construct = 'qad/mfg@ny-oracle-pr-02.Yurman.com:1521/dwprod01'
construct = 'qad/mfg@ny-oracle-ts-01.Yurman.com:1521/dwtest01'
print ("The construct is...  " + construct)
conn = cx_Oracle.connect(construct)
cursorOracle = conn.cursor()



#csvdata = pandas.read_csv('trans-1586.csv')
excelData = pd.ExcelFile('trans-1586.xls')

print excelData.sheet_names
print excelData.sheet_names[0]
#df = DataFrame(excelData)

df = excelData.parse(excelData.sheet_names[0])

print df
print "+++++++++++++++++++++"

i =0 
#ticketNumber = 74681

#Get the highest ticket number from table - will be something like "H74961". Cut off H.
#ticketNumber = 74681
selectStatement = ("select max(ticket_number) from RETAIL_MART_MERGE.RETAIL_SALES_HISTORY_CUSTOM_bk ")
selectResults = cursorOracle.execute(selectStatement)
for maxTicketValue in selectResults:
    ticketNumber = str(maxTicketValue[0])

ticketNumber = ticketNumber[1:]
print "testststs 1 " + str(ticketNumber)

ticketNumber = int(ticketNumber)+1 
#ticket now a number again
print "testststs 2 " + str(ticketNumber)

#ticketNumber += 1
ticketNumber = ticketNumber + 1
#ticketNumber = int(ticketNumber) +1 




for row_index, row in df.iterrows():
    # iterate through all elements in the row
    #if (i == 2): 
       #break
    
    print "ticketNumber "+ str(ticketNumber)+"\n"
    #set up ticketNumber 
    print 'H'+str(ticketNumber)
    fullTicketNumber = 'H'+str(ticketNumber)
    print "fullTicketNumber "+ fullTicketNumber+"\n"
    
    ticketNumber = ticketNumber +1 
    i= i +1 

    for colname in df.columns:
        row_element = row[colname]
        print colname + " "+ str(row_element)

    vDtTransDate = row['DtTransDate']
    vvDate =  pd.to_datetime(row['DtTransDate'])#, format='%d-%m-%Y')
    vvDate =  pd.to_datetime(vvDate, format='%d-%b-%Y')
              #vvDate = vvDate.split()
    #raw_data['Mycol'] =  pd.to_datetime(raw_data['Mycol'], format='%d%b%Y:%H:%M:%S.%f')
    print "vvDate " + str(vvDate)
    print "vvDate " + str(type(vvDate))
    vDtTransDate2 = str(vDtTransDate)
    vDtTransDate3= vDtTransDate2.split() 
    vDtTransDate4 = vDtTransDate3[0]
    print "pppppppppppppppppppppppppppp\n"
    print "vDtTransDate4 " + str(vDtTransDate4)
    vDtTransDate4= "to_char(to_date('"+vDtTransDate4+"','YYYY-MM-DD'),'DD-MON-YYYY')"
    print "rrrrrrrrrrrrrrrrrrrrrrrr\n"
    print "vDtTransDate4 " + str(vDtTransDate4)

#now = datetime.datetime.now()
#print (now.year)
#print (now.month)
#print (now.minute, now.second, now.microsecond)
    

    print "++++++++++++++" + vDtTransDate4
    if (row['Type'] == 'S'):
       DOCUMENT_TYPE = 'SLC'
    elif (row['Type'] == 'R'):
       DOCUMENT_TYPE = 'CRD'
    else:
       DOCUMENT_TYPE = 'XXX'
    price = row['Price']
    quantity = row['Qty']

    #Set up UPC CODE
    upcCode = row['UPC']
    if (len(str(upcCode)) < 12 or (str(upcCode).isdigit()  == False)): # and 
        upcCode = '883932627398'
    
    #Set up KWI UPC Code
    kwiUpcCode = str(upcCode)
    kwiUpcCode = kwiUpcCode[:-1]
    kwiUpcCode = kwiUpcCode[1:]
    #stry4= stry3[:-1]
    
    print "//////////////////////////"
    #print " ".join([x[1:] for x in upcCode.split(" ")]);
    print "kwiUpcCode  " + str(kwiUpcCode)
    print "[[[[[[[[[[[[[[[[[[[[[[[[[[["
    
#883932627398


    print "----------------------------"
    
    #Insert Statement
    insertStatement = ("insert into RETAIL_MART_MERGE.RETAIL_SALES_HISTORY_CUSTOM_bk "+
                       "(BATCH_NUMBER, TICKET_NUMBER, LINE_NUMBER, SALESPERSON, STORE_LOCATION, TRANSACTION_DATE, SYSTEM_DATE, DOCUMENT_TYPE, " +
                       "SPLIT_SALE, CUSTOMER_NUMBER, UNIT_PRICE, QUANTITY_SOLD, EXT_VALUE_SOLD_USD, EXT_COST_SOLD, TAXABLE_FLAG, TAX_VALUE, STATION_NUMBER, OWNERSHIP, LOAD_DATE, CURRENT_UNIT_RETAIL_PRICE, "+
                       "DISCOUNT_CODE, SALE_COUNT, TICKET_REFERENCE, RETAIL_UNIT_PRICE, UPC_CODE, EXT_STD_COST_SOLD, KWI_UPC_CODE, KWI_EMPLOYEE_NBR, COMPANY, LOCAL_EXT_VALUE_SOLD) "+     
                       "values "+
                       "('KWI', "+                     #BATCH_NUMBER
                       "'"+ fullTicketNumber + "', " + #TICKET_NUMBER
                       "'1', "+                        #Line_number
                       "'300101', " +                  #SALESPERSON
                       "'269350', " +                  #STORE_LOCATION 
                       " " + vDtTransDate4 + ", " +   #TRANSACTION_DATE
                       "trunc(sysdate), " +          #SYSTEM_DATE 
                       "'" + DOCUMENT_TYPE + "', " +   #DOCUMENT_TYPE
                       "'N','0', "+                    #SPLIT_SALE and CUSTOMER_NUMBER
                       "'" + str(price) +"', " +       #UNIT_PRICE
                       "'" + str(quantity)   +"'," +  #QUANTITY_SOLD 
                       "'" + str(price) +"'," +       #EXT_VALUE_SOLD_USD
                       "'" + str(price) +"'," +       #EXT_COST_SOLD
                       "'Y','" + str(price) +"', " +   #TAXABLE_FLAG and TAX_VALUE
                       "'1', 'PD', trunc(sysdate)," + #STATION_NUMBER and OWNERSHIP and LOAD_DATE
                       "'" + str(price)+ "'," +        #CURRENT_UNIT_RETAIL_PRICE
                       "'0','0','0'," +               #DISCOUNT_CODE, SALE_COUNT, TICKET_REFERENCE 
                       "'" + str(price)+ "', " +       #RETAIL_UNIT_PRICE 
                       "'" + str(upcCode)+ "'," +     #UPC_CODE
                       "'" + str(price)+  "'," +      #EXT_STD_COST_SOLD
                       "'" + str(kwiUpcCode)+ "', "+   #KWI_UPC_CODE 
                       "'300101', '269', " +           #KWI_EMPLOYEE_NBR and COMPANY
                       "'" + str(price) + "')" +        #LOCAL_EXT_VALUE_SOLD
                       "")
 
 
  

    print "insertStatement \n>>>>>>>>>>>>>>\n" + str(insertStatement) +  "\n>>>>>>>>>>>>>>" 
    productionValue = cursorOracle.execute(insertStatement)
    conn.commit()
    

cursorOracle.close()


conn.close()
