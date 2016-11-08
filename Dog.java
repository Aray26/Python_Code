public class Dog
{
  String name;

  public void bark()
  {
    System.out.println(name + " says Ruff!!");
  }


  public static void main(String[] args)
  {
    Dog dog1 = new Dog();
    dog1.bark();
    dog1.name = "Bart";

    Dog[] allMyDogs = new Dog[5];

    allMyDogs[0] = new Dog();
    allMyDogs[1] = new Dog();
    allMyDogs[2] = dog1;

    allMyDogs[0].name = "Fred";
	allMyDogs[1].name = "Bart";

	System.out.print("last dog's name is ");
	System.out.println(allMyDogs[2].name);

    int x = 0;
    while (x < allMyDogs.length())
    {
		allMyDogs[x].bark();
		x = x+1;
	}
  }

}