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
from datetime import datetime
from dateutil.parser import parse
import logging

logging.basicConfig(filename='Logility_Run_Log.log', filemode='w', level=logging.DEBUG)

print str('What is the name of the Forecast Description ex. AUG172016 ?')
forecast_desc = raw_input('=>')
print str('Thank you. \"{0}\" is set as Forecast Description'.format(forecast_desc).strip())
output_filename = 'output.csv'
target = open(output_filename, 'wb')

logging.debug("This is a debug message")
logging.info("Informational message")
logging.error("An error has happened!")

try:
    raise RuntimeError
except Exception, err:
    log.exception("Error!")

"""
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
"""

# excelData = pd.ExcelFile('Lindsey Done With Adjustments Altered.xlsx')
# df = pd.read_excel('Lindsey Done With Adjustments Altered.xlsx', sheet_name='CIM 2016')
# df = pd.read_excel('CaseyG-CIM.xlsx', sheet_name='CIM 2016')
df = pd.read_excel('Log_Out_8_17_Pt1.xlsx', sheet_name='Log_Out_8_17_Pt1')
# df.fillna('X')

# df.fillna('missing')
# df.mean().fillna(0)
# print df

index_of_columns = df.columns
list = len(df.columns.tolist())
length_of_columns = len(index_of_columns)
# print "*" * 36
# print "list " + str(list)

index_of_rows = df.index
# print "length of rows " + str(len(index_of_rows))
length_of_rows = (len(index_of_rows))

# target.write("M,CORE_FORECAST,CORE_FORECAST_DESC,WEEKS,,30,30,NJW,N\n") #original
logging.info("Begin writting of header line")
target.write("M,CORE_FC,CR_DESC,Days,21,14,NJW,N\r\n")  # Extra space bug -
for x in range(1, length_of_columns):
    for i in range(0, length_of_rows):
        row_value = df.at[index_of_rows[i], index_of_columns[0]]
        # print str(row_value) + "\n"
        date_value = index_of_columns[x].strftime("%d-%b-%Y").upper().split(' ')[0]
        # date_value = date_value.strftime("%d-%b-%Y").upper()
        # date_value2 = str(date_value).split(' ')[0].upper()
        data_value = df.at[index_of_rows[i], index_of_columns[x]]
        # if not data_value or data_value == 0:
        # c=8#print "0 or null"
        # else:
        # target.write("D,CORE,"+str(row_value)+","+ str(date_value).upper()+",,"+ str(data_value)+",N\r\n")
        # print "date_value is " + str(date_value)
        # apple = datetime.datetime.strptime(date_value, '%d-%b-%Y').date()

        now = datetime.now().date()
        compare_date = datetime.now().date()
        todays_date = datetime.strptime(str(now), '%Y-%m-%d').strftime('%d-%b-%Y').upper()
        compare_date = datetime.strptime(str(date_value), '%d-%b-%Y').strftime('%d-%b-%Y').upper()

        print "compare_date is " + repr(type(compare_date))

        # compare_date = datetime.strptime(str(now), '%Y-%m-%d').strftime('%d-%b-%Y').date().upper()
        print "todays_date is " + str(todays_date)
        print 'compare_date is {0}'.format(str(compare_date))

        if todays_date >= compare_date:
            print "Date is already loaded."
        #if not data_value or data_value == 0:
        #    c=8#print "0 or null"
        else:
            logging.info("Begin writing of data rows")
            target.write(
                "D,CORE,"+str(forecast_desc)+",," + str(row_value) + "," + str(date_value).upper() + ",," + str(data_value) + ",N\r\n")

target.close()
