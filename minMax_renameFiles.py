import os
import time
import fnmatch
import datetime

#get directory list of files
#find only files that are with DY*EU
#find only files that are with DY*
#find only files that are with DY*CA



""" 
Renames the filenames within the same directory to be Unix friendly
(1) Changes spaces to hyphens
(2) Makes lowercase (not a Unix requirement, just looks better ;)
Usage:
python rename.py
"""

#import my date function

#path =  'H:/Data Warehouse/KWI Refresh Data/'
path =  'H:/Data Warehouse/KWI Refresh Data/'

#S:\SHARED-DEPARTMENT-FOLDERS\SALES ADMINISTRATION\Retail Buying\KWI Uploads\MinMax\drop
#path =  'C:/Data/'

allFiles = os.listdir(path)

for filename in allFiles:
    print "Filename is " + filename
    filenameM = os.path.join(path, filename)
    
    #if fnmatch.fnmatch(filenameM, path+'DY*.txt'): 
    if filename.startswith('DY'):
       print "YYYYYYYYYY "+(filename)
       st = datetime.datetime.now() #strftime('%Y-%m-%d%H:%M:%S')
       formattedDate = str(st.strftime("%m%d%y"))+"-"+str(st.strftime("%H%M%S"))
       splitFilename = filename.split('.')
       newFilename = splitFilename[0]+formattedDate+str('.txt')
       print "testing " + newFilename
       #os.rename(filename, newFilename[0]+formattedDate+str('.txt'))
       os.rename(os.path.join(path,filename), os.path.join(path, newFilename))
       #print "PPPPP  " + filename
       #print "MMMMM  " + newFilename[0]
       #print "MMMMM  " + newFilename       

       #newFilename = 
       #    os.rename(filename, newFilename.append("bbbb").upper())
#  >>> d.strftime("%d/%m/%y")
#'11/03/02'
#>>> d.strftime("%A %d. %B %Y")