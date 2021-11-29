/*
The program must accept two integer arrays of size M and N as the input. The program must print the elements of the first array interlaced with reversed second array elements 
as the output.

Boundary Condition(s):
1 <= M, N <= 100

Input Format:
The first line contains the value of M.
The second line contains M integers separated by space(s).
The third line contains the value of N.
The fourth line contains N integers separated by space(s).

Output Format:
The first line contains M+N integers of the first array and the second array separated by a space.

Example Input/Output 1:
Input:
5
51 48 35 79 12
8
70 34 84 98 31 23 64 85

Output:
51 85 48 64 35 23 79 31 12 98 84 34 70

Explanation:
The first array elements are 51 48 35 79 12
The reversed second array elements are 85 64 23 31 98 84 34 70
Hence the output is 51 85 48 64 35 23 79 31 12 98 84 34 70

Example Input/Output 2:
Input:
4
78 82 9 27
3
63 57 9

Output:
78 9 82 57 9 63 27
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int m,n;
    scanf("%d",&m);
    int arr1[m];
    for(int i=0;i<m;i++)
        scanf("%d",&arr1[i]);
    scanf("%d",&n);
    int arr2[n];
    for(int i=n-1;i>=0;i--)
        scanf("%d",&arr2[i]);
    int min=m>n?n:m;
    for(int i=0;i<min;i++)
        printf("%d %d ",arr1[i],arr2[i]);
    if (min==m)
        for(int i=min;i<n;i++)
            printf("%d ",arr2[i]);
    else
        for(int i=min;i<m;i++)
            printf("%d ",arr1[i]);

}
