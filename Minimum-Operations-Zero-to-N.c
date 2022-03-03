/*
The program must accept an integer N as the input. The program must print the minimum number of operations required to reach N from 0. There are two types of operations which 
are given below.
- Double the integer
- Add one to the integer

Boundary Condition(s):
1 <= N <= 10^8

Input Format:
The first line contains N.

Output Format:
The first line contains the minimum number of operations required to reach N from 0.

Example Input/Output 1:
Input:
8

Output:
4

Explanation:
Here N = 8
1st operation = 0 + 1 = 1
2nd operation = 1 + 1 = 2
3rd operation = 2 * 2 = 4
4th operation = 4 * 2 = 8

Example Input/Output 2:
Input:
43

Output:
9
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int N, count=2;
    scanf("%d",&N);
    if (N<=2)
    {
        printf("%d",N);
        return;
    }
    while (N>2)
    {
        if(N%2==0)
        {
            N/=2;
        }
        else
        {
            N--;
        }
        count++;
    }
    printf("%d",count);

}
