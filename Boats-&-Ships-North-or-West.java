/*
The program must accept a character matrix of size R*C representing a port as the input. The character asterisk (*) represents water. 
The character hash symbol (#) represents a boat. Two consecutive hash symbols (vertically or horizontally) represent a ship. 
The vertical ships can move only towards the north. The horizontal ships can move only towards the west. The boats can move towards north or west. 
The boats and ships leave the port based on the following conditions.
- Every odd minute, the first occurring boat or the vertical ship in each column leave the port (towards north).
- Every even minute, the first occurring boat or the horizontal ship in each row leave the port (towards west).
- A boat or ship cannot move if there is another boat or ship on its way.
The program must print the number of minutes it takes to empty the port as the output.

Boundary Condition(s):
2 <= R, C <= 25

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C characters separated by a space.

Output Format:
The first line contains the number of minutes it takes to empty the port.

Example Input/Output 1:
Input:
7 6
# # * # # *
* * # * * #
# * # * # *
* * * * # *
# * # # * #
* # * * * *
* * * * # *

Output:
5

Explanation:
After 1 minute (1 vertical ship and 1 boat left the port), the port becomes
# # * # # *
* * * * * *
# * * * # *
* * * * # *
# * # # * #
* # * * * *
* * * * # *
After 2 minutes (1 horizontal ship and 4 boats left the port), the port becomes
* * * # # *
* * * * * *
* * * * # *
* * * * # *
* * # # * #
* * * * * *
* * * * * *
After 3 minutes (1 boat left the port), the port becomes
* * * # # *
* * * * * *
* * * * # *
* * * * # *
* * # # * *
* * * * * *
* * * * * *
After 4 minutes (2 horizontal ships left the port), the port becomes
* * * * * *
* * * * * *
* * * * # *
* * * * # *
* * * * * *
* * * * * *
* * * * * *
After 5 minutes (1 vertical ship left the port), the port becomes empty.
It takes 5 minutes to empty the port. So 5 is printed as the output.

Example Input/Output 2:
Input:
6 7
* * * # * # #
# # * * * * *
* * # * * # *
* # * # * # *
* # * # * * #
# * # * * # *

Output:
4
*/
import java.util.*;
public class Hello {
    static int R, C;
    public static boolean verticalShip(char mat[][], int row, int col) {
        return (row-1>=0 && mat[row-1][col]=='#') || (row+1<R && mat[row+1][col]=='#');
    }
    
    public static boolean horizontalShip(char mat[][], int row, int col) {
        return (col-1>=0 && mat[row][col-1]=='#') || (col+1<C && mat[row][col+1]=='#');
    }
    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		R = sc.nextInt();
		C = sc.nextInt();
		int hashCount = 0;
		char mat[][] = new char[R][C];
		for(int row=0;row<R;row++) {
		    for(int col=0;col<C;col++) {
		        mat[row][col]=sc.next().charAt(0);
		        if (mat[row][col]=='#')
		            hashCount++;
		    }
		}
		int minute=1;
		while(hashCount>0) {
		    if (minute%2!=0) {
		        for(int col=0;col<C;col++) {
		            for(int row=0;row<R;row++) {
		                if (mat[row][col]=='#') {
		                    if (!horizontalShip(mat,row,col)) {
		                        mat[row][col]='*';
		                        hashCount--;
		                        if (row+1<R && mat[row+1][col]=='#') {
		                            mat[row+1][col]='*';
		                            hashCount--;
		                        }
		                    }
		                    break;
		                }
		            }
		        }
		    }
		    else {
		        for(int row=0;row<R;row++) {
		            for(int col=0;col<C;col++) {
		                if (mat[row][col]=='#') {
		                    if (!verticalShip(mat,row,col)) {
		                        mat[row][col]='*';
		                        hashCount--;
		                        if (col+1<C && mat[row][col+1]=='#') {
		                            mat[row][col+1]='*';
		                            hashCount--;
		                        }
		                    }
		                    break;
		                }
		            }
		        }
		    }
		    minute++;
		}
		System.out.print(minute-1);
	}
}
