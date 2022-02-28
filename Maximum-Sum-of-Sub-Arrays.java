/*
The program must accept an array of N integers as the input. The program must print the maximum sum of sub-arrays in the given array as the output.

Boundary Condition(s):
1 <= N <= 10^6
-1000 <= Each integer value <= 1000

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains the maximum sum of sub-arrays in the given array.

Example Input/Output 1:
Input:
5
3 2 -2 5 -4

Output:
8

Explanation:
The sub-array with the maximum sum 8 is given below.
3 2 -2 5

Example Input/Output 2:
Input:
3
-5 -4 -6

Output:
-4


*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt(), arr[]=new int[n];
		for(int index=0;index<n;index++)
		    arr[index]=sc.nextInt();
		int currSum=arr[0], maxSum=arr[0];
		for(int index=1;index<n;index++)
		{
		    currSum=Math.max(arr[index], currSum+arr[index]);
		    maxSum=Math.max(maxSum, currSum);
		}
		System.out.print(maxSum+" ");

	}
}
