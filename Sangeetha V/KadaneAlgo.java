class KadaneAlgo
{
     public static void main(String args[])
    {
        int arr[]={1,-2,4,6,-3,7};
        System.out.println("The Maxsum contigous subarray is:"+MaxSubArray(arr));
    }
    static int MaxSubArray(int arr[])
    {
        int max_curr;
        int max_before;
        int a=arr.length;
        max_curr=max_before=arr[0];
        for(int i=1;i<a;i++)
        {
           max_curr=Math.max(arr[i],max_curr+arr[i]);
           if( max_curr>max_before)
           
            max_before=max_curr;
         }
        return max_before;
       }
       }