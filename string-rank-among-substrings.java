/*
A string S is passed as the input. The program must generate the set (all unique) of all the substrings of S and then sort that set lexicographically. Now the program must print the rank of the string S in the new set formed.

Note:
– String S contains only lowercase English letters.
– Time complexity matters, optimize your algorithm

Boundary Condition(s):
1 <= Length of S <= 100

Input Format:
The first line contains S.

Output Format:
The first line contains the integer value denoting the rank.

Example Input/Output 1:
Input:
eren

Output:
5

Explanation:
Lexicograhically sorted set of unique substrings of S is
e
en
er
ere
eren
n
r
re
ren

In this eren appears in the 5th position.
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
        String s=(new Scanner(System.in)).next();
        TreeSet<String> ts=new TreeSet<>();
		int l=s.length();
		for(int i=0;i<l;i++){
		    for(int j=i+1;j<=l;j++){
		        ts.add(s.substring(i,j));
		    }
		}
		Iterator<String> it=ts.iterator();
		String curr=null;
		int index=0;
		while(it.hasNext()){
		    curr=it.next();
		    index+=1;
		    if (curr.equals(s)){
		        System.out.print(index);
		        break;
		    }
		}
	}
}
