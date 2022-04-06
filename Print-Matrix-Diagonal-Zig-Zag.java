/*
An R*C matrix is passed as the input to the program. The program must print the values in zig-zag order diagonally. 
(Please refer Example Input/Output section for more details).

Input Format:
The first line contains R and C separated by a space.
Next R lines contain C values separated by a space.

Output Format:
The first line contains all R*C elements in zig-zag order diagonally, with the elements separated by a space.

Boundary Conditions:
2 <= R, C <= 100

Example Input/Output 1:
Input:
3 3
1 2 3
4 5 6
7 8 9

Output:
1 2 4 7 5 3 6 8 9

Example Input/Output 2:
Input:
3 7
1 2 3 4 5 6 7
8 9 1 2 3 4 5
6 7 8 9 1 2 3

Output:
1 2 8 6 9 3 4 1 7 8 2 5 6 3 9 1 4 7 5 2 3
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int R=sc.nextInt(), C=sc.nextInt(), mat[][]=new int[R][C];
		for(int i=0;i<R;i++) {
		    for(int j=0;j<C;j++) {
		        mat[i][j]=sc.nextInt();
		    }
		}
		boolean flag=true;
		for(int j=0;j<C;j++) {
		    int a=0, b=j, rowDiff=1, colDiff=-1;
		    if (flag) {
		        rowDiff=-1;
		        colDiff=1;
		        int min=Math.min(j,R-1);
		        a+=min;
		        b-=min;
		    }
	        while(a>=0 && a<R && b>=0 && b<C) {
	            System.out.print(mat[a][b]+" ");
	            a+=rowDiff;
	            b+=colDiff;
	        }
		    flag=!flag;
		}
		for(int i=1;i<R;i++) {
		    int a=i, b=C-1, rowDiff=1, colDiff=-1;
		    if (flag) {
		        rowDiff=-1;
		        colDiff=1;
		        int min=Math.min(C-1,R-i-1);
		        a+=min;
		        b-=min;
		    }
		    while(a>=0 && a<R && b>=0 && b<C) {
		        System.out.print(mat[a][b]+" ");
		        a+=rowDiff;
		        b+=colDiff;
		    }
		    flag=!flag;
		}
		

	}
}
