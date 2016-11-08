import java.sql.DriverManager;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Properties;

public class GetProduct_Dimension
{
  public static void main(String[] argv)
  {
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

            String sql ="select * from dw_common.product_dimension";

            //creating PreparedStatement object to execute query
            PreparedStatement preStatement = connection.prepareStatement(sql);

            ResultSet result = preStatement.executeQuery();

            while(result.next())
            {
               System.out.println("Current Date from Oracle : " +         result.getString("current_day"));
            }
            System.out.println("done");

//step5 close the connection object
connection.close();


		} catch (SQLException e) {

			System.out.println("Connection Failed! Check output console");
			e.printStackTrace();
			return;

		}


	}

}