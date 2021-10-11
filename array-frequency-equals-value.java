/*
The program must accept N integer values and print the values which are equal to the count of their occurrence (in ascending order). If there is no such value then the program must print -1.

Boundary Condition(s):
1 <= N <= 100
1 <= Each integer value <= 100

Input Format:
The first line contains N.
The second line contains the N integer values separated by a space.

Output Format:
The first line contains the integer values separated by a space.

Example Input/Output 1:
Input:
4
2 4 2 3

Output:
2

Example Input/Output 2:
Input:
11
2 1 4 3 4 3 4 5 3 4 6

Output:
1 3 4
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    int n=sc.nextInt();
	    TreeMap<Integer,Integer> tm=new TreeMap<>();
	    while (n>0){
	        int t=sc.nextInt();
	        tm.put(t,tm.getOrDefault(t,0)+1);
	        n-=1;
	    }
	    boolean flag=true;
	    for(Map.Entry a:tm.entrySet()){
	        if(a.getKey()==a.getValue()){
	            System.out.print(a.getKey()+" ");
	            flag=false;
	        }
	    }
	    if (flag)
	        System.out.print(-1);
	}
}
