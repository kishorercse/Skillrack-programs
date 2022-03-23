/*
There are N empty buckets in a row. Every second, a certain number of balls fill each bucket. The maximum capacity of each bucket is K. If the number of balls exceeds 
the maximum capacity of a bucket, the remaining balls will overflow. When a bucket is full or overflowing, a boy collects the balls from the bucket and empties the
bucket again. The program must accept an integer matrix of size T*N representing the number of balls that fall into N buckets in T seconds and the value of K as the
input. The program must print the number of balls he can collect as the output. At T = 1, the balls in the last row of the matrix will fall into the N buckets.
At T = 2, the balls in the last but one row of the matrix will fall into the N buckets and so on.

Boundary Condition(s):
1 <= T, N <= 50
1 <= Matrix element value <= 1000
1 <= K <= 10^4

Input Format:
The first line contains T and N separated by a space.
The next T lines, each containing N integers separated by a space.
The T+2nd line contains K.

Output Format:
The first line contains the number of balls the boy can collect.

Example Input/Output 1:
Input:
5 5
1 1 5 1 4
5 4 3 2 4
3 4 3 2 2
5 1 4 1 3
1 4 2 2 2
8

Output:
48

Explanation:
After 1 second, the balls in the 5 buckets are 1 4 2 2 2.
After 2 seconds, the balls in the 5 buckets are 6 5 6 3 5.
After 3 seconds, the balls in the 5 buckets are 0 0 0 5 7 (The balls from the buckets 1, 2 and 3 are collected by the boy).
After 4 seconds, the balls in the 5 buckets are 5 4 3 7 0 (The balls from the bucket 5 are collected by the boy).
After 5 seconds, the balls in the 5 buckets are 6 5 0 0 4 (The balls from the buckets 3 and 4 are collected by the boy).
The total number of balls collected is 48 (6 buckets * 8 balls = 48 balls), which is printed as the output.

Example Input/Output 2:
Input:
6 7
4 6 4 8 6 2 5
7 6 2 1 1 6 8
2 2 6 5 6 1 8
4 3 6 6 7 7 9
5 9 9 1 7 1 3
9 8 1 2 7 5 2
22

Output:
154
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt(), n=sc.nextInt(), mat[][]=new int[t][n];
		for(int i=0;i<t;i++) {
		    for(int j=0;j<n;j++) {
		        mat[i][j]=sc.nextInt();
		    }
		}
		int k=sc.nextInt(), arr[]=new int[n], collected=0;
		for(int i=t-1;i>=0;i--) {
		    for(int j=0;j<n;j++) {
		        arr[j]+=mat[i][j];
		        if (arr[j]>=k) {
		            collected++;
		            arr[j]=0;
		        }
		    }
		}
		System.out.print(collected*k);
	}
}
