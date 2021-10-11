/*
The program must accept two integers N and K as the input. The program must form a grid of asterisks of size N*N.
Then the program must replace the asterisks in the Kth border of the grid with the hash symbols(#). Finally, the
program must print N*N grid as the output.

Boundary Condition(s):
2 <= N <= 100
1 <= K <= (N+1)/2

Input Format:
The first line contains N and K separated by a space.

Output Format:
The first N lines, each contains N characters separated by a space. 

Example Input/Output 1:
Input: 
5 1

Output: 
# # # # # 
# * * * # 
# * * * # 
# * * * # 
# # # # # 

Explanation: 
Here N=5, so the 5*5 grid of asterisks is formed. 
The value of K is 1, so the 1st border is replaced with the hash symbols. 
Now the 5*5 grid becomes 
# # # # #
# * * * # 
# * * * # 
# * * * #
# # # # #

Example Input/Output 2:
Input:
6 3

Output: 
* * * * * *
* * * * * * 
* * # # * * 
* * # # * * 
* * * * * * 
* * * * * * 

Example Input/Output 3:
Input: 
7 2 

Output:
* * * * * * * 
* # # # # # * 
* # * * * # *
* # * * * # *
* # * * * # *
* # # # # # * 
* * * * * * *
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n=sc.nextInt(), k=sc.nextInt();
		for(int i=1;i<=n;i++){
		    for(int j=1;j<=n;j++){
		        if(((i==n-k+1 || i==k) && j>=k && j<=n-k+1) || ((j==k || j==n-k+1) && i>=k && i<=n-k+1))
		            System.out.print("# ");
		        else
		            System.out.print("* ");
		    }
		    System.out.println();
		}

	}
}
