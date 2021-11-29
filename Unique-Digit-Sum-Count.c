/*
The program must accept an integer array of size N as the input. The program must print the count of integers after removing duplicate integers based on the digit sum of each
integer as the output. That is if two integers have the same digit sum then it is a duplicate.

Boundary Condition(s):
2 <= N <= 10^6
1 <= Array Element Value <= 10^16

Input Format:
The first line contains the value of N.
The second line contains N integers separated by space(s).

Output Format:
The first line contains the count of integers after removing duplicate integers based on the digit sum of each integer.

Example Input/Output 1:
Input:
6
93 73 84 86 38 55 

Output:
4

Explanation:
The digit sum of 93 is 12
The digit sum of 73 is 10
The digit sum of 84 is 12
The digit sum of 86 is 14
The digit sum of 38 is 11
The digit sum of 55 is 10
Here there are two duplicate integers 84 and 55. After removing these 2 integers in the array the count of integers in the array will become 4.
Hence the count 4 is printed as the output.

Example Input/Output 2:
Input:
8
4 15 13 42 112 24 76 94 
 
Output:
3
*/
#include<stdio.h>
#include<stdlib.h>

int digitSum(unsigned long long int n)
{
    int sum=0;
    while (n>0)
    {
        sum+=n%10;
        n/=10;
    }
    return sum;
}

int main()
{
    int n,sum[136],count=0;
    scanf("%d",&n);
    unsigned long long int arr[n];
    for(int i=0;i<n;i++)
    {
        scanf("%llu",&arr[i]);
        arr[i]=digitSum(arr[i]);
        sum[arr[i]]=1;
    }
    for(int i=0;i<n;i++)
    {
        if (sum[arr[i]]==1)
        {
            sum[arr[i]]=0;
            count++;
        }
    }
    printf("%d",count);
    
}
