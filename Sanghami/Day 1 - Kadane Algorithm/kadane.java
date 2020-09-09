
/**
 * Write a description of class kadane here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
class Kadane
{
	// Function to find contiguous sub-array with the largest sum
	// in given set of integers
	public static int kadane(int[] A)
	{
		// stores maximum sum sub-array found so far
		int maxSoFar = 0;

		// stores maximum sum of sub-array ending at current position
		int maxEndingHere = 0;

		// traverse the given array
		for (int i: A)
		{
			// update maximum sum of sub-array "ending" at index i (by adding
			// current element to maximum sum ending at previous index i-1)
			maxEndingHere = maxEndingHere + i;

			// if maximum sum is negative, set it to 0 (which represents
			// an empty sub-array)
			maxEndingHere = Integer.max(maxEndingHere, 0);

			// update result if current sub-array sum is found to be greater
			maxSoFar = Integer.max(maxSoFar, maxEndingHere);
		}

		return maxSoFar;
	}

	public static void main(String[] args)
	{
		int[] A = { -2, 1, -3, 4, -1, 2, 1, -5, 4 };

		System.out.println("The sum of contiguous sub-array with the " +
							"largest sum is " + kadane(A));
	}
}