import java.lang.*;

public class Kandane {

	public static void main(String[] args)
	{
		int[] arr = {-2, 3, 2, -1};
		System.out.println("Maximum contigious sum is "+algo(arr));		
	}
	static int algo(int arr[])
	{
		int curr_max,final_max;
		curr_max = final_max = arr[0];
		
		for (int i = 1; i < arr.length; i++) {
			curr_max = Math.max(arr[i], curr_max+arr[i]);
			if (curr_max>final_max) {
				final_max = curr_max;
			}
		}
		
		return final_max;
	}

}
