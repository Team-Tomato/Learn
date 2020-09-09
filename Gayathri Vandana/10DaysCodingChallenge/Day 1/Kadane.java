
public class Kadane {
    public static void main(String args[])
    {
       int m[] = {-2,1,-3,4,-1,2,1,-5,4};
       int maxSum = Integer.MIN_VALUE, curSum = 0;
       for(int i=0;i<m.length;i++)
       {
          curSum = curSum + m[i];
           if(maxSum < curSum)
               maxSum = curSum;
           if(curSum < 0)
               curSum = 0;
       }
      System.out.println("Maximum sum of subarray is "+ maxSum);
    }
}
