/*
A boy has X rupees and he wants to buy some stickers. The price of a sticker is Y rupees. The values of X and Y are passed as the input. The program must print the maximum number 
of stickers he can buy and the amount left in his hand after purchase as the output. If it is not possible to buy at least one sticker, then the program must print -1 as the 
output. 

Boundary Condition(s):
1 <= X, Y <= 1000 

Input Format: 
The first line contains X and Y separated by a space. 

Output Format:
The first line contains two integer values separated by a space or -1.

Example Input/Output 1: 
Input: 
100 30 

Output:
3 10 

Explanation:
The boy has 100 rupees.
The price of a sticker is 30 rupees. 
He can buy a maximum of 3 stickers (3 * 30 = 90).
The amount remaining in his hand is 10 rupees. 
Hence the output is 3 10 

Example Input/Output 2:
Input:
50 25

Output: 
2 0 

Example Input/Output 3:
Input:
60 75 

Output: 
-1
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int x=sc.nextInt(), y=sc.nextInt();
		if (y>x)
		    System.out.print(-1);
		else {
		    System.out.print(x/y +" "+ x%y);
		}

	}
}
