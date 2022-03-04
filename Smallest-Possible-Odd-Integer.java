/*
The program must accept an integer N as the input. The program must print the smallest possible odd integer using all the digits in N as the output. If it is not possible to 
form such an integer, the program must print no as the output.

Boundary Condition(s):
10 <= N <= 10^17

Input Format:
The first line contains N.

Output Format:
The first line contains the smallest possible odd integer using all the digits in N or no.

Example Input/Output 1:
Input:
1670078423

Output:
1002346787

Explanation:
The smallest possible odd integer using all the digits in 1670078423 is 1002346787.

Example Input/Output 2:
Input:
40068

Output:
no
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		long N=sc.nextLong();
		int count[]=new int[10], unit=-1;
		while(N>0) {
		    count[(int)(N%10)]++;
		    N/=10;
		}
        for(int digit=9;digit>=1;digit-=2) {
            if (count[digit]>0) {
                unit=digit;
                count[digit]--;
                break;
            }
        }
        if (unit==-1) {
            System.out.print("no");
            return;
        }
        boolean nonZero=false;
        for(int digit=1;digit<=9;digit++) {
            if (count[digit]>0) {
                System.out.print(digit);
                count[digit]--;
                nonZero=true;
                break;
            }
        }
        if (nonZero) {
            while(count[0]>0) {
                System.out.print(0);
                count[0]--;
            }
        }
        for(int digit=1;digit<=9;digit++) {
            while(count[digit]>0) {
                System.out.print(digit);
                count[digit]--;
            }
        }
        System.out.print(unit);
	}
}
