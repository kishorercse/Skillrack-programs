/*
The program must accept an integer N as the input. The program must print the cumulative sum of the first N prime integers as the output.

Boundary Condition(s):
1 <= N <= 100 

Example Input/Output 1:
Input:
5

Output: 
2 5 10 17 28 

Example Input/Output 2:
Input: 
8

Output:
2 5 10 17 28 41 58 77
*/
#include<stdio.h>
#include<stdlib.h>

int isprime(int n)
{
    if (n<=1)
        return 0;
    if (n<=3)
        return 1;
    if (n%2==0 || n%3==0)
        return 0;
    int i=5;
    while (i*i<=n)
    {
        if (n%i==0 || n%(i+2)==0)
            return 0;
        i+=6;
    }
    return 1;
}
int main()
{
    int n;
    scanf("%d",&n);
    int sum=2, start=3;
    printf("%d ",sum);
    while(n>1)
    {
        if (isprime(start))
        {
            sum+=start;
            printf("%d ",sum);
            n-=1;
        }
        start+=2;
    }

}
