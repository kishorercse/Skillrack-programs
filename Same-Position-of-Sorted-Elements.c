/*
The program must accept two arrays of same size N as the input. The program must sort both the arrays. The program must print YES if the elements in the first array are less 
than or equal to the elements in the second array in the same position. Else the program must NO as the output.

Boundary Conditon(s):
1 <= N <= 100
1 <= Array Element Value <= 10000

Input Format:
The first line contains the integer value of N.
The second line and the third line contains N integers separated by spaces.

Output Format:
The first line contains either YES or NO.

Example Input/Output 1:
Input:
5
8 2 4 6 3
9 12 7 3 10

Output:
YES

Explanation:
The sorted elements of the first array are 2 3 4 6 8
The sorted elements of the second array  are 3 7 9 10 12
The elements in the first position of both the arrays are 2 and 3.
The elements in the second position of both the arrays are 3 and 7.
The elements in the third position of both the arrays are 4 and 9.
Similarly, the same position elements in the first array is less than or equal to the elements in the second array.
Hence the output is YES

Example Input/Output 2:
Input:
6
12 20 40 5 9 12
8 25 30 20 15 23

Output:
NO
*/
#include<stdio.h>
#include<stdlib.h>
void sort(int *arr, int size)
{
    for(int i=0;i<size-1;i++)
    {
        for(int j=0;j<size-i-1;j++)
        {
            if (arr[j]>arr[j+1])
            {
                int t=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=t;
            }
        }
    }
}
int main()
{
    int n;
    scanf("%d",&n);
    int arr1[n],arr2[n];
    for(int i=0;i<n;i++)
        scanf("%d",&arr1[i]);
    for(int i=0;i<n;i++)
        scanf("%d",&arr2[i]);
    sort(arr1,n);
    sort(arr2,n);
    int flag=1;
    for(int i=0;i<n;i++)
    {
        if (arr1[i]>arr2[i])
        {
            flag=0;
            break;
        }
    }
    if (flag==1)
        printf("YES");
    else
        printf("NO");
}
