/*
A positive integer N and a digit D are passed as input to the program. The program must print the first multiple of N (which is greater than N) which has the same unit digit as D.

Boundary Condition(s):
1 <= N <= 9999
0 <= D <= 9

Input Format:
The first line contains N and D separated by a space.

Output Format:
The first line contains the integer value which is the first multiple of N which has the unit digit as D.

Example Input/Output 1:
Input:
24 2

Output:
72

Explanation:
24, 48, 72, 96, .. are multiples of 24.
The first multiple greater than N which has 2 as unit digit is 72 which is printed as the output.
 
Example Input/Output 2:
Input:
401 1

Output:
4411
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt(), d=sc.nextInt(), num=2*n;
		while(num%10!=d)
		    num+=n;
		System.out.print(num);

	}
}
