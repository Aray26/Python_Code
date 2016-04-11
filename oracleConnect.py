import cx_Oracle

print ("test")

connection = cx_Oracle.connection('aray/ar@ny-oracle-ts-01.Yurman.com/dwtest01')


print (connection.version)
print ("test3")
connection.close()
#"jdbc:oracle:thin:@ny-oracle-ts-01.Yurman.com:1521:dwtest01", "aray",
#					"ar");
