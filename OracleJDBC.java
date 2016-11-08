import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

public class OracleJDBC
{
  public static void main(String[] argv)
  {
	//Get table and "string to find" information
	System.out.println("-------- Find a string within a table ------");
	Scanner userInput = new Scanner(System.in);
	
	
	System.out.println("Enter in the table name");
	String tableName = userInput.next();
	
	System.out.println("Enter in the \"thing\" to find");
	String findString = userInput.next();
	
	System.out.println("You are looking for "+ findString + " in the table "+ tableName);
		  
    System.out.println("-------- Oracle JDBC Connection Testing ------");
	try
	{
    	Class.forName("oracle.jdbc.driver.OracleDriver");
	}
	catch (ClassNotFoundException e)
	{
     System.out.println("Where is your Oracle JDBC Driver?");
	 e.printStackTrace();
	return;
   }
   System.out.println("Oracle JDBC Driver Registered!");
   
   Connection connection = null;
   try
   {
     connection = DriverManager.getConnection(
					"jdbc:oracle:thin:@ny-oracle-ts-01.Yurman.com:1521:dwtest01", "aray",
					"ar");

     String sqlQuery = "select * from DW_COMMON.USER_DIMENSION"; //"select sysdate as current_day from dual";

     ResultSet result = connection.createStatement().executeQuery(sqlQuery);
     ResultSetMetaData resultMetaData = result.getMetaData();
	 int columnsNumber = resultMetaData.getColumnCount();

     while(result.next())
     {
	   for (int i = 1; i <= columnsNumber; i++ )
	   {
	      if (result.getString(i).toUpperCase().contains(findString.toUpperCase()))
		  {			  
		    System.out.print(result.getString(i) + " "); //print row   
		  }
	   }
	   System.out.println();
       //System.out.print("Current Date from Oracle : " + result.getString("current_day"));
	   
	   
     }
     System.out.println("done");
            /*
			
			
			select * from DW_COMMON.USER_DIMENSION

			
			
			
			//Get column meta data for table
			String sqlColumnMetaData ="select sysdate as current_day from dual";

            //creating PreparedStatement object to execute query
            PreparedStatement preStatement2 = connection.prepareStatement(sqlColumnMetaData);

            ResultSet results2 = preStatement2.executeQuery();
			ResultSetMetaData = resultsColumnMetaData.getMetaData();
			//alternative getMetaData().getColumns(null, schema, tableName, "%")
			resultsColumnMetaData.getColumnType(1);
			resultsColumnMetaData.getColumnLabel(1);

            while(result.next())
            {
               System.out.println("Current Date from Oracle : " +         result.getString("current_day"));
            }
            System.out.println("done");
			
			//1. Loop through each row- 2. grab each cell 3. cast each cell into string 4. 
	/*		select * from 

select * from all_all_tables
where table_name like '%SALES%INV%HISTORY%'

select * from dw_temp.sales_inv_hist_month_snpshot
order by invoice_date desc

*/
			
        //step5 close the connection object
        connection.close();


		} catch (SQLException e) {

			System.out.println("Connection Failed! Check output console");
			e.printStackTrace();
			return;

		}

		/*if (connection != null)
          {
			System.out.println("You made it, take control your database now!");
		  } 
		 else 
		 {
			System.out.println("Failed to make connection!");
		 }*/
	}

}