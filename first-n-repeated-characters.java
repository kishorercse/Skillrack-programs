/*
The program must accept a string S and then print all the characters which are among the first N repeated characters in S. 

Boundary Condition(s): 
1 <= Length of S <= 1000
1 <= N <= 100

Input Format: 
The first line contains S.
The second line contains N. 

Output Format:
The first line contains the string output.

Example Input/Output 1: 
Input:
abcdeabecdacdbe
4

Output: 
abceabecacbe 

Explanation: 
Though all characters a, b, c, d, e are repeated thrice, the first four repeated characters are a b c e.

Example Input/Output 2: 
Input:
officialwork 
2

Output: 
ffii
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
	Scanner sc=new Scanner(System.in);
	String s=sc.next();
	int n=sc.nextInt(), l=s.length();
	HashMap<Character, Integer> hm = new HashMap<>();
	for (int i=0;i<l;i++){
	    hm.put(s.charAt(i),hm.getOrDefault(s.charAt(i),0)+1);
	    if (hm.get(s.charAt(i))==2){
		n-=1;
		if (n==0)
		    break;
	    }
	}
	for(int i=0;i<l;i++){
	    if (hm.getOrDefault(s.charAt(i),0)>=2)
		System.out.print(s.charAt(i));
	}
   }
}
