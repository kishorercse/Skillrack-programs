/*
The program must accept a string S containing only lower case alphabets as the input. The program must encrypt the given string based on the following conditions.
- For each alphabet CH in the string S, the program must modify the alphabet based on a shift value.
- The value of the shift is determined by the count of occurrences of CH before the position of CH in the original string S.
- If the modified value of the alphabet goes beyond 'z', the shift wraps around to the beginning (i.e., If the alphabet is 'z' and the shift value is 2, then the 
modified value is 'b').
Finally, the program must print the encrypted string as the output.

Boundary Condition(s):
2 <= Length of S <= 1000

Input Format:
The first line contains S.

Output Format:
The first line contains the encrypted string.

Example Input/Output 1:
Input:
currentaffairs

Output:
cursentafgbits

Explanation:
Here S = currentaffairs.
c -> c (no characters before c)
u -> u (u does not occur before u)
r -> r (r does not occur before r)
r -> s (only one r occurs before r)
e -> e (e does not occur before e)
n -> n (n does not occur before n)
t -> t (t does not occur before t)
a -> a (a does not occur before a)
f -> f (f does not occur before f)
f -> g (only one f occurs before f)
a -> b (only one a occurs before a)
i -> i (i does not occur before i)
r -> t (two r's occur before r)
s -> s (s does not occur before s)

Example Input/Output 2:
Input:
abyzabyzabyz

Output:
abyzbczacdab
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		String s = (new Scanner(System.in)).next();
		int len = s.length();
		Map<Character, Integer> map = new HashMap<>();
		for(int i=0;i<len;i++) {
		    char ch = s.charAt(i);
		    int val = map.getOrDefault(ch,0);
		    int t = ((ch-96)+val)%26;
		    if (t==0)
		        t=26;
		    System.out.print((char)(96+t));
		    map.put(ch,val+1);
		}

	}
}
