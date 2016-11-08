from __future__ import division
import datetime
import calendar
import cx_Oracle
import sys
import os
from datetime import timedelta, date


print ("Fix ext_purch_cost_received is null in dw_history.purchase_receipt_history from Jan 01 , 2012 ")
os.environ['ORACLE_HOME'] = '/oracle_64/orahome11g/'
os.environ['LD_LIBRARY_PATH'] = '/oracle_64/orahome11g/lib'

#construct = 'aray/ar@ny-oracle-ts-01.Yurman.com:1521/dwtest01'
construct = 'qad/mfg@ny-oracle-pr-02.Yurman.com:1521/dwprod01'

print ("The construct is...  " + construct)
conn = cx_Oracle.connect(construct)
conn2 = cx_Oracle.connect(construct)

cursorOracle = conn.cursor()
cursorOracle2 = conn2.cursor()


#get list of dw_history.purchase_receipt_history records where ext_purch_cost_received is null and receipt_date >= 01-JAN -2012
#update them with data from dw_test.test_ar_fix_data
 
sqlStatement = ("select prh.receiver_id, " 
                "prh.purchase_order_nbr, "
                "prh.line_nbr, "
                "prh.cost_element "
                "from dw_history.purchase_receipt_history prh, dw_test.test_ar_fix_data ard "
                "where prh.receiver_id = ard.receiver_id "
                "and   prh.purchase_order_nbr = ard.purchase_order_nbr "
                "and   prh.line_nbr = ard.line_nbr "
                "and   prh.cost_element = ard.cost_element "
                "and   prh.ext_purch_cost_received is null "
                "and   ard.ext_purch_cost_received is not null "
                "and   prh.receipt_date >= '01-JAN-2012' "
                "and   ard.receipt_date >= '01-JAN-2012' ")

print sqlStatement



rowsToUpdate = cursorOracle.execute(sqlStatement)
totalRowsUpdated = 0

for rowToUpdate in rowsToUpdate:
    receiver_id = rowToUpdate[0]
    purchase_order_nbr = rowToUpdate[1] 
    line_nbr = rowToUpdate[2]
    cost_element = rowToUpdate[3] 
    
    #update the table purchase_receipt_history from dw_test.test_ar_fix_data
    updateStatement = ("update dw_history.purchase_receipt_history prd " 
                       "set prd.ext_purch_cost_received = "
                       " (select ard.ext_purch_cost_received from dw_test.test_ar_fix_data ard " 
                       "  where ard.receiver_id = '"+ str(receiver_id) +"' and " 
                       "        ard.purchase_order_nbr = '"+ str(purchase_order_nbr) +"' and " 
                       "        ard.line_nbr = '"+str(line_nbr)+"' and " 
                       "        ard.ext_purch_cost_received is not null and "
                       "        ard.cost_element = '"+str(cost_element)+"') " 
                       "where prd.receiver_id = '"+ str(receiver_id) +"' and " 
                       "      prd.purchase_order_nbr = '"+ str(purchase_order_nbr) +"' and " 
                       "      prd.line_nbr = '"+str(line_nbr)+"' and " 
                       "      prd.cost_element = '"+str(cost_element)+"' and " 
                       "      prd.ext_purch_cost_received is null and " 
                       "      receipt_date >= '01-JAN-2012' ")

    print "\n\n updateStatement " + updateStatement + "\n"
 #   if (totalRowsUpdated > 3):
 #      break

    updateValue = cursorOracle2.execute(updateStatement)
    conn2.commit()
    totalRowsUpdated = totalRowsUpdated  + 1

cursorOracle2.close()
cursorOracle.close()

print ("totalRowsUpdated "+ str(totalRowsUpdated))

conn2.close()
conn.close()