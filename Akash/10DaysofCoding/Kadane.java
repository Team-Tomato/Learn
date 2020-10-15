import java.util.*;

public class Kadane {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter the number of elements:");
		int n = scan.nextInt();
		int[] a = new int[n];
		for(int i=0;i<n;i++)
		{
			a[i] = scan.nextInt();
		}
		int meh = 0, msf = Integer.MIN_VALUE;
		for(int i = 0;i<n;i++)
		{
			meh = meh + a[i];
			if(msf<meh)
				msf = meh;
			if(meh<0)
				meh = 0;
		}
		System.out.print(msf);
		scan.close();
	}

}
