
public class Kadane
{
    static int MaxSubarray(int a[])
    {
        int Max_current = a[0];
        int Max_Global = a[0];
        for(int i=1;i<a.length;i++)
        {
            if(Max_current < 0)
            Max_current = a[i];
            else
            Max_current += a[i];
            if(Max_current >= Max_Global )
            Max_Global = Max_current;
        }
       return Max_Global;
    }
    public static void mian()
    {
        int a[] = {-2,3,2,-1};
        System.out.println("Maximum sum of the sub array is : " +MaxSubarray(a));
    }
    
}
