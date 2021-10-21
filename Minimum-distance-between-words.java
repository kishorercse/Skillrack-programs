/*
A string S is passed as the input. Two words W1 and W2 which are present in the string S are also passed as the input. The program must find the minimum distance D between W1
and W2 in S (in forward or reverse order) and print D as the output. Input Format: The first line will contain S. The second line will contain W1. The third line will contain 
W2. Output Format: The first line will contain D - the minimum distance between W1 and W2 in S. 

Boundary Conditions: 
Length of S is from 5 to 200. 

Example Input/Output 1: 
Input: 
the brown quick frog quick the 
the 
quick 

Output: 
1 

Explanation: 
quick and the are adjacent as the last two words. Hence distance between them is 1.

Example Input/Output 2: 
Input: 
the quick the brown quick brown the frog 
quick 
frog 

Output: 
3
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		String arr[]=sc.nextLine().split(" "), a=sc.next(), b=sc.next();
		int prev=-1,l=arr.length,min=l;
		for(int i=0;i<l;i++){
		    if (arr[i].equals(a) || arr[i].equals(b)){
		        prev=i;
		        break;
		    }
		}
		for(int i=prev+1;i<l;i++){
		    if (arr[i].equals(a) || arr[i].equals(b)){
		        if ((a.equals(b) || !arr[i].equals(arr[prev])) && i-prev<min)
		            min=i-prev;
		        prev=i;
		    }
		}
		System.out.print(min);

	}
}
