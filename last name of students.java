/*
A String containing comma separated names of students (first name and last name) is passed as the input to the program. 
The program must print only the last name of each student in the given order as the output. 

Boundary Condition(s): 
1 <= Length of string <= 1000 

Input Format: 
The first line contains the string. 

Output Format: 
The first line contains the last name of students separated by a space.

Example Input/Output 1: 
Input: 
Ravi Sashtri,Mary Jane,Carl Johnson 
Output:
Sashtri Jane Johnson 

Example Input/Output 2: 
Input: 
Johnny Depp,David Guetta,Sachin Tendulkar,Melinda Gates 
Output: 
Depp Guetta Tendulkar Gates
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		String s=(new Scanner(System.in)).nextLine(), ans="";
		int l=s.length();
		boolean flag=false;
		for(int i=0;i<l;i++){
		    char ch=s.charAt(i);
		    if (ch==' '){
		        if (!ans.equals("")){
		            System.out.print(ans+" ");
		            ans="";
		        }
		        flag=true;
		    }
		    else if(ch==',')
		        flag=false;
		    else if (flag)
		        ans+=ch;
		}
		System.out.print(ans);

	}
}
