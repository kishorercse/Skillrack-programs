/*
The program must accept an integer N as the input. The program must print the largest possible odd integer using all the digits in N as the output. If it is not possible to 
form such an integer, the program must print no as the output.

Boundary Condition(s):
10 <= N <= 10^17

Input Format:
The first line contains N.

Output Format:
The first line contains the largest possible odd integer using all the digits in N or no.

Example Input/Output 1:
Input:
120087460153

Output:
876543210001

Explanation:
The largest possible odd integer using all the digits in 120087460153 is 876543210001.

Example Input/Output 2:
Input:
246228

Output:
no
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		long N=sc.nextLong();
		int count[]=new int[10], unit=-1;
		while(N>0) {
		    count[(int)(N%10)]++;
		    N/=10;
		}
		for(int ctr=1;ctr<=9;ctr+=2) {
		    if (count[ctr]>0) {
		        unit=ctr;
		        count[ctr]--;
		        break;
		    }
		}
		if (unit==-1) {
		    System.out.print("no");
		    return;
		}
		int start=1;
		for(int ctr=9;ctr>=start;ctr--) {
		    while(count[ctr]>0) {
		        start=0;
		        System.out.print(ctr);
		        count[ctr]--;
		    }
		}
		System.out.print(unit);

	}
}
