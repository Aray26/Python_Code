class e_TapeDeckTestDrive
{
  public static void main(String[] args)
  {

    e_TapeDeck t = new e_TapeDeck();
    t.canRecord = true;
    t.playTape();

    if (t.canRecord == true)
    {
      t.recordTape();
    }
  }
}