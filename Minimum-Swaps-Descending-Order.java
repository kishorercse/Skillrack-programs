/*
The program must accept N integers from 1 to N in any order as the input. The program must print the minimum number of swaps required to order those N integers in descending 
order as the output.

Boundary Condition(s):
1 <= N <= 1000

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains the minimum number of swaps required.

Example Input/Output 1:
Input:
5
4 5 1 3 2

Output:
3

Explanation:
The integers 5 and 4 can be swapped.
Now the integers become 5 4 1 3 2.
Then the integers 2 and 1 can be swapped.
Now the integers become 5 4 2 3 1.
Then the integers 2 and 3 can be swapped.
Now the integers become 5 4 3 2 1.
So at least 3 swaps are required.
Hence 3 is printed.

Example Input/Output 2:
Input:
7
2 7 6 3 5 4 1

Output:
5
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int N=sc.nextInt(), swaps=0;
		int arr[]=new int[N+1];
		for(int index=N;index>=1;index--) {
		    arr[index]=sc.nextInt();
		}
		boolean visited[]=new boolean[N+1];
		for(int index=1;index<=N;index++)
		{
		    if (visited[index]) {
		        continue;
		    }
		    if (arr[index]==index) {
		        visited[index]=true;
		        continue;
		    }
		    int edges=0, cycleIndex=index;
		    while(!visited[cycleIndex]) {
		        visited[cycleIndex]=true;
		        edges++;
		        cycleIndex=arr[cycleIndex];
		    }
		    swaps+=edges-1;
		}
		System.out.print(swaps);

	}
}
