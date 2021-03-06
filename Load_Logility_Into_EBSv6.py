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

output_filename = 'output.csv'

#was w
target = open(output_filename, 'wb')

print "What is the name of the incoming file? "
print "Just hit enter to use the default file name \"Incoming Forecast.xlsx\" "
incoming_filename =raw_input()
if (incoming_filename == ''):
    print "Using default filename - \"Incoming Forecast.xlsx\" "
else:
    print "Filename is " + str(incoming_filename)
    
print "What is the name of the Forecast - i.e. 'CORE_FC' or 'NON_COREFC' ?"
print "Name of the Forecast needs to be less than 8 characters"
forecast =raw_input()
print "Forecast us " + str(forecast)
print "\n"

print "what is the name of the Forecast Description ?"
print "the current Forecast Description is " + str(str(incoming_filename).split('.'))
print "Just hit enter to use the default file name \"Incoming Forecast.xlsx\" "
forecast_description =raw_input()
if (forecast_description == ''):
    forecast_description = str(incoming_filename.split('.'))
else:
    print "forecast_description is " + str(forecast_description)
print "\n"

print "Let's sum up "
print "Incoming file name is " + str(incoming_filename)
print "Forecast name is " + str(forecast)
print "Forecast Description is " + str(forecast_description)
  


#excelData = pd.ExcelFile('Lindsey Done With Adjustments Altered.xlsx')
#df = pd.read_excel('Lindsey Done With Adjustments Altered.xlsx', sheet_name='CIM 2016')
#df = pd.read_excel('CaseyG-CIM.xlsx', sheet_name='CIM 2016')
df = pd.read_excel('new_logility_load2.xlsx', sheet_name='Report 2')

index_of_columns = df.columns
list = len(df.columns.tolist())
length_of_columns = len(index_of_columns)
print "*" * 36
print "list " + str(list)

index_of_rows = df.index
print "length of rows " + str(len(index_of_rows))
length_of_rows =(len(index_of_rows))

print "A" * 36
#index_of_columns = df.columns
print "index_of_columns "+ str(index_of_columns)
print "type index_of_columns "+str(type(index_of_columns))
print type(index_of_columns[0])
print type(index_of_columns[1])
print type(index_of_columns[2])
print (index_of_columns[0])
print (index_of_columns[1])
print (index_of_columns[2])
print (index_of_columns[-1])

#for i in range(0, )

#target.write("M,CORE_FORECAST,CORE_FORECAST_DESC,WEEKS,,30,30,NJW,N\n") #original   
target.write("M,CORE_FC,CORE_FC_DESC,Weeks,30,30,NJW,N\r\n") #Extra space bug - 
for x in range(1, length_of_columns):
      for i in range(0, length_of_rows):
            row_value = df.at[index_of_rows[i], index_of_columns[0]]
            date_value = index_of_columns[x].strftime("%d-%b-%Y").upper().split(' ')[0]
            #date_value = date_value.strftime("%d-%b-%Y").upper()
            #date_value2 = str(date_value).split(' ')[0].upper()
            data_value = df.at[index_of_rows[i], index_of_columns[x]]
            target.write("D,COREFCST,COREFCST_DESC,,"+str(row_value)+","+ str(date_value).upper()+","+ str(date_value).upper()+","+ str(data_value)+",N\r\n")


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

target.close()