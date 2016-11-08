import datetime
import calendar
import cx_Oracle
import sys
import os
from datetime import timedelta, date, time
import csv
import re
import pandas as pd
from pandas import DataFrame
import numpy as np
from matplotlib import style
import xlrd
print str(xlrd.__VERSION__)

'''
1. get list of all files
2. open file
3. loop through file
4. Loop through master list per file
5. write outfile of matches
6. write records to xxdy.xxdy_logility_missing_hh_items
'''

os.environ['ORACLE_HOME'] = '/oracle_64/orahome11g/'
os.environ['LD_LIBRARY_PATH'] = '/oracle_64/orahome11g/lib'
#construct = 'qad/mfg@ny-oracle-ts-01.Yurman.com:1521/dwtest01'  #TEST
#construct = 'APPS_RO/APPS_RO@oraebsscdb2.nav.yurman.com:1562/DYEUAT1' #PRODUCTION
construct = 'APPS_RO/APPS_RO@oraebsaddb1-vip.nav.yurman.com:1522/DYEPRD1' #PRODUCTION
conn = cx_Oracle.connect(construct)
cursorOracle = conn.cursor()

#set up output file
output_file_hh = 'Records_found_hh.csv'
output_file_aa = 'Records_found_aa.csv'
output_file_missing = 'Records_missing.csv'
target_hh = open(output_file_hh, 'wb')
target_aa = open(output_file_aa, 'wb')
target_missing = open(output_file_missing, 'wb')
list_hh_records = []
#list_aa_records = []
list_aa_records = set()
unpaired_hh_items =[]

hh_df = pd.read_csv('H:\Data Warehouse\Logility\extracts\lom_hhlv1_sell_thru.txt', header=None)
aa_df = pd.read_csv('H:\Data Warehouse\Logility\extracts\lom_aalv1.txt',error_bad_lines=False, header=None)

#print hh_df
#print aa_df

print "The number_of_rows HH is " + str(len(hh_df.index))
print "The number_of_rows AA is " + str(len(aa_df.index))

for (index, row) in hh_df.iterrows():
    #print "Index is " + str(index) + "  row " + str(row)
    result_of_split = re.split('HH', str(row))
    # lstrip().rstrip() strip does not get rid of middle spaces
    result_hh_raw = result_of_split[0][1:].strip()
    result_hh = result_hh_raw[1:]
    target_hh.write(str(result_hh) + "\n")
    list_hh_records.append(result_hh)
    print "have parsed HH"

for (index, row) in aa_df.iterrows():
    #print "Index is " + str(index) + "  row " + str(row)
    result_of_split = re.split('AA', str(row))
    # lstrip().rstrip() strip does not get rid of middle spaces
    result_aa_raw = result_of_split[0][1:].strip()
    result_aa = result_aa_raw[1:]
    target_aa.write(str(result_aa) + "\n")
    list_aa_records.add(result_aa)
    print str(index) + " " +str(result_aa) + " have parsed AA"

print "list_hh_records " + str(list_hh_records)
print "len list_hh_records " + str(len(list_hh_records))
print "The number_of_rows HH is " + str(len(hh_df.index))

print "list_aa_records " + str(list_aa_records)
print "len list_aa_records " + str(len(list_aa_records))
print "The number_of_rows AA is " + str(len(aa_df.index))

#unpaired_hh_items = set(list_hh_records) - set(list_aa_records)

if 'T9001QMSTBKCF2M' in list_hh_records:
    print "FOUNDD in hh records"
else:
    print "Not in HH"

if 'T9001QMSTBKCF2M' in list_aa_records:
    print "FOUNDD in aa records"
else:
    print "Not in AA"


for element in list_hh_records:
    print "Looking At: " + str(element)

    if  element not in list_aa_records:
        print str(element) +  "fkdfksdfds;fksd;f;ks"
        target_missing.write(str(element) + "\n")
        unpaired_hh_items.append(element)

print "Here are the items in the 2nd HH file not in the original AA file " + str(unpaired_hh_items)
print "Here is the number of unpaired items in HH file " + str(len(unpaired_hh_items))

count = 0

for element in unpaired_hh_items:
    print str(element)
    insertStatement = ("insert into xxdy.xxdy_logility_missing_hh_items " +
                                         "(ITEM_NAME) " +
                                         "values " +
                                         "( '" + str(element).strip() + "')" )

    print "insertStatement " + str(insertStatement)
    # Load Data
    count += 1
    productionValue = cursorOracle.execute(insertStatement)
    #cursorOracle.execute(insertStatement)
    conn.commit()

target_hh.close()
target_aa.close()
target_missing.close()
print "total inserted is " + str(count)

print str("++++++++++++++++++++++")
#Clean up database connections
cursorOracle.close()
conn.close()
