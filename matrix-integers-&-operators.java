/*
The program must accept a matrix of size R*C containing integers and operators(+ and -) as the input. For each
occurence of plus(+) in the matrix, the program must replace the operator with the sum of integers on the top
and bottom of the operator. Similarly, for each occurence of minus(-) in the matrix, the program must replace
the operator with the absolute difference between the integers on the top and bottom of the operator. Finally,
the program must print the revised matrix as the output.

Note:
- There will be no consecutive operators in each column of the matrix.
- There will be no operators on the top and bottom edges of the matrix.

Boundary Condition(s):
3 <= R, C <= 25
1 <= Matrix element value <= 10^5

Input Format:
The first line contains R and C.
The next R lines contain the matrix.

Output Format:
The first R line, each contains C integers separated by a space representing the revised matrix.

Example Input/Output 1:
Input:
4 3
10 30 60
+ - 70
20 95 +
25 50 10

Output:
10 30 60
30 65 70
20 95 80
25 50 10
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int r = sc.nextInt(), c = sc.nextInt();
		String m[][] = new String[r][c];
		for(int i=0;i<r;i++){
		    for(int j=0;j<c;j++){
		        m[i][j]=sc.next();
		    }
		}
		for(int i=0;i<r;i++){ 
		    for(int j=0;j<c;j++){
		        if (m[i][j].equals("+"))
		            System.out.print(Integer.parseInt(m[i-1][j])+Integer.parseInt(m[i+1][j])+" ");
		        else if (m[i][j].equals("-"))
		            System.out.print(Math.abs(Integer.parseInt(m[i-1][j])-Integer.parseInt(m[i+1][j]))+" ");
		        else
		            System.out.print(m[i][j]+" ");
		    }
		System.out.println();
		}
	}
}
