/*
The program must accept two integers N and M as the input. The program must print the desired pattern as shown in the Example Input/Output sections.

Boundary Condition(s):
1 <= N,M <= 100

Input Format:
The first line contains the values of N and M.

Output Format:
The first Mx2 lines contain the desired pattern as shown in the Example Input/Output sections.

Example Input/Output 1:
Input:
3 4

Output:
3
44
555
6666
6666
555
44
3

Example Input/Output 2:
Input:
2 5

Output:
2
33
444
5555
66666
66666
5555
444
33
2
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt(),m=sc.nextInt();
		ArrayList<String> al=new ArrayList<String>();
		for(int i=n;i<n+m;i++){
		    String t="";
		    for(int j=n;j<=i;j++){
		        System.out.print(i);
		        t+=i;
		    }
		    al.add(0,t);
		    System.out.println();
		}
		for(String t:al){
		    System.out.println(t);
		}
	}
}
