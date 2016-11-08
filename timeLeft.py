import datetime
import numpy as np
import time
from datetime import timedelta

d1 = datetime.date.today()
d2 = datetime.date(2016,8,5)
d3 = datetime.date(2016,01,20)
print "Today is " + str(d1)
print "Go live is " + str(d2)

print str((d2-d1).days -1) + ' absolute days that are left before go-live'

days = np.busday_count(d1,d2) -1 

print "Days without weekends " + str(days) + " !!!! "




#time_used_in_current_day = datetime.strftime("%H:%M:%S")

#time_to_go_home = datetime.strptime("18:30:00")

#print time_to_go_home
#print time_used_in_current_day

#d1 = datetime.strptime(str(time_to_go_home), "%Y-%m-%d %H:%M:%S")
#d2 = datetime.strptime(str(time_used_in_current_day), "%Y-%m-%d %H:%M:%S")

#print(d1 - d2)




#time_left_in_day=(datetime.datetime.fromtimestamp(time_to_go_home) - datetime.datetime.fromtimestamp(time_used_in_current_day))

#print time_left_in_day.total_hours()


#print('difference is {0} seconds'.format(abs(diff.total_seconds())))

#print "\n\n\n\nOther stuff\n"
#choice = 'ham'

#print ({'spam':1.25, 
#        'ham':33}[choice])
