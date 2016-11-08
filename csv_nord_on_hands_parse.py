import cx_Oracle
import os
from datetime import timedelta, date, datetime
import pandas as pd
import time



os.environ['ORACLE_HOME'] = '/oracle_64/orahome11g/'
os.environ['LD_LIBRARY_PATH'] = '/oracle_64/orahome11g/lib'
#construct = 'qad/mfg@ny-oracle-ts-01.Yurman.com:1521/dwtest01'  #TEST
#construct = 'qad/mfg@ny-oracle-pr-02.Yurman.com:1521/dwprod01' #PRODUCTION
#construct = 'APPS_RO/APPS_RO@oraebsscdb1.nav.yurman.com:1552/DYEDEV01' 
construct = 'APPS_RO/APPS_RO@oraebsscdb2.nav.yurman.com:1562/DYEUAT1'
#construct = 'APPS_RO/APPS_RO@oraebsaddb2-vip.nav.yurman.com:1552/DYEPRD1' #PRODUCTION


conn = cx_Oracle.connect(construct)
cursorOracle = conn.cursor()

def QueryDatabase(year,month,days_to_add):
    print year
    print month
    print days_to_add
     #Get the highest ticket number from table - will be something like "H74961". Cut off H.
    selectStatement = ("select trunc(start_date) + " + str(days_to_add) + " from apps.gl_periods " \
                       "where period_year = " + str(year) + " and period_num = " + str(month))
    print "selectStatement is " + str(selectStatement)
    selectResults = cursorOracle.execute(selectStatement)
    print selectResults
    date_result = selectResults.fetchone()
    
    dt = datetime(date_result)
    print "0000000000000000000000000"
    date_final = str(dt.strftime("%m-%d-%Y"))
    print "the date_result is " + str(date_result)
    print "the date_final is " + str(date_final)
    
    print "XXXXXXXXXXXXXXXXXXXXXXXX"
    #for maxTicketValue in selectResults:
    #    print "maxTicketValue " + str(maxTicketValue)
    print "YYYYYYYYYYYYYYYYYYYYYYYYYYYY"
    return date_final
    
#for maxTicketValue in selectResults:

csv_file = open('incoming_template.csv')

list_line_elements =[]
parsed_line_elements=[]
i = 0



def last_day(d, day_name):
    days_of_week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]
    print days_of_week.index(day_name.lower())
    target_day = days_of_week.index(day_name.lower())
    delta_day = target_day -d.isoweekday()
    print "d.isoweekly " + str(d.isoweekday())
    print delta_day
    if delta_day >= 0:
        delta_day -= 7
    date_formatted = d + timedelta(days=delta_day)
    print type(date_formatted)
    print date_formatted.date()
    return d + timedelta(days=delta_day)

print datetime.today()    
print last_day(datetime.today(),'sunday')


for individual_row in csv_file:
    print individual_row
    print type(individual_row)
    list_line_elements = individual_row.split('",')
    print "POOOP" + str(type(list_line_elements))
    print "++++++"
    
    for num, element in enumerate(list_line_elements):
        #print str(num) + " " + str(element)
        if num == 0:
            print "num " + str(num) + " " + str(element)
            parsed_line_elements.insert(num,element.split(',')[1].strip())
            print "parsed_line_elements 0 " + str(parsed_line_elements)
            print "length of list is " + str(len(parsed_line_elements))
        elif num == 1:
            print "-----------------"
            print "num " + str(num) + " " + str(element)
            insert = element.split(',')[0].strip('"').strip()
            #parsed_line_elements.insert(num,element.split(',')[0].strip('"').strip())
            parsed_line_elements.append(insert)
            print "parsed_line_elements 1 " + str(parsed_line_elements)
            print "length of list is " + str(len(parsed_line_elements))
        elif num == 2:
            print "num " + str(num) + " " + str(element)
            insert = (element.split(',')[1].strip('"').strip())
            parsed_line_elements.append(insert)
            print "parsed_line_elements 1 " + str(parsed_line_elements)
        elif num == 3:
            print "num " + str(num) + " " + str(element)
            insert = (element.split(',')[0].strip('"').strip())
            parsed_line_elements.append(insert)
            #parsed_line_elements.append(element.split(',')[0].strip('"').strip())
            print "parsed_line_elements 1 " + str(parsed_line_elements)
        elif num == 4:
            print "date num " + str(num) + " " + str(element)
            year = (element.split(',')[0].strip('"').strip())
            month = (element.split(',')[1].strip('"').strip())
            week = ((element.split(',')[2].strip('"').replace('Wk','').strip()))
            days_to_add = (int(week) -1) * 7
            print "week " + str(week)
            print "days_to_add " + str(days_to_add)
            print year
            print month
            print "weekly " + str(week)
            date_final = QueryDatabase(year,month,days_to_add)
            print "date_final is " + str(date_final)
            parsed_line_elements.append(date_final)
            #parsed_line_elements.append(database_insert)
        elif num == 5:
            print "num " + str(num) + " " + str(element)
        elif num == 6:
            print "num " + str(num) + " " + str(element)
        elif num == 7:
            print "num " + str(num) + " " + str(element)
        else:
            pass
        print "Total parsed_line_elements " + str(parsed_line_elements)
        #del parsed_line_elements[:]


    if i > 3: 
        exit()
    else: 
        i += 1
    print "parsed_line_elements " + str(parsed_line_elements)
    del parsed_line_elements[:]

csv_file.close()

cursorOracle.close()
conn.close()

