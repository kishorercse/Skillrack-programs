/*
Given a string S, the program must print the count of sub palindromes (with a minimum length of two characters) in the string S.

Boundary Conditions: 
Length of the string is between 2 and 200. 

Input Format: 
First line will contain the string value S. 

Output Format: 
First line will contain the integer which represents the count of sub palindromes in the string S. 

Sample Input/Output: 
Example 1: 
Input: 
everest 

Output: 
2 
Explanation: 
The sub palindromes are eve, ere

Example 2: 
Input: 
abccbaab 

Output: 
5 

Explanation: 
The sub palindromes are cc, bccb, aa, baab, abccba
*/
import java.util.*;
public class Hello {
    
    public static int isPalindrome(String s, int len){
        int i=0;
        len-=1;
        while(i<len){
            if (s.charAt(i)!=s.charAt(len))
                return 0;
            i++;
            len--;
        }
        return 1;
    }

    public static void main(String[] args) {
		String s=(new Scanner(System.in)).next();
		int len=s.length(), count=0;
		for(int i=0;i<len;i++){
		    for(int j=i+2;j<=len;j++){
		        count+=isPalindrome(s.substring(i,j),j-i);
		    }
		}
		System.out.print(count);

	}
}
