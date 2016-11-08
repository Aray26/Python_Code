from datetime import datetime, timedelta
import time

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

    
print last_day(datetime.today(),'sunday')