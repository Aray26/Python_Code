#This file will fix case codes
#ARay 5-18-16

import cx_Oracle
import os
from datetime import timedelta, date
import pandas as pd

#Database connection information
os.environ['ORACLE_HOME'] = '/oracle_64/orahome11g/'
os.environ['LD_LIBRARY_PATH'] = '/oracle_64/orahome11g/lib'
#construct = 'qad/mfg@ny-oracle-ts-01.Yurman.com:1521/dwtest01'  #TEST
construct = 'qad/mfg@ny-oracle-pr-02.Yurman.com:1521/dwprod01' #PRODUCTION

fo = open("foo.txt", "wb")

conn = cx_Oracle.connect(construct)
cursorOracle = conn.cursor()

#Load Excel file
excelData = pd.ExcelFile('KWI_CASECODE_REFRESH_TR2.xlsx')

#Place data into Data Frame
df = excelData.parse(excelData.sheet_names[0])


#Iterate through all rows in Data Frame
#for row in df.iterrows():
for row_index, row in df.iterrows():
    #print(row[0])
    try:
      article = int(row[0])
    except:
        print "article is " + str(row[0])
    print "jjjjjj " + str(article)
    #Select statement 
    selectStatement = ("select venitem2 from dw_temp.kwi_merge_articles_junk "+
                       "where company_code = \'273\' and venitem2 is not null and article = \'" + (str(article)) + "\'")        #LOCAL_EXT_VALUE_SOLD
    print str(selectStatement)
    
    #Load Data
    productionValue = cursorOracle.execute(selectStatement)
    #print (productionValue[0])
    
    for pv in productionValue:
        stringy = str(pv).replace(",","")
        stringy = str(stringy).replace("\)\'","")
        stringy = str(stringy).replace("\'\(",",")
        print str(stringy)
        fo.write(str(article)+","+ str(row[1])+","+ str(stringy)+"\n")
        #fo.write("sdsds\n")

#Clean up database connections
cursorOracle.close()
conn.close()
fo.close()
