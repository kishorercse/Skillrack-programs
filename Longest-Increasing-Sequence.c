/*
The program must accept N integers as the input. The program must print the longest contiguous increasing sequence (with difference as 1) in the given N integers as the output.
If there are two or more longest contiguous increasing sequences, the program must print the first occurring longest contiguous increasing sequence as the output.

Boundary Condition(s):
2 <= N <= 100
1 <= Each integer value <= 1000

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains the longest contiguous increasing sequence separated by a space.

Example Input/Output 1:
Input:
8
3 4 6 7 8 9 1 2

Output:
6 7 8 9

Example Input/Output 2:
Input:
7
8 9 10 2 4 5 6

Output:
8 9 10

Example Input/Output 3:
Input:
5
9 10 11 12 13

Output:
9 10 11 12 13
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n, start=0, end=0, maxLen=1, currLen=1, currStart=0;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++)
        scanf("%d",&arr[i]);
    for(int i=1;i<n;i++)
    {
        if (arr[i]==arr[i-1]+1)
        {
            currLen++;
        }
        else
        {
            if (currLen>maxLen)
            {
                maxLen=currLen;
                start=currStart;
                end=i-1;
            }
            currLen=1;
            currStart=i;
        }
    }
    if (currLen>maxLen)
    {
        maxLen=currLen;
        start=currStart;
        end=n-1;
    }
    for(int i=start;i<=end;i++)
        printf("%d ",arr[i]);

}
