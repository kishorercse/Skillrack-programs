/*

The program must accept a string S as the input. The program must print the smallest substring containing all the distinct characters of the string S in it.
Note: If more than one such substring is found, print the first occurring substring.

Boundary Condition(s):
1 <= Length of string S <= 100

Input Format:
The first line contains the value of S.

Output Format:
The first line contains the smallest substring with all the distinct characters of the string S.

Example Input/Output 1:
Input:
aabbcccdddd

Output:
abbcccd

Explanation:
Here the distinct characters are a, b, c and d.
The smallest substring with all the characters a, b, c and d is abbcccd.
Hence abbcccdis printed as the output.

Example Input/Output 2:
Input:
jsajdnskjd

Output:
ajdnsk
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		String s=new Scanner(System.in).next();
		int l=s.length(),dist=0;
		HashMap<Character,Integer> hm=new HashMap<>();
		for(int i=0;i<l;i++){
		    char ch=s.charAt(i);
		    hm.put(ch,hm.getOrDefault(ch,0)+1);
		    if (hm.get(ch)==1)
		        dist+=1;
		}
		hm.clear();
		int count=0,min=l,start=0,ind=0;
		for(int i=0;i<l;i++){
		    char ch=s.charAt(i);
		    hm.put(ch,hm.getOrDefault(ch,0)+1);
		    if (hm.get(ch)==1){
		        count+=1;
			if(count==dist){
				while(hm.get(s.charAt(start))>1){
				    hm.replace(s.charAt(start),hm.get(s.charAt(start))-1);
				    start+=1;
				}
				min=i-start+1;
				ind=start;
				break;
			}
		    }
		}
		System.out.print(s.substring(ind,ind+min));

	}
}
