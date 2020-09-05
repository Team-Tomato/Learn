import java.util.*;
import java.io.*;
public class Kadane{
    public static void main(String[] args){
        int i,n,maxnum,currnum;
        System.out.println("Enter the total elements:");
        Scanner s=new Scanner(System.in);
        n=s.nextInt();
        int arr[]=new int[n];
        for(i=0;i<n;i++){
            arr[i]=s.nextInt();
        }
        maxnum=currnum=arr[0];
        for(i=0;i<n;i++){
            if(currnum<0)
                currnum=arr[i];
            else
                currnum=currnum+arr[i];
            maxnum=Math.max(maxnum,currnum);
        }
        System.out.println(maxnum);
    }
}
