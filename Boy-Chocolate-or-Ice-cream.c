/*
A boy can have either a chocolate(C) or an ice-cream(I) on a given day. But to avoid catching cold, his mom has prevented him from having ice-cream on consecutive days. The 
program must print the number of ways W in which the boy can have chocolate or ice-cream over the period of N days.

Boundary Condition(s):
1 <= N <= 80

Input Format:
The first line contains N.

Output Format:
The first line contains W.

Example Input/Output 1:
Input:
3

Output:
5

Explanation:
The 5 ways to have over three days are
C C C
C C I
C I C
I C C
I C I

Example Input/Output 2:
Input:
5

Output:
13


*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    long long int ch=1, ice=1, temp;
    int n;
    scanf("%d",&n);
    for(int i=2;i<=n;i++)
    {
        temp=ch;
        ch=ch+ice;
        ice=temp;
    }
    printf("%lld",ice+ch);

}
