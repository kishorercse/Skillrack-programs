/*
An odd length string S of length L is passed as the input. The program must print the string S as two diagonals as shown in the example Input/Output below. 

Input Format: 
The first line will contain S. 

Output Format: 
L lines will contain the pattern as shown in the example Input/Output below. 

Boundary Conditions: 
Length of S is from 3 to 51. 

Example Input/Output 1: 
Input: cry Output:
c y
 r
c y 

Example Input/Output 2: 
Input: 
tiger 

Output:
t   r
 i e
  g 
 i e 
t   r
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		String s=(new Scanner(System.in)).next();
		int l=s.length();
		for(int i=0;i<l;i++){
		    for(int j=0;j<l;j++){
		        if (j==i || j==l-i-1)
		            System.out.print(s.charAt(j));
		        else
		            System.out.print(" ");
		    }
		    System.out.println();
		}
	}
}
