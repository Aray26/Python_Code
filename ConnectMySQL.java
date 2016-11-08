public static void main( String[] args ) throws ClassNotFoundException, SQLException
{
  // connection to JDBC using mysql driver
  Class.forName( "com.mysql.jdbc.Driver" );
  Connection connect = DriverManager.getConnection("jdbc:mysql://localhost/ + "user=root&password=root" );

   

        selectAll( connect );

 

        // close resources, in case of exception resources are not properly cleared


 
    }

     

    /**

     * select statement and print out results in a JDBC result set

     *

     * @param conn

     * @throws SQLException

     */
23
    private static void selectAll( java.sql.Connection conn ) throws SQLException
24
    {
25
        Statement statement = conn.createStatement();
26
 
27
        ResultSet resultSet = statement.executeQuery( "select x from dual" );
28
 
29
        while( resultSet.next() )
30
        {
31
            String name = resultSet.getString( "NAME" );
32
            String population = resultSet.getString( "POPULATION" );
33
 
34
            System.out.println( "NAME: " + name );
35
            System.out.println( "POPULATION: " + population );
36
        }
37
 
38
    }
