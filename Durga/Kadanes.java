import java.util.Scanner;

public class Kadanes
{
    public static int getMaxSubarraySum(int[] array){
    int currentMax = Integer.MIN_VALUE;
    int totalMax =  Integer.MIN_VALUE;

    for(int i = 0; i < array.length; i++){
        currentMax = Math.max(currentMax, 0) + array[i];
        totalMax = Math.max(totalMax, currentMax);
        }
    return totalMax;
    }
    public static void main(String args[])
    {
        int a[] = {1,2,-2,4,5};
        System.out.println(Kadanes.getMaxSubarraySum(a));
    }
    
}
