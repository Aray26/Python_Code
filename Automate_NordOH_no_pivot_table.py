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
import __future__
print str(xlrd.__VERSION__)
import sys
import re


'''
A. open up the file on command line
1. get text file into data frame - not working so parse line by line
2. open excel file to write to 
2A. write function to transform date
3. loop through text file line by line
4. update select * from DW_USERS.USER_MENS_WEDDING_XREF
'''

#argv for file
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

#df = pd.write_csv(awesome_output.csv, sep=',')
target_file = open('awesome_output.csv','w')

first_line = "Y"
list_line = []
count_array_elements = 0
inner_count = 0
count_lines_seen = 0

def printme( str ):
   "This prints a passed string into this function"
   print str
   return
   

with open('Extract.txt') as file:
    for line in file:
       count_lines_seen = count_lines_seen + 1
       if (count_lines_seen > 3):
           exit()
       list_line = line.split('\t')
       #print ("length of line is " + str(len(list_line)))
       #check to see if this is the first line in the file - header is formatted differently
       print (list_line)    
       
       if (first_line == "Y"): 
           first_line = "N"
           #check to see if it is the last element in the line - make sure no trailing ,         
           print ("list_line" + str(list_line))
           for line_element in list_line[:-1]:
               target_file.write(str(line_element)+',')
           print str(list_line[-1])
           target_file.write(str(list_line[-1]))
           continue

       #print "length of list_line is " + str(len(list_line))
       
       print str(len(list_line)) + "      dksdksdks\n"
       for i in range(0,20):
           if (i == 0):
               print str(list_line[0]) + " aaaaaaaaaaaaaaaaaa\n"
               (testing,y) = list_line[0].split(', ')
               print "JJJJJJJJJJJJJJJ" + str(testing)
               line_element_clean_e0 = (str(list_line[0].split(', ')[-1]))
               line_element_clean_e0 = line_element_clean_e0.translate(None, '"') 
               print str(line_element_clean_e0)
           elif (i == 1):
               print str(list_line[1]) + " bbbbbbbbbbbbbbbbbb\n"
               line_element_clean_e1 = (str(list_line[1].split(', ')[0]))
               line_element_clean_e1 = line_element_clean_e1.translate(None, '"') 
               print str(line_element_clean_e1)
           elif (i == 2):
               print str(list_line[2]) + " cccccccccccc\n"
               line_element_clean_e2 = (str(list_line[2].split(', ')[-1]))
               line_element_clean_e2 = line_element_clean_e2.translate(None, '"') 
               print str(line_element_clean_e2)
           elif (i == 3):
               print str(list_line[3]) + " ddddddddddd\n"
               line_element_clean_e3 = (str(list_line[3].split(', ')[-1]))
               line_element_clean_e3 = line_element_clean_e3.translate(None, '"') 
               print str(line_element_clean_e3)
           elif (i == 7):
               print str(list_line[7]) + " eeeeeeeeeeeeee\n"
               line_element_clean_e7 = (str(list_line[7]))
               line_element_clean_e7 = line_element_clean_e7.translate(None, '"') 
               print str(line_element_clean_e7)
           elif (i == 13):
               print str(list_line[13]) + " ffffffffffffffff\n"
               line_element_clean_e13 = (str(list_line[13]))
               line_element_clean_e13 = line_element_clean_e13.translate(None, '"') 
               print str(line_element_clean_e13)
           elif (i == 14):
               print str(list_line[14]) + " hhhhhhhhhhhhhhhh\n"
               line_element_clean_e14 = (str(list_line[14]))
               line_element_clean_e14 = line_element_clean_e14.translate(None, '"') 
               print str(line_element_clean_e14)
           elif (i == 6):
               print str(list_line[6]) + " eeeeeeeeeeeeee\n"
               line_element_clean_e6 = (str(list_line[6]))
               line_element_clean_e6 = line_element_clean_e6.translate(None, '"') 
               print str(line_element_clean_e6)
       target_file.write(str(line_element_clean_e0)+',')
       target_file.write(str(line_element_clean_e1)+',')
       target_file.write(str(line_element_clean_e2)+',')
       target_file.write(str(line_element_clean_e3)+',')
       target_file.write(str(line_element_clean_e7)+',')
       target_file.write(str(line_element_clean_e13)+',')
       target_file.write(str(line_element_clean_e14)+',')
       target_file.write(str(line_element_clean_e6))
       
       
       #    line_element_clean = (str(line_element.split(', ')[-1]))
       #    line_element_clean = line_element_clean.translate(None, '"') 
       #    #print str(line_element_clean) + "\n"
       #    target_file.write(str(line_element_clean)+',')
       #    target_file.write(str(line_element)+',')
       #print str(list_line[-1])
       #target_file.write(str(list_line[-1]))

target_file.close()

