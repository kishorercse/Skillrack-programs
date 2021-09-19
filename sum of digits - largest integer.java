/*
The program must accept N integers as the input. The program must print the sum of the digits of the 
largest integer among the N integers as the output.

Boundary Condition(s): 
1 <= N <= 100 
1 <= Each Integer Value <= 1000 

Input Format: 
The first line contains the integer N. 
The second line contains N integers separated by space(s). 

Output Format: 
The first line contains the sum of the digits of the largest integer among N integers.

Example Input/Output 1: 
Input: 
6 
98 74 85 23 58 21 

Output: 
17 
Explanation: 

The largest integer is 98. So the sum of the digits of 98 is 17 (9 + 8). Hence the output is 17 

Example Input/Output 2: 
Input: 
9 
401 884 8 203 123 950 475 520 193 

Output: 
14
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt(), t, max=-1;
		for(int i=0;i<n;i++){
		    t=sc.nextInt();
		    if(t>max)
		        max=t;
		}
		t=0;
		while(max>0){
		    t+=max%10;
		    max/=10;
		}
		System.out.print(t);
	}
}
