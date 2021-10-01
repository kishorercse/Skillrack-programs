/*
An array of N integers with non-zero values is passed as the input to the program. The program must print another array of size N 
where value at each index will be the product of all values in the input array except the value at that index in the input array. 

Input Format: 
The first line will contain N integers separated by a space.

Output Format:
The first line will contain N integers separated by a space.

Boundary Conditions: 
The length of the input containing N integers will be from 3 to 100.
The integer values will be from 1 to 100. 

Example Input/Output 1: 
Input: 
1 2 3 4 5 

Output: 
120 60 40 30 24

Example Input/Output 2: 
Input: 
10 5 4 

Output: 
20 40 50 

Example Input/Output 3: 
Input:
21 100 

Output: 
100 21
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int product=1,n=0;
		ArrayList<Integer> al = new ArrayList<Integer>();
		while (sc.hasNext()){
		    int t=sc.nextInt();
		    al.add(t);
		    product*=t;
		    n++;
		}
		for(int i=0;i<n;i++){
		    System.out.print(product/al.get(i)+" ");
		}

	}
}
