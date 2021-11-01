/*
The program must accept an integer M representing the marks scored by a student. The program must print the color grade based on the following conditions. 
- If M is greater than 80, then the program must print the string value "Green". 
- If M is greater than 60 and less than or equal to 80, then the program must print the string value "Yellow". 
- If M is greater than 30 and less than or equal to 60, then the program must print the string value "Orange". 
- If M is less than or equal to 30, then the program must print the string value "Red". 

Boundary Condition(s): 
0 <= M <= 100 

Input Format: 
The first line contains M. 

Output Format: 
The first line contains a string representing the color grade for the student. 

Example Input/Output 1: 
Input:
85 

Output: 
Green 

Example Input/Output 2:
Input:
77 

Output:
Yellow

Example Input/Output 3:
Input:
54

Output:
Orange 

Example Input/Output 4:
Input:
25 

Output:
Red
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		int marks=(new Scanner(System.in)).nextInt();
		if (marks>80)
		    System.out.print("Green");
		else if(marks>60)
		    System.out.print("Yellow");
		else if(marks>30)
		    System.out.print("Orange");
		else
		    System.out.print("Red");

	}
}
