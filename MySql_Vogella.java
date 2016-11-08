import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Date;

public class MySql_Vogella
{
   public static void main(String[] argv)
   {
       Connection connection = null;
       Statement statement = null;
       PreparedStatement preparedStatement = null;
       ResultSet resultSet = null;


      try
      {
      // This will load the MySQL driver, each DB has its own driver
      Class.forName("com.mysql.jdbc.Driver");
      // Setup the connection with the DB
      connection = DriverManager.getConnection("jdbc:mysql://localhost/test?user=sqluser");
//      "jdbc:oracle:thin:@ny-oracle-ts-01.Yurman.com:1521:dwtest01", "aray",
//                    "ar");

      }
    catch (ClassNotFoundException e)
    {
        System.out.println("Where is your MySQL JDBC Driver?");
        e.printStackTrace();
       return;
    }
   System.out.println("MySQL JDBC Driver Registered!");
}
}

