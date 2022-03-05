/*
The program must accept the stock prices on N days as the input. A person can buy a stock on a particular day and he can sell it once on any other given day. He can not buy and
sell on the same day. The program must print the maximum possible profit P that can be obtained by buying and selling 1 stock once as the output.

Boundary Condition(s):
2 <= N <= 10^5
1 <= Each integer value <= 10^5

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains P.

Example Input/Output 1:
Input:
7
50 100 40 60 70 50 80

Output:
50

Explanation:
Here N = 7.
The stock price on the 1st day is 50 and the stock price on the 2nd day is 100.
On buying the stock on the 1st day and selling it on the 2nd day can earn the maximum profit 50 (100 - 50 = 50).
Hence the output is 50

Example Input/Output 2:
Input:
10
15 10 60 70 45 5 70 30 100 90

Output:
95
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int N=sc.nextInt(), prices[]=new int[N];
		for(int index=0;index<N;index++) {
		    prices[index]=sc.nextInt();
		}
		int maxProfit=0, minPrice=prices[0];
		for(int index=1;index<N;index++) {
		    if (prices[index]<minPrice)
		    {
		        minPrice=prices[index];
		    }
		    else if (prices[index]-minPrice>maxProfit)
		    {
		        maxProfit=prices[index]-minPrice;
		    }
		}
		System.out.print(maxProfit);

	}
}
