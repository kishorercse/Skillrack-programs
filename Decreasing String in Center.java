/*

A string S is passed as the input to the program. The program must print the pattern as shown in the Example Input/Output sections.
Note: The length of the string is always even.

Boundary Condition(s):
1 <= Length of the string <= 100

Input Format:
The first line contains the string S.

Output Format:
The lines contain the pattern as shown in the Example Input/Output sections.

Example Input/Output 1:
Input:
barber

Output:
barber
*baer*
**br**
******

Example Input/Output 2:
Input:
database

Output:
database
*datase*
**dase**
***de***
********
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		String s=(new Scanner(System.in)).next();
		int l=s.length()/2,a=l,b=l;
		for(int i=0;i<=l;i++){
		    for(int j=0;j<i;j++){
		        System.out.print("*");
		    }
		    System.out.print(s.substring(0,a));
		    System.out.print(s.substring(b));
		    for(int j=0;j<i;j++){
		        System.out.print("*");
		    }
		    System.out.println();
		    a-=1;
		    b+=1;
		}
	}
}
