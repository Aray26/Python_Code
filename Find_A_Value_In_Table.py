#find a column that has a value given a database and a table

import cx_Oracle
import os
import re
import sys

# raw_input('Which databaese do you ')

os.environ['ORACLE_HOME'] = '/oracle_64/orahome11g/'
os.environ['LD_LIBRARY_PATH'] = '/oracle_64/orahome11g/lib'
construct = 'qad/mfg@ny-oracle-ts-01.Yurman.com:1521/dwtest01'  #TEST
#construct = 'qad/mfg@ny-oracle-pr-02.Yurman.com:1521/dwprod01'  # PRODUCTION

conn = cx_Oracle.connect(construct)
cursorOracle = conn.cursor()
cursorOracle2 = conn.cursor()

print "Please enter a table name- like DW_COMMON.USER_DIMENSION"
#table_to_query = str(raw_input("Tell me your table: " )).upper()
table_to_query = "DW_COMMON.USER_DIMENSION"
print table_to_query
just_table_name = table_to_query.split('.')[1]

print "Please enter what you are looking for - everything is cast into a String including numbers like 3"
query_string = str(raw_input("Tell me your string: " )).upper()
print query_string

print "You  are looking for " + str(query_string).upper() + " in the table " + str(table_to_query).upper() + "."


try:
    select_statement = ("select * from " + str(table_to_query) )
    selectResults = cursorOracle.execute(select_statement)
except Exception:
   print "table not found"
   sys.exit()

try:
    column_select_query = ("select column_name from DBA_TAB_COLS  where table_name = \'" + str(just_table_name) ) + "\'"
    print column_select_query
    print "type of column query " + str(type(column_select_query))

    column_results = cursorOracle2.execute(column_select_query)

    print "type(column_results) " + str(type(column_results))

    print "column_results XXXX  " + str(column_results)
except Exception:
    print "XXXX Columns not found"
    sys.exit()

print "++++++++++++++++++++"
print column_results
print "///////////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"
clean_columns =[]
for i in column_results:
    print "Column name is " + str(i).strip(',').strip('(,)').replace("'", "")
    x = str(i).strip(',').strip('(,)').replace("'", "")
    clean_columns.append(x)

print "clean_columns " + str(clean_columns)


entire_row =[]
matches = []
combine_lists = []
final_results = {}



for entire_row in selectResults:
    #zip()   columns and the row_element
    #print "entire_row " + str(entire_row)
    #print "combined_list " + str(combine_lists)
    combine_lists = zip(clean_columns, entire_row )

    for row_element in combine_lists:
        #print "testing " + str(row_element).upper()
        #print type(row_element)

        if (re.search(str(query_string).upper(), str(row_element[1]).upper())):
            print "Found match!!! " + str(query_string).upper() + "  " + str(row_element[1]).upper()
            print "Found a match in table " + str(table_to_query) + " column " + str(row_element[0]).upper()
            final_results[str(table_to_query).upper()] =  str(row_element[0]).upper()

print "-----------JJJJJ--------------"
print final_results

'''
Columns do not match order also buggy code
'''







print "4444444444444444444444444"
#print column_select_query

print "555555555555555555555555555"
#print selectResults,  column_results



