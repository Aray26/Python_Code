class f_dvdPlayerTestDrive
{
  public static void main(String[] args)
  {
    f_dvdPlayer d = new f_dvdPlayer();
    d.canRecord = true;
    d.playDVD();

    if (d.canRecord == true)
    {
      d.recordDVD();
    }

  }

}