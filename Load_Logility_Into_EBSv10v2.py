import datetime
import calendar
import cx_Oracle
import sys
import os
from datetime import timedelta, date, time
import csv
import six
import pandas as pd
from pandas import DataFrame
import numpy as np
from matplotlib import style

output_filename = 'output.csv'


target = open(output_filename, 'wb')
#excelData = pd.ExcelFile('Lindsey Done With Adjustments Altered.xlsx')
#df = pd.read_excel('Lindsey Done With Adjustments Altered.xlsx', sheet_name='CIM 2016')
#df = pd.read_excel('CaseyG-CIM.xlsx', sheet_name='CIM 2016')
#df = pd.read_excel('Log_Out_8_17_Pt1.xlsx', sheet_name='Log_Out_8_17_Pt1')
#df = pd.read_excel('9_8_2016_data_request.xlsx', sheet_name='data')

#df = pd.read_excel('Timepieces91616.xlsx', sheet_name='CIM')
#df = pd.read_excel('Logility_load_ADDITIONS_9_16_2016v3_testing.xlsx', sheet_name='CIM')
#df = pd.read_excel('Review Template - Timepieces 9 16 16.xlsx', sheet_name='CIM')

#works 
#df = pd.read_excel('Logility1010.xlsx', sheet_name='CIM')


df = pd.read_excel('Logility2ndLoad9152016_COREv2.xlsx', sheet_name='CIM CORE')


#Logility_load_ADDITIONS_9_16_2016v3_testing

#df = pd.read_excel('CORE 9162016.xlsx', sheet_name='CIM')

#print df


index_of_columns = df.columns
list = len(df.columns.tolist())
length_of_columns = len(index_of_columns)
#print "*" * 36
#print "list " + str(list)

index_of_rows = df.index
#print "length of rows " + str(len(index_of_rows))
length_of_rows =(len(index_of_rows))

#target.write("M,CORE_FORECAST,CORE_FORECAST_DESC,WEEKS,,30,30,NJW,N\n") #original
#target.write("M,CORE_FC,CR_DESC,Days,21,14,NJW,N\r\n") #Extra space bug -
target.write("M,CORE_FC,CR_DESC,Days,15,10,NJW,N\r\n") #Extra space bug -
for x in range(1, length_of_columns):
      for i in range(0, length_of_rows):
            row_value = df.at[index_of_rows[i], index_of_columns[0]]
            print str(row_value) + "\n"
            #if row_value > 2:
            #    print "here"
            #    exit()
            if isinstance(index_of_columns[x], six.string_types):
                #pass  # It's a string !!
                print x
                print i
                row_value = df.at[index_of_rows[i], index_of_columns[x]]
                datetime.make_to_time = 0
                print (index_of_columns[x])
                print str(" ") + str(type(index_of_columns[x]))
                #make_to_time = datetime.datetime.strptime(index_of_columns[x],"%m/%d/%y ")
                #date_value =str(make_to_time).upper().split(' ')[0]
            #else:
                date_value = index_of_columns[x].strftime("%d-%b-%Y").upper().split(' ')[0]
                print date_value
            print str(index_of_columns[x]) + " " + str(type(index_of_columns[x]))
            #cast_to_string
            data_value = df.at[index_of_rows[i], index_of_columns[x]]
            if data_value is not None: # or data_value == 0: # ar 91516 change
               #target.write("D,CORE,"+str(row_value)+","+ str(date_value).upper()+",,"+ str(data_value)+",N\r\n") #original
               target.write("D,CORE,Oct10,,"+str(row_value)+","+ str(date_value).upper()+",,"+ str(data_value)+",N\r\n")
               #target.write("D,CORE,Sept15,, "+str(row_value)+","+ str(date_value).upper()+",,"+ str(data_value)+",N\r\n")
               pass
#print "B" * 36
#print "index_of_rows " + str(index_of_rows)
label = df.index[0]
#print  label
lst = df.index.tolist()
#print "lst  " + str(lst)
#print lst[-1]
#print "rows " + str(index_of_rows)
#print index_of_rows[0]
#print index_of_rows[1]
#print type(index_of_rows)
#print type(index_of_rows[0])
#print type(index_of_rows[1])

#print "C" * 36
#print "Let's access some cells"
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