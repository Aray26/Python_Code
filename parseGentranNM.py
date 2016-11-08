import csv 
import os

file_out=open("Output.csv","w")
file_out.write("TESTING\n")
file_out.write("Date;VendorDepartment;VendorCode;Store;DepartmentCode;Class;Style;VendorStyleName;Color;Size;SALES;ONHAND\n")

file_in=open("David_Yurman1640.csv","r")
file_in.next() # skip the header
for line in file_in:
    eachLine = line.split(",")
    print "UPC " + str(eachLine[0])
    vendor = str(eachLine[1])
    print "Vendor " + str(eachLine[1])
    print "Department " + str(eachLine[2])
    department = str(eachLine[2])
    print "Class " + str(eachLine[3])
    class_value = str(eachLine[2])
    print "Style " + str(eachLine[4])
    print "Color " + str(eachLine[5])
    print "Size " + str(eachLine[6])
    print "Vendor_Style " + str(eachLine[7])
    vendor_style = str(eachLine[7])
    print "Store_Id " + str(eachLine[8])
    store_id = str(eachLine[8])
    print "On_Order " + str(eachLine[9])
    print "On_Hand_Units " + str(eachLine[10])
    print "?Column? " + str(eachLine[11])
    print "Reg_Sales_Units " + str(eachLine[12])
    print "Reg_Sales_Dol " + str(eachLine[13])
    print "Mkd_Sales_Units " + str(eachLine[14])
    print "Mkd_Sales_Dol " + str(eachLine[15])
    print "Day_Daye " + str(eachLine[16])
    file_out.write("11/2/2013|")
    file_out.write(vendor+"00"+department+"|")
    file_out.write(vendor+"|")
    file_out.write(store_id+"|")
    file_out.write(department+"|")
    file_out.write(class_value+"|")
     department

    break
    
    
    #for elements in line.split(","):
    #    print (elements) #file_out.write(line)
    
         
		 
file_in.close() # not really needed
file_out.close()