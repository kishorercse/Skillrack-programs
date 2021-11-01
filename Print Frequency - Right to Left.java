/*
The program must accept a string S as the input. The program must find the frequency of the characters in the given string in reverse order. Then the program must print each 4
character and its frequency till that character from the right. 

Boundary Condition(s)
1 <= Length of S <= 1000 

Input Format:
The first line contains S.

Output Format: 
The first line contains the character-integer pairs representing the characters of the string S and their frequencies from the right. 

Example Input/Output 1: 
Input:
google 

Output: 
g2 o2 o1 g1 l1 e1 

Explanation: 
Here the given string is google. 
1st character g -> 2nd occurrence from the right. So g2 is printed. 
2nd character o -> 2nd occurrence from the right. So g2 is printed. 
3rd character o -> 1st occurrence from the right. So o1 is printed. 
4th character g -> 1st occurrence from the right. So g1 is printed. 
5th character l -> 1st occurrence from the right. So l1 is printed. 
6th character e -> 1st occurrence from the right. So e1 is printed. 

Example Input/Output 2: 
Input: 
hippopotamus 

Output: 
h1 i1 p3 p2 o2 p1 o1 t1 a1 m1 u1 s1
*/
import java.util.*;
public class Hello {
    static Map<Character,Integer> hm=new HashMap<>();
    public static void Counter(String s, int index){
        if (index==-1)
            return;
        char ch=s.charAt(index);
        hm.put(ch,hm.getOrDefault(ch,0)+1);
        int t=hm.get(ch);
        Counter(s,index-1);
        System.out.print(""+ch+t+" ");
    }
    
    public static void main(String[] args) {
		  String s=new Scanner(System.in).next();
		  Counter(s,s.length()-1);

	}
}
