import datetime
import calendar
import cx_Oracle
import sys
import os
from datetime import timedelta, date, time
import csv
import pandas as pd
from pandas import DataFrame
import numpy as np
from matplotlib import style
import xlrd
print str(xlrd.__VERSION__)

'''
1. get Oracle connection 
2. open excel file 
3. loop through file
4. update select * from DW_USERS.USER_MENS_WEDDING_XREF
'''

os.environ['ORACLE_HOME'] = '/oracle_64/orahome11g/'
os.environ['LD_LIBRARY_PATH'] = '/oracle_64/orahome11g/lib'
construct = 'qad/mfg@ny-oracle-pr-02.Yurman.com:1521/dwprod01'
#construct = 'qad/mfg@ny-oracle-ts-01.Yurman.com:1521/dwtest01'
print ("The construct is...  " + construct)
conn = cx_Oracle.connect(construct)
cursorOracle = conn.cursor()



excel_df = pd.read_excel('fix_wedding_items.xlsx')
index_of_columns = excel_df.columns
list = len(excel_df.columns.tolist())
length_of_columns = len(index_of_columns)
#print "length_of_columns is " + str(length_of_columns)
index_of_rows = excel_df.index
length_of_rows =(len(index_of_rows))


for i in range(0, length_of_rows):
      row_value = excel_df.at[index_of_rows[i], index_of_columns[4]] # item number
      print "row_value is " + str(row_value)
      print "CCCCCCCCCCCCCCCCCCCCCCCC"
      row_value = "'"+str(row_value)+"'"
      print "row_value is now " + str(row_value)
      insert_statement = "insert into DW_USERS.USER_MENS_WEDDING_XREF (ITEM_CODE, PREV_PROD_LINE, CURR_PROD_LINE, LOAD_DATE, GENDER_DESC) " + \
                         "values ("+row_value+", '3500','4000',trunc(sysdate),'MALE')"
                          
      print insert_statement
      distinctMenuItems = cursorOracle.execute(insert_statement)  
      conn.commit()      

