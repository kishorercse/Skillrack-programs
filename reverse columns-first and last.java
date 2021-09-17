/*
The program must accept an integer matrix of size RxC as the input. 
The program must reverse all the elements in the column if the first and the last elements of the column are same.
Then the program must print the modified matrix as the output. 

Boundary Condition(s): 
2 <= R, C <= 50 
-999 <= Each element of the matrix <= 999 

Input Format: 
The first line contains the value of R and C separated by a space. The next R lines contain each C elements separated by space(s). 

Output Format: 
The first R lines contain each C elements separated by a space.

Example Input/Output 1: 
Input: 
5 4 
11 7 5 19 
4 13 16 10 
9 9 13 0 
7 5 17 8 
11 8 5 12 

Output: 
11 7 5 19
7 13 17 10 
9 9 13 0 
4 5 16 8 
11 8 5 12 

Explanation: 
The elements in the first column are 11, 4, 9, 7 and 11. Here the first and the last elements are same. So reverse the elements in the first column. 
The elements in the third column are 5, 17, 13, 16 and 5. Here the first and the last elements are same. So reverse the elements in the third column. 
Hence the output is 
11 7 5 19 
7 13 17 10 
9 9 13 0 
4 5 16 8 
11 8 5 12 

Example Input/Output 2: 
Input: 
4 4 
49 81 22 92 
20 60 14 79 
57 39 20 73 
50 81 22 92 

Output: 
49 81 22 92 
20 39 20 73 
57 60 14 79 
50 81 22 92
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int r = sc.nextInt(), c = sc.nextInt();
		int m[][] = new int[r][c];
		for(int i=0;i<r;i++){
		    for(int j=0;j<c;j++){
		        m[i][j]=sc.nextInt();
		    }
		}
		for(int j=0;j<c;j++){
		    if (m[0][j]==m[r-1][j]){
		        int a=0,b=r-1;
		        while(a<b){
		            int t=m[a][j];
		            m[a][j]=m[b][j];
		            m[b][j]=t;
		            a++;
		            b--;
		        }
		    }
		}
		for(int i=0;i<r;i++){
		    for(int j=0;j<c;j++){
		        System.out.print(m[i][j]+" ");
		    }
		    System.out.println();
		}
		

	}
}
