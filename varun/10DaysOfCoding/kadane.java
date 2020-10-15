public class GFG { 

	static void maxSubArraySum(int a[], int size) 
	{ 
	    int max = Integer.MIN_VALUE, 
		max_end = 0,start = 0, 
		end = 0, s = 0; 
		for (int i = 0; i < size; i++) 
		{ 
			max_end += a[i]; 
			if (max < max_end) 
			{ 
			    max = max_end; 
				start = s; 
				end = i; 
			} 
			if (max_end < 0) 
			{ 
				max_end = 0; 
				s = i + 1; 
			} 
		} 
		System.out.println("Maximum continuous sum is "+ max); 
		System.out.println("Starting index " + start); 
		System.out.println("Ending index " + end); 
	} 
	public static void main(String[] args) 
	{ 
		int a[] = { -5, -2, 9, 4, 7, -3 }; 
		int n = a.length; 
		maxSubArraySum(a, n); 
	} 
} 
