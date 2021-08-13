/*

Given two integers M and N as input, the program must apply the bitwise AND operation for the odd numbers between M and N(inclusive) as S1 and apply the bitwise OR operation for the even numbers between M and N(inclusive) as S2. Finally, XOR the bits of S1 and S2 and print it.

Boundary Condition(s):
1 <= M < N 
M < N <=999999

Input Format:
The first line contains the M and N value separated by space.

Output Format:
The first line contains the integer value.

Example Input/Output 1:
Input:
3 6

Output:
7

Explanation :
By applying bitwise AND operation for 3 and 5 is 1, bitwise OR operation for 4 and 6 is 6, and bitwise XOR operation for 1 and 6 is 7

Example Input/Output 2:
Input:
10 16

Output:
23
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
		int m=sc.nextInt(),n=sc.nextInt(),a=m+(m%2==0?1:0),b=m+(m%2!=0?1:0);
		for (int i=a+2;i<=n;i+=2){
		    a&=i;
		}
		for (int i=b+2;i<=n;i+=2){
		    b|=i;
		}
		System.out.print(a^b);

	}
}
