import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Date;

public class MySqlConnection
{
   public static void main(String[] argv)
   {
      try
      {
      // This will load the MySQL driver, each DB has its own driver
      Class.forName("com.mysql.jdbc.Driver");
      // Setup the connection with the DB
     // connect = DriverManager
     //     .getConnection("jdbc:mysql://localhost/football?"
     //         + "user=root");
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