cursorOracle.close()
conn.close()

               
'''

              #row_value2 = df2.at[index_of_rows[0], index_of_columns[0]]
      #print str(row_value2)
          
              
              
      #df = pd.read_excel('Uncased Items.xlsx', sheet_name='Case')


#>>> os.chdir(r'/home/username/Downloads')

#            date_value = index_of_columns[x].strftime("%d-%b-%Y").upper().split(' ')[0]
#            #date_value = date_value.strftime("%d-%b-%Y").upper()
#            #date_value2 = str(date_value).split(' ')[0].upper()
#            data_value = df.at[index_of_rows[i], index_of_columns[x]]
#            target.write("D,COREFCST,COREFCST_DESC,,"+str(row_value)+","+ str(date_value).upper()+","+ str(date_value).upper()+","+ str(data_value)+",N\n")


#date_value = date_value.split(' ')[0]




print "B" * 36
print "index_of_rows " + str(index_of_rows)
label = df.index[0]
print  label
lst = df.index.tolist()
print "lst  " + str(lst)
print lst[-1]
print "rows " + str(index_of_rows)
print index_of_rows[0]
print index_of_rows[1]
print type(index_of_rows)
print type(index_of_rows[0])
print type(index_of_rows[1])

print "C" * 36
print "Let's access some cells"
#value = df.at['row','col']
#value2 = df.loc['row','col']

value = df.at[index_of_rows[0], index_of_columns[0]]
print "1 is " + str(value)

value2 = df.loc[index_of_rows[0], index_of_columns[2]]
print "2 is " + str(value2)

datey = index_of_columns[2]
value3 = df.loc[index_of_rows[0], datey]
print "3 is " + str(value3)




target.write("++++++++++++++++++++++++++++++++++++Begin Run+++++++++++++++++++++++++++++++++++++++\n")

target.write("\n")
target.write("\n")





value = df.at[index_of_rows[0], index_of_columns[0]]
print "1 is " + str(value)










allDates = list(df.columns[1:])

print "All Dates"
allDates = list(df.columns[1:])
#print allDates[0].now().date()#.format("%d.%b.%Y")

small = allDates[0].now().date()

#then = datetime.datetime.strptime(when, '%Y-%m-%d').date()
#adjusted = datetime.datetime.strptime(str(small), '%d-%b-%Y').date()

small = small.strftime("%d-%b-%Y").upper()
print "small = "  + str(small)




#datetime.datetime.now().date()

print "CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC"    
#value = df.at(0,12).values
#Item	04/04/16
#B03934 S4AAMM	7

print df.index

for index, row in df.iterrows():
    print('index: ', index)
    print "*********"
    print('row: ', row)
    print "---------"
    target.write(str(row[0]))

#allRows = pd.DataFrame(df.row)
#print allRows   
vv2 = df.iloc[1,1]
#vv2 = df.loc['2','04/04/16']

print "Vv2 = " + str(vv2)


print "ddddddddddddddddddddddddddddddddddddddddddddd"    

df2 = pd.DataFrame({0: [3]});df2
#pd.Timestamp('20140202')})

i = 0 
#date = time.strftime("%x")
#print df

d={}
d['CIM 2016'] = df

 

#print d

#print "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"

#print df.head(1)

#print "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"


df2.insert(0,"M","D")
df2.insert(1,"Forecast Name","COREFCST")
df2.insert(2,"Description","Current Forecast")
df2.insert(3,"Demand Class","")
#df["M"] ="D"
#df.head()

#print "mmsmdajondasjindasdnasdno  " + str(matrix) 

#for rowy in matrix:
#    print "rowy" + str(rowy) + "\n"
    
    
#print "/////////////////////////////////////////"    
#print "df.columns\n"    
#print df.columns[1:]
#print df.columns
 
allDates = list(df.columns[1:])
#print allDates

#print df.index[1]

#print "\n+++++++++++++++++++++++++++++++++++++++++++++++++++\n"

#print df.T

#print "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
 
#print "df.values\n"    
#print df.values

#print "df.index\n"    
#print df.index


df.to_excel('ForEBS.xlsx',sheet_name='Logility Results')



#print "000000000000000000000000000000000000000000000000000000000000000000"
#print df2
df2.to_excel('Final EBS.xlsx',sheet_name='Logility Results')

for row in df.iterrows():
    # iterate through all elements in the row
    if (i >= 3): 
       break
    #print "row" + str(row) + "\n"
    #print "CMCMCmcmcmcmcmcmcmcmcmc\n"
    #print "row" + str(row[1]) + "\n"
    
    #Divide up the columns

    vvDate = str(row[1]).split()
    #for cc in vvDate:
    #    print "CC" + str(vvDate)
#   print "row" + str(row) + "\n"
    
 #   print "CMCMC" + str(row[0])
  #  print "mmmm" +  str(row[1]) 
    #print str(row[2])
    
   # array = [str(row[1]).split(' ')]
    #print "ooooooooooooooooooooooooo\n"
    #print str(array[0]) 
    #print "\njjjjjjjjj\n"
    #print array[1] + "\n"
    #print array[2] + "\n"
    
#    i+=1

#target.write("\n")
#target.write("\n")

#print "And finally, we close it."
'''

'''
junk

#print str(os.getcwd())
      #open up file to find match in previously loaded
      #os.chdir('//ny-dfs-pr-03/etl-prod/Data Warehouse/KWI Refresh Data/CaseCode/loaded')
      #print str('AAAA')
      #print str(os.getcwd())
      #print str('BBBB')
      #for files in os.walk(os.getcwd()):
      #for files in os.listdir('\\networkshares\\folder1\\folder2\\folder3')
      #listy2 = os.listdir('//ny-dfs-pr-03/etl-prod/Data Warehouse/KWI Refresh Data/CaseCode/loaded')
      
'''