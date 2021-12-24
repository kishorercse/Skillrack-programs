/*
Given N positive integers, find the minimum sum S that can be obtained by adding exactly M out of the N integers. The program must print the value of the minimum sum S.

Input Format:
The first line will contain N and M separated by a space.
The second line will contain the values of N positive integers separated by a space.

Output Format:
First line will contain S.

Boundary Conditions:
3 <= N <= 50
2 <= M <= N

Example Input/Output 1:
Input:
5 2
9 2 1 5 4

Output:
3

Explanation:
Out of the five given numbers, the sum of 1+2 = 3 is the least sum and hence printed as the output.
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt(),m=sc.nextInt();
		int arr[]=new int[n], sum=0;
		for(int i=0;i<n;i++)
		    arr[i]=sc.nextInt();
		Arrays.sort(arr);
		for(int i=0;i<m;i++)
		    sum+=arr[i];
		System.out.print(sum);

	}
}
