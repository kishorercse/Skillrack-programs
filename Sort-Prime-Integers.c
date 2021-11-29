/*
The program must accept an integer array of size N as the input. The program must print all the prime integers in the array sorted in ascending order as the output. If there 
is no prime integer in the array then the program must print -1 as the output. 

Boundary Condition(s):
2 <= N <= 100
1 <= Array Element Value <= 100000

Input Format:
The first line contains the value of N.
The second line contains N integers separated by space(s).

Output Format:
The first line contains either the prime integers in the array sorted in ascending order separated by space(s) or -1.

Example Input/Output 1:
Input:
10
4 53 23 44 11 66 33 112 93 32

Output:
11 23 53

Explanation:
The prime integers in the array are 53, 23 and 11. 
The prime integers are sorted in ascending order as 11, 23 and 53.
Hence the output is 11 23 53.

Example Input/Output 2:
Input:
8
4 15 12 42 111 24 76 98 

Output:
-1
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
    int arr[n],ind=0;
    for(int i=0;i<n;i++)
    {
        int t;
        scanf("%d",&t);
        if (isprime(t))
            arr[ind++]=t;
    }
    if (ind==0)
        printf("-1");
    for(int i=0;i<ind;i++)
    {
        for(int j=i+1;j<ind;j++)
        {
            if (arr[i]>arr[j])
            {
                int t=arr[i];
                arr[i]=arr[j];
                arr[j]=t;
            }
        }
        printf("%d ",arr[i]);
    }
    
}