'''
# Iterate through all rows in Data Frame
# for row in df.iterrows():
for row_index, row in df.iterrows():
    # Set up ticketNumber with "H" preappended
    fullTicketNumber = 'H' + str(ticketNumber)
    ticketNumber += 1
    vDtTransDate = row['DtTransDate']
    vDtTransDate = str(vDtTransDate).split()
    # Transform into correct format
    vDtTransDate = "to_char(to_date('" + vDtTransDate[0] + "','YYYY-MM-DD'),'DD-MON-YYYY')"

    # Logic for DOCUMENT_TYPE
    if (row['Type'] == 'S'):
        DOCUMENT_TYPE = 'SLC'
    elif (row['Type'] == 'R'):
        DOCUMENT_TYPE = 'CRD'
    else:
        DOCUMENT_TYPE = 'XXX'

    # Set Price and Quantity
    price = row['Price']
    quantity = row['Qty']

    # Set up UPC CODE
    upcCode = row['UPC']
    # Fix bad UPC CODES
    if (len(str(upcCode)) < 12 or (str(upcCode).isdigit() == False)):
        upcCode = '883932627398'

    # Set up KWI UPC Code- cut off end and beginning
    kwiUpcCode = str(upcCode)
    kwiUpcCode = kwiUpcCode[:-1]
    kwiUpcCode = kwiUpcCode[1:]

    # Insert Statement
    insertStatement = ("insert into RETAIL_MART_MERGE.RETAIL_SALES_HISTORY_CUSTOM " +
                       "(BATCH_NUMBER, TICKET_NUMBER, LINE_NUMBER, SALESPERSON, STORE_LOCATION, TRANSACTION_DATE, SYSTEM_DATE, DOCUMENT_TYPE, " +
                       "SPLIT_SALE, CUSTOMER_NUMBER, UNIT_PRICE, QUANTITY_SOLD, EXT_VALUE_SOLD_USD, EXT_COST_SOLD, TAXABLE_FLAG, TAX_VALUE, STATION_NUMBER, OWNERSHIP, LOAD_DATE, CURRENT_UNIT_RETAIL_PRICE, " +
                       "DISCOUNT_CODE, SALE_COUNT, TICKET_REFERENCE, RETAIL_UNIT_PRICE, UPC_CODE, EXT_STD_COST_SOLD, KWI_UPC_CODE, KWI_EMPLOYEE_NBR, COMPANY, LOCAL_EXT_VALUE_SOLD) " +
                       "values " +
                       "('KWI', " +  # BATCH_NUMBER
                       "'" + fullTicketNumber + "', " +  # TICKET_NUMBER
                       "'1', " +  # Line_number
                       "'300101', " +  # SALESPERSON
                       "'269350', " +  # STORE_LOCATION
                       " " + vDtTransDate + ", " +  # TRANSACTION_DATE
                       " " + vDtTransDate + ", " +  # SYSTEM_DATE
                       "'" + DOCUMENT_TYPE + "', " +  # DOCUMENT_TYPE
                       "'N','0', " +  # SPLIT_SALE and CUSTOMER_NUMBER
                       "'" + str(price) + "', " +  # UNIT_PRICE
                       "'" + str(quantity) + "'," +  # QUANTITY_SOLD
                       "'" + str(price) + "'," +  # EXT_VALUE_SOLD_USD
                       "'" + str(price) + "'," +  # EXT_COST_SOLD
                       "'Y','" + str(price) + "', " +  # TAXABLE_FLAG and TAX_VALUE
                       "'1', 'PD', trunc(sysdate)," +  # STATION_NUMBER and OWNERSHIP and LOAD_DATE
                       "'" + str(price) + "'," +  # CURRENT_UNIT_RETAIL_PRICE
                       "'0','0','0'," +  # DISCOUNT_CODE, SALE_COUNT, TICKET_REFERENCE
                       "'" + str(price) + "', " +  # RETAIL_UNIT_PRICE
                       "'" + str(upcCode) + "'," +  # UPC_CODE
                       "'" + str(price) + "'," +  # EXT_STD_COST_SOLD
                       "'" + str(kwiUpcCode) + "', " +  # KWI_UPC_CODE
                       "'300101', '269', " +  # KWI_EMPLOYEE_NBR and COMPANY
                       "'" + str(price) + "')")  # LOCAL_EXT_VALUE_SOLD

    # Load Data
    productionValue = cursorOracle.execute(insertStatement)
    conn.commit()
'''
# Clean up database connections
cursorOracle.close()
cursorOracle2.close()
conn.close()