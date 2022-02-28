/*
There are N integers passed as the input. The program must print the minimum possible sub-array sum S as the output.

Boundary Condition(s):
1 <= N <= 10^5
-1000 <= Each integer value <= 1000

Input Format:
The first line contains N.
The second line contains the N integer values separated by a space.

Output Format:
The first line contains S. 

Example Input/Output 1:
Input:
6
-5 -2 9 -1 -8 -2

Output:
-11

Explanation:
The elements in a sub array must be continuous. The sub array having minimum sum is -1 -8 -2.

Example Input/Output 2:
Input:
6
-5 -2 4 -1 -8 -2

Output:
-14
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt(), arr[]=new int[n];
		for(int index=0;index<n;index++)
		    arr[index]=sc.nextInt();
	    int currSum=arr[0], minSum=arr[0];
	    for(int index=1;index<n;index++)
        {
            currSum=Math.min(arr[index], currSum+arr[index]);
            minSum=Math.min(minSum, currSum);
        }
        System.out.print(minSum);
	}
}
