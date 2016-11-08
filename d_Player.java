public class d_Player
{
  int number = 0;
  String name = "Stan";

  public void guess()
  {
   number = (int) (Math.random() * 10);
   System.out.println("I'm guessing" + number);

  }

  public void setName()
  {
	 name = "Alex";
     System.out.println("I'm guessing" + name);
  }



}