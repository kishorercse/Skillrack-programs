"""
Given N, print the pattern as described in the Example Input/Output.

Input Format:
The first line will contain N.

Output Format:
N lines will contain the required pattern.

Boundary Conditions:
1 <= N <= 50

Example Input/Output 1:
Input:
5

Output:
1 2 3 4 5
2 4 6 8 4
4 8 12 10 8
8 16 18 20 10
16 26 36 28 20

Example Input/Output 2:
Input:
4

Output:
1 2 3 4
2 4 6 3
4 8 7 6
8 11 14 7

"""
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		int n=(new Scanner(System.in)).nextInt();
		long[] arr=new long[n], temp=new long[n];
		for(int i=1;i<=n;i++)
		{
		    arr[i-1]=i;
		    System.out.print(i+" ");
		}
		System.out.println();
		for(int i=1;i<n;i++)
		{
		    temp[0]=arr[1];
		    System.out.print(arr[1]+" ");
		    for(int j=1;j<n-1;j++)
		    {
		        temp[j]=arr[j-1]+arr[j+1];
		        System.out.print(arr[j-1]+arr[j+1]+" ");
		    }
		    temp[n-1]=arr[n-2];
		    System.out.println(arr[n-2]);
		    System.arraycopy(temp,0,arr,0,n);
		}

	}
}
