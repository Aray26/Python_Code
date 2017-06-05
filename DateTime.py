import datetime
#import pyodbc
import sys

now = datetime.datetime.now()
print (now.year)
print (now.month)
print (now.minute, now.second, now.microsecond)


print ("Configurations")
print (sys.version) + str("\n")
print str(sys.version_info) + str("\n")
print (sys.path)

