public class d_GuessGame
{
   d_Player Alex = new d_Player();
   d_Player Barry = new d_Player();
   d_Player Cathy = new d_Player();

   Alex.setName = "Alex";

   public void startGame()
   {

     int guessp1 = 0;
     int guessp2 = 0;
     int guessp3 = 0;

     boolean p1isRight = false;
     boolean p2isRight = false;
     boolean p3isRight = false;

     int targetNumber = (int) (Math.random() * 10);
     System.out.println("I'm thinking of a number between 0 and 9....");

     while(true)
     {
       System.out.println("Number to guess is " + targetNumber);

       Alex.guess();
       Barry.guess();
       Cathy.guess();

       guessp1= Alex.number;
       System.out.println("Player one guessed " + guessp1);

       guessp2= Barry.number;
       System.out.println("Player one guessed " + guessp2);

       guessp3= Cathy.number;
       System.out.println("Player one guessed " + guessp3);

       if (guessp1 == targetNumber)
       {
		   p1isRight = true;
	   }
	   if (guessp2 == targetNumber)
       {
		   p2isRight = true;
	   }
	   if (guessp3 == targetNumber)
	   {
	   	   p3isRight = true;
	   }

	   if (p1isRight || p2isRight || p3isRight )
	   {
		   System.out.println("Winner:");
		   System.out.println("Player one got it right " + p1isRight);
		   System.out.println("Player two got it right " + p2isRight);
		   System.out.println("Player three got it right " + p3isRight);
		   System.out.println("Game is over.");

		   break;
	   }
	   else
	   {
	     System.out.println("Players will have to try again.");
	   }
     }
   }

}