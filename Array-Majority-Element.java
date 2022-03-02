/*
The program must accept an integer array of size N as the input. The program must print the majority element in the given array as the output. The majority element is an integer
that appears more than N/2 times in an array. If there is no such integer, the program must print No Majority Element as the output.

Boundary Condition(s):
1 <= N <= 10^5
1 <= Each integer value <= 10^8

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains the majority element in the given array or No Majority Element.

Example Input/Output 1:
Input:
5
4 5 4 6 4

Output:
4

Explanation:
The integer 4 has occurred 3 times.
The integer 5 has occurred 1 time.
The integer 6 has occurred 1 time.
Here, the integer 4 has occurred more than 5/2 times.
Hence the output is 4

Example Input/Output 2:
Input:
8
10 20 10 5 10 10 5 10

Output:
10

Example Input/Output 3:
Input:
6
28 74 28 74 28 74

Output:
No Majority Element
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int N=sc.nextInt();
		boolean flag=false;
		HashMap<Integer,Integer> count=new HashMap<>();
		for(int ctr=0;ctr<N;ctr++) {
		    int num=sc.nextInt();
		    count.put(num,count.getOrDefault(num,0)+1);
		    if (count.get(num)>N/2) {
		        System.out.print(num);
		        flag=true;
		        break;
		    }
		}
		if (!flag) {
		    System.out.print("No Majority Element");
		}

	}
}
