class GoodDog
{
   private int size = 10;

   public void setSize(int s)
   {
	 size = s;
   }

   public int getSize()
   {
   	 return size;
   }

   void bark()
   {
	 if (size > 60)
	 {
		 System.out.println("LOUD BARK, LOUD BARK");
	 }
	 else if (size > 14)
	 {
		 System.out.println("Ruff, ruff");
	 }
	 else
	 {
		 System.out.println("Yip, yip");
	 }
   }
}