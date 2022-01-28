/*
The program must accept an integer N as the input. The program must print the smallest factor and the largest factor of N. Then the program must print the second smallest factor
and the second largest factor of N. Similarly, the program must print the remaining factors of N as the output.

Boundary Condition(s):
2 <= N <= 10^5

Input Format:
The first line contains N.

Output Format:
The first line contains the integer values separated by a space.

Example Input/Output 1:
Input:
24

Output:
1 24 2 12 3 8 4 6

Example Input/Output 2:
Input:
121

Output:
1 121 11

Example Input/Output 3:
Input:
10

Output:
1 10 2 5
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n,i;
    scanf("%d",&n);
    for(i=1;i*i<n;i++)
    {
        if (n%i==0)
        {
            printf("%d %d ",i,n/i);
        }
    }
    if (n/i==i)
        printf("%d",i);

}
