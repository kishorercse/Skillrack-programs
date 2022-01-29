/*
The program must accept N integers and an integer K as the input. The program must shift the N integers to the left by K positions. Then the program must print the sum of every
three integers among the N modified integers. If there are no three integers to find the sum, then print the sum of the existing integers.

Boundary Condition(s):
1 <= K < N <= 100
1 <= Each integer value <= 1000

Input Format:
The first line contains N.
The second line contains N integers separated by a space.
The third line contains K.

Output Format:
The first line contains the integer value(s) separated by a space.

Example Input/Output 1:
Input:
5
2 3 4 7 1
2

Output:
12 5

Example Input/Output 2:
Input:
6
4 12 8 16 7 13
5

Output:
29 31

Example Input/Output 3:
Input:
10
2 41 79 40 13 57 66 65 67 62
4

Output:
136 194 122 40
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n,k,sum=0;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++)
        scanf("%d",&arr[i]);
    scanf("%d",&k);
    k%=n;
    int i=k;
    for(int ctr=1;ctr<=n;ctr++)
    {
        sum+=arr[i];
        i=(i+1)%n;
        if (ctr%3==0)
        {
            printf("%d ",sum);
            sum=0;
        }
    }
    if (n%3!=0)
        printf("%d",sum);

}
