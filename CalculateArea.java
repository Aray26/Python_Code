import java.util.Scanner;

class CalculateArea
{
  public static void main(String[] args)
  {
    Scanner userInputScanner = new Scanner(System.in);
    int choice = 0;
    int a = 0;
    int width = 0;
    int height = 0;
    int base = 0;
    int radius = 0;

    System.out.println("Welcome - Pick a shape");
    System.out.println("1. Square");
    System.out.println("2. Rectangle");
    System.out.println("3. Triangle");
    System.out.println("4. Circle");
    System.out.print("\nWhat is your shape? ");
    choice = userInputScanner.nextInt();

    if (choice == 1)
    {
		System.out.print("\n-->You choose square. What is the length of a side ?   " );
        int length = userInputScanner.nextInt();
        int square = length * length;
		System.out.print("\nThe area of the square = " + square + "\n");
	}
    else if (choice == 2)
    {
		System.out.print("\nThe area of the rectangle = " );//+ rectangle + "\n");
	}



   }
}