/*
Given an integer N as the input, the program must print the pattern as mentioned in the Example Input/Output Section.

Boundary Condition(s):
1 <= N <= 50

Input Format:
The first line contains the value of N.

Output Format:
The list of lines contain the pattern as shown in the Example Input/Output Section.

Example Input/Output 1:
Input:
4

Output:
* * * * 0 * * * * 
* * * 0 1 0 * * * 
* * 0 1 2 1 0 * * 
* 0 1 2 3 2 1 0 * 
0 1 2 3 4 3 2 1 0 
* 0 1 2 3 2 1 0 * 
* * 0 1 2 1 0 * * 
* * * 0 1 0 * * * 
* * * * 0 * * * * 

Example Input/Output 2:
Input:
5

Output:
* * * * * 0 * * * * * 
* * * * 0 1 0 * * * * 
* * * 0 1 2 1 0 * * * 
* * 0 1 2 3 2 1 0 * * 
* 0 1 2 3 4 3 2 1 0 * 
0 1 2 3 4 5 4 3 2 1 0 
* 0 1 2 3 4 3 2 1 0 * 
* * 0 1 2 3 2 1 0 * * 
* * * 0 1 2 1 0 * * * 
* * * * 0 1 0 * * * * 
* * * * * 0 * * * * * 
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt(),t;
		String s,s2,arr[]=new String[n];
		for(int i=0;i<=n;i++){
		    s="";
		    s2="";
		    for(int j=0;j<n-i;j++){
		        System.out.print("* ");
		        s="* "+s;
		        s2+="* ";
		    }
		    for(int j=0;j<=i;j++){
		        System.out.print(j+" ");
		        s=j+" "+s;
		        s2+=j+" ";
		    }
		    t=Integer.toString(i).length()+1;
		    if (i<n)
		        arr[i]=s2+s.substring(t);
		    System.out.println(s.substring(t));
		}
		for(int i=n-1;i>=0;i--)
		    System.out.println(arr[i]);

	}
}
