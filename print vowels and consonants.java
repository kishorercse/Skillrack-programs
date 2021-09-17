/*
The program must accept a string value S as the input. The program must print the vowels in S and then print the consonants in S as the output. 

Boundary Condition(s): 
1 <= Length of S <= 100 

Input Format: 
The first line contains the values of string S. 

Output Format: 
The first line contains the vowels in S and the consonants in S. 

Example Input/Output 1: 
Input: 
Hello 

Output: 
eoHll 

Explanation: 
In Hello, the vowels are e and o. 
The consonants are H, l and l. 
Hence the output is eoHll 

Example Input/Output 2: 
Input: 
EncycLopediA 

Output: 
EoeiAncycLpd
*/
import java.util.*;
public class Hello {
    
    public static boolean isVowel(char ch){
        ch=Character.toLowerCase(ch);
        return ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u';
    }

    public static void main(String[] args) {
		String s=(new Scanner(System.in)).next(), consonants="";
		int l=s.length();
		for(int i=0;i<l;i++){
		    if (isVowel(s.charAt(i)))
		        System.out.print(s.charAt(i));
		    else
		        consonants+=s.charAt(i);
		}
		System.out.print(consonants);
	}
}
