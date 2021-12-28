/*
The program must accept a string S containing only alphabets as the input. The string S always starts with a consonant. The program must print the string like a line chart as
shown in the Example Input/Output section. The line in the chart always increases till the 1st vowel. Then the line decreases till the 2nd vowel. Then the line increases till
the 3rd vowel. Then the line decreases till the 4th vowel, and so on. The empty spaces before each character must be printed as hyphens.

Boundary Condition(s):
2 <= Length of S <= 100

Input Format:
The first line contains S.

Output Format:
The lines contain the string like a line chart as shown in the Example Input/Output section.

Example Input/Output 1:
Input:
skillrack

Output:
--i
-k-l
s---l---k
-----r-c
------a

Explanation:
Here S = "skillrack".
The first occuring vowel is 'i', so the characters till 'i' are printed in increasing order.
The second occuring vowel is 'a', so the characters till 'a' are printed in decreasing order.
No more vowels left in the given string, so the remaining characters are printed in increasing order.

Example Input/Output 2:
Input:
pineapple

Output:
-i
p-n-a
---e-p
------p
-------l
--------e

Example Input/Output 3:
Input:
NOTEBOOKS
Output:
--------S
-O---O-K
N-T-B-O
---E
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        char[] s=sc.next().toCharArray();
        ArrayList<String> al=new ArrayList<>();
        int r=0, i=0, c=0, d=-1;
        for(char ch:s)
        {
            if (i==r)
            {
                al.add("-".repeat(c)+ch);
                r++;
            }
            else if(i==-1)
            {
                al.add(0,"-".repeat(c)+ch);
                i=0;
                r++;
            }
            else
                al.set(i,al.get(i)+"-".repeat(c-al.get(i).length())+ch);
            if ("AEIOUaeiou".contains(""+ch))
                d*=-1;
            i+=d;
            c++;
        }
        for(String t:al)
            System.out.println(t);

	}
}
