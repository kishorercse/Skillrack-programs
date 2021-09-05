/*
The program must accept two integer arrays of sizes M and N as the input. The program must print all the uncommon integer(s) (ascending order) in the given two arrays. If there is no uncommon integer in the given two arrays then the program must print -1 as the output.

Boundary Condition(s):
1 <= M, N <= 10000

Input Format:
The first line contains the values of M and N separated by a space.
The second line contains M integers separated by space(s).
The third line contains N integers separated by space(s).

Output Format:
The first line contains either all the uncommon integer(s) separated by space(s) or -1.

Example Input/Output 1:
Input:
5 5
87 5 6 12 91
5 1 7 87 8

Output:
1 6 7 8 12 91

Explanation:
The uncommon integers in the first array are 6 12 91
The uncommon integers in the second array are 1 7 8
The uncommon integers from both the arrays are combined and sorted in ascending order.
Hence the output is 1 6 7 8 12 91

Example Input/Output 2:
Input:
10 6
37 79 94 50 92 7 6 23 98 6
6 7 57 85 55 78

Output:
23 37 50 55 57 78 79 85 92 94 98

Explanation:
The uncommon integers in the first array are 37 79 94 50 92 23 98
The uncommon integers in the second array are 57 85 55 78
The uncommon integers from both the arrays are combined and sorted in ascending order.
Hence the output is 23 37 50 55 57 78 79 85 92 94 98
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int m=sc.nextInt(),n=sc.nextInt(),t;
		TreeMap<Integer,Integer> tm=new TreeMap<>();
		for(int i=0;i<m;i++){
		    t=sc.nextInt();
		    tm.put(t,1);
		}
		for(int i=0;i<n;i++){
		    t=sc.nextInt();
		    Integer p=tm.get(t);
		    if (p==null)
		        tm.put(t,-1);
		    else if(p==1)
		        tm.replace(t,2);
		}
	    boolean flag=true;
		for(Map.Entry i:tm.entrySet()){
		    if ((int)i.getValue()!=2){
		        System.out.print(i.getKey()+" ");
		        flag=false;
		    }
		}
		if (flag)
	        System.out.print(-1);

	}
}
