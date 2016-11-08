import datetime
import calendar
import cx_Oracle
import sys
import os
from datetime import timedelta, date, time
import csv
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('ggplot')


filename = 'output.txt'

target = open(filename, 'w')

#excelData = pd.ExcelFile('Lindsey Done With Adjustments Altered.xlsx')
df = pd.read_excel('Lindsey Done With Adjustments Altered.xlsx', sheet_name='CIM 2016')

print df
target.write(str(df))

value = df.loc['banana','Police']
print value

#x = str('04/04/16')
#value2 = df.loc['banana','X']
#print value2

label = df.index[1]
print label

column = df.columns[2]
print column

value = df.at['apple','Police']
print value

value2 = df.at['apple','2016/04/04 00:00:00']
print value2




target.close()