/*
The program must accept a positive integer array of size of N as the input. The program must print the middle element(s) in the sorted array as the output.

Boundary Condition(s):
3 <= N <= 50
1 <= Each array element value <= 999

Input Format:
The first line contains the value of N.
The second line contains N integers separated by space(s).

Output Format:
The first line contains the middle element(s) in the sorted array.

Example Input/Output 1:
Input:
5
98 26 47 29 10

Output:
29

Explanation:
The elements in the sorted array are 10 26 29 47 98.
There is only one middle element 29.
Hence 29 is printed

Example Input/Output 2:
Input:
6
45 88 27 19 20 8

Output:
20 27


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
        int minIndex=i;
        for(int j=i+1;j<n;j++)
        {
            if (arr[j]<arr[minIndex])
                minIndex=j;
        }
        int t=arr[minIndex];
        arr[minIndex]=arr[i];
        arr[i]=t;
    }
    if (n%2==0)
        printf("%d %d",arr[n/2-1],arr[n/2]);
    else
        printf("%d",arr[n/2]);

}
