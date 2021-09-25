/*
The program must accept a string S and a binary string B. The length of both S and B are smae. Where ever 1 occurs in B,
if the character is not an alphabet then delete the character. Else toggle the case of the alphabet. The program must print
the revised string value.

Boundary Condition(s):
1 <= Length of S, B <=1000

Input Format:
The first line contains S.
The second line contains B.

Output Format: 
The first line contains the revised string value. 

Example Input/Output 1: 
Input:
a1bcD2e3 
01101001 

Output: 
aBcd2e 

Explanation: 
Here S=a1bcD2e3, B=01101001. 
The positions where 1 occurs in the string 01101001 are 2, 3, 5 and 8. 
The character at the 2nd position of the string a1bcD2e3 is 1. So 1 is deleted. 
The character at the 3rd position of the string a1bcD2e3 is b. So it is toggled to upper case. 
The character at the 5th position of the string a1bcD2e3 is D. So it is toggled to lower case. 
The character at the 8th position of the string a1bcD2e3 is 3. So 3 is deleted. 
Now the string becomes aBcd2e. 

Example Input/Output 2:
Input: 
12Ab5c4P9qR8S0t 
111001010111011 

Output: 
ab5C4p9QrST
*/
import java.util.*;
public class Hello {
    
    public static char toggle(char ch){
        if (Character.isLowerCase(ch))
            return Character.toUpperCase(ch);
        else
            return Character.toLowerCase(ch);
    }
    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder s=new StringBuilder(sc.next());
		String b=sc.next();
		int l=s.length(), removed=0;;
		for(int i=0;i<l;i++){
		    if (b.charAt(i)=='1'){
    		    if (!Character.isAlphabetic(s.charAt(i-removed))){
    		        s.deleteCharAt(i-removed);
    		        removed+=1;
    		    }
    		    else
    		        s.setCharAt(i-removed,toggle(s.charAt(i-removed)));
		    }
		}
		System.out.print(s);

	}
}
