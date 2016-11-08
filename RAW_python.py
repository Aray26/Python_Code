from __future__ import division
import datetime
import calendar
import cx_Oracle
import sys
import os
import pandas
from datetime import timedelta, date


#C:\Python27\;C:\Anaconda2\Lib;

print ("Ticket 22984 -  PRODUCT_DIMENSION.UNIT_TOTAL_CUR_COST")
os.environ['ORACLE_HOME'] = '/oracle_64/orahome11g/'
os.environ['LD_LIBRARY_PATH'] = '/oracle_64/orahome11g/lib'

#construct = 'aray/ar@ny-oracle-ts-01.Yurman.com:1521/dwtest01'
#construct = 'qad/mfg@ny-oracle-pr-02.Yurman.com:1521/dwprod01'
construct = 'qad/mfg@ny-oracle-ts-01.Yurman.com:1521/dwtest01'
print ("The construct is...  " + construct)
conn = cx_Oracle.connect(construct)
conn2 = cx_Oracle.connect(construct)

cursorOracle = conn.cursor()
cursorOracle2 = conn2.cursor()

#grab list of item_codes where unit_total_cur_cost = 0
sqlStatement = "select kwi_employee_nbr from retail_mart_merge.LU_RETAIL_SALES_REP_ALL where employee_type is null "
employees = cursorOracle.execute(sqlStatement)

totalEmployeesCodes=0
badItemCodes=0
goodItemCodes=0


for itemCode in itemCodes:
    print ("PRINT itemCode is just " + str(itemCode))
 
    #if (totalItemCodes >= 5):
    #    break
    #else:
    totalItemCodes = totalItemCodes + 1
    #   print ("HERE")
        
   
    #grab sum amount and prod amount then compare
    #prodStatement = 'select CURRENT_COST from DW_COMMON.VW_ITEM_MASTER@prod where item_number = \'%s\'' % (itemCode[0])   
    prodStatement = 'select CURRENT_COST from DW_COMMON.VW_ITEM_MASTER where item_number = \'%s\'' % (itemCode[0])   
    prodValue = cursorOracle2.execute(prodStatement)
    
    for prodCurrentCost in prodValue:
        print ("---------------------")
        print ("Current Cost from Prod query---: ", (prodCurrentCost))
        print ("---------------------")
    
        productionStatement = """select sum(lower_level_cost + this_level_cost) 
                             from DW_COMMON.COST_DIMENSION, dw_stage.pt_mstr 
                             where COST_SET_CODE = \'CURRENT\' 
                             and ITEM_CODE = PT_MSTR.PT_PART 
                             and item_code = \'%s\'""" % (itemCode)
    
        #productionStatement = """select sum_level_costs 
        #                      from ar_test_tix22984
        #                      where item_code = \'%s\'""" % (itemCode)
    
        print "////////////////////"
        print (productionStatement)
        print "////////////////////" 
    
        print ("Current Cost from productionStatement query---: ", (productionStatement))
        productionValue = cursorOracle2.execute(productionStatement)
    
        for productionCurrentCost in productionValue:
            print ("////////////////")
            if (productionCurrentCost == prodCurrentCost):
               equality = "yes"
               results.write(str(itemCode[0]) +',' + str(prodCurrentCost[0]) + ',' + str(productionCurrentCost[0]) + ',' + str(equality) +'\n')
               goodItemCodes = goodItemCodes +1 
               print ("Match! " + str(goodItemCodes))
            else: 
               equality = "no"
               badResults.write(str(itemCode[0]) +',' + str(prodCurrentCost[0]) + ',' + str(productionCurrentCost[0]) + ',' + str(equality) +'\n')
               badItemCodes = badItemCodes +1 
               print ("No Match! " + str(badItemCodes))
    
results.write(str(itemCode[0]) +',' + str(prodCurrentCost[0]) + ',' + str(productionCurrentCost[0]) + ',' + str(equality) +'\n')
    

print ("Why am I ending up here out of the loop!")

print ("badItemCodes " + str(badItemCodes))
print ("goodItemCodes " + str(goodItemCodes))
print ("totalItemCodes " + str(totalItemCodes))
percentageBadItemCodes = (badItemCodes/totalItemCodes)
print (str(round(percentageBadItemCodes * 100, 2)) +"%")


cursorOracle.close()
cursorOracle2.close()

conn.close()
conn2.close()
results.close()
