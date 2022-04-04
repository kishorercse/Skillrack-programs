/*
The program must accept a matrix of size R*C containing integers and alphabets as the input. For each occurrence of the alphabet in the matrix, the program must
append the alphabet to the surrounding integers of the alphabet. Then the program must print the revised matrix as the output.
Note: In the given matrix, there are no common integers around two or more alphabets.

Boundary Condition(s):
2 <= R, C <= 50
1 <= Each integer value in the matrix <= 1000

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C elements of the matrix separated by a space.

Output Format:
The first R lines contain the revised matrix.

Example Input/Output 1:
Input:
4 5
5 2 2 2 4
7 5 2 3 b
8 a 5 5 9
9 3 8 5 6

Output:
5 2 2 2b 4b
7a 5a 2a 3b b
8a a 5a 5b 9b
9a 3a 8a 5 6

Explanation:
Here R=4 and C=5.
The alphabets in the given matrix are highlighted below
5 2 2 2 4
7 5 2 3 b
8 a 5 5 9
9 3 8 5 6
After modifying the matrix based on the given conditions, the matrix becomes
5 2 2 2b 4b
7a 5a 2a 3b b
8a a 5a 5b 9b
9a 3a 8a 5 6

Example Input/Output 2:
Input:
5 5
86 77 45 57 82
13 A 10 86 70
32 74 72 27 C
28 79 12 43 90
15 B 13 15 37

Output:
86A 77A 45A 57 82
13A A 10A 86C 70C
32A 74A 72A 27C C
28B 79B 12B 43C 90C
15B B 13B 15 37
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int R = sc.nextInt(), C=sc.nextInt();
		String mat[][] = new String[R][C];
		for(int row=0;row<R;row++) {
		    for(int col=0;col<C;col++) {
		        mat[row][col]=sc.next();
		    }
		}
		int diff[][]=new int[][]{{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
		for(int row=0;row<R;row++) {
		    for(int col=0;col<C;col++) {
		        if (Character.isLetter(mat[row][col].charAt(0))) {
		            for(int index=0;index<8;index++) {
		                int x=row+diff[index][0], y=col+diff[index][1];
		                if (x>=0 && x<R && y>=0 && y<C) {
		                    mat[x][y]+=mat[row][col];
		                }
		            }
		        }
		    }
		}
		for(int row=0;row<R;row++) {
		    for(int col=0;col<C;col++) {
		        System.out.print(mat[row][col]+" ");
		    }
		    System.out.println();
		}

	}
}
