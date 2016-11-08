class Doggie
{
  //int size;
  String name;

  int bark(int size)
  {
    if (size > 60)
    {
	  System.out.println("size incoming " + size);
      System.out.println("Woof! Woof!");
      size = 800;
      System.out.println("size outgoing " + size);
      return size;
    }
    else if (size > 14)
    {
      System.out.println("Ruff! Ruff!");
    }
    else
    {
      System.out.println("Yip! Yip!");
    }
    return 700;
  }
}