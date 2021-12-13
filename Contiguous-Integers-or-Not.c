/*
The program must accept an integer array of size N as the input. The program must print YES if all the integers in the array can be used to form a contiguous set of integers 
(duplicates allowed) as the output. Else the program must print NO as the output. 

Boundary Condition(s):
2 <= N <= 100
1 <= Array Element Value <= 100000

Input Format:
The first line contains the value of N.
The second line contains N integers separated by space(s).

Output Format:
The first line contains either YES or NO. 

Example Input/Output 1:
Input:
8
5 2 3 6 4 4 6 6

Output:
YES

Explanation:
The integers 5, 2, 3, 6, 4, 4, 6 and 6 are used to form a contiguous set of integers 2, 3, 4, 4, 5, 6, 6 and 6
Hence the output YES is printed.

Example Input/Output 2:
Input:
5
10 14 12 13 13
 
Output:
NO
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++)
        scanf("%d",&arr[i]);
    for(int i=0;i<n-1;i++)
    {
        for(int j=0;j<n-i-1;j++)
        {
            if (arr[j]>arr[j+1])
            {
                int t=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=t;
            }
        }
    }
    for(int i=1;i<n;i++)
    {
        if (arr[i]-arr[i-1]>=2)
        {
            printf("NO");
            return;
        }
    }
    printf("YES");

}
