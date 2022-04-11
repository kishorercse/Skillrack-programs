/*
A Bingo game is played with a 5x5 matrix board. When a person correctly guesses a number in the board it is slashed. When 5 rows or columns are entirely slashed it is
BINGO (As BINGO contains 5 letters).

Given the values for the 5*5 matrix board, followed by N numbers which are guesses by a person, find the number of guesses needed for a BINGO.

Input format:
First 5 lines each contain 5 numbers with the values for bingo game.
6th line contains N
7th line contains N numbers as guesses by the person separated by space.

Boundary Condition:
1 <= Number in a Bingo board <=50
1 <= Number Guessed <=50

Example Input/Output 1:
Input:
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
33
1 29 2 49 28 3 4 5 47 6 7 8 26 9 11 50 12 27 45 13 16 17 18 21 22 23 24 41 25 36 19 39 42

Output:
29

Explanation:
The guesses required to solve the bingo are
1 29 2 49 28 3 4 5 47 6 7 8 26 9 11 50 12 27 45 13 16 17 18 21 22 23 24 41 25
Last 4 guesses are not required as after 29 guesses the bingo is,
- - - -  -
- - - -  10
- - - 14 15
- - - 19 20
- - - -  -
Here 2 rows and 3 columns are slashed (that is a total of 5 rows or columns are completely slashed)
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int m[][]=new int[5][5];
		for(int i=0;i<5;i++) {
		    for(int j=0;j<5;j++) {
		        m[i][j]=sc.nextInt();
		    }
		}
		int n=sc.nextInt(), count=0, rowCount[]=new int[5], colCount[]=new int[5];
		for (int ctr=1;ctr<=n;ctr++) {
		    int t=sc.nextInt();
		    boolean found=false;
		    for(int i=0;i<5;i++) {
		        for(int j=0;j<5;j++) {
		            if (m[i][j]==t) {
		                m[i][j]=-1;
		                rowCount[i]++;
		                colCount[j]++;
		                if (rowCount[i]==5)
		                    count++;
		                if (colCount[j]==5)
		                    count++;
		                found=true;
		                break;
		            }
		        }
		        if (found)
		            break;
		    }
		    if (count>=5) {
		        System.out.print(ctr);
		        break;
		    }
		}

	}
}
