public class GoodDogTestDrive
{
	public static void main(String[] args)
	{

		GoodDog doggie = new GoodDog();
		System.out.println("doogie.getSize = " + doggie.getSize());

		doggie.setSize(100);
        System.out.println("doogie.getSize is now = " + doggie.getSize());

		GoodDog doggie2 = new GoodDog();
        System.out.println("doogie2.getSize = " + doggie2.getSize());

		doggie2.setSize(50);
        System.out.println("doogie2.getSize is now = " + doggie2.getSize());


        System.out.print("doogie.bark() ");
        doggie.bark();
        System.out.print("doogie2.bark() ");
        doggie2.bark();

	}
}