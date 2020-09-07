/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
import java.util.Scanner;



public class Main
{
  public static void main (String[]args)
  {


    int n;
    int msf = 0, meh = 0;
    int a[] = new int[10];
      System.out.println ("Enter the size of array: ");
    Scanner num = new Scanner (System.in);
      n = num.nextInt ();
      System.out.println ("Enter the array elements: ");
    for (int i = 0; i < n; i++)
      {
	Scanner anum = new Scanner (System.in);
	  a[i] = anum.nextInt ();
      }
    for (int j = 0; j < n; j++)
      {
	meh = meh + a[j];
	if (meh < a[j])
	  meh = a[j];
	if (msf < meh)
	  msf = meh;

      }
    System.out.println ("Contiguos sum of subarray is :" + msf);

  }
}
