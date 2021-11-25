"""
The program must accept an integer array of size N as the input. The program must print the count of pairs in the array so that the integers in the pair are sorted in 
descending order as the output.

Boundary Condition(s):
1 <= N <= 100

Input Format:
The first line contains the value of N.
The second line contains N integers separated by space(s).

Output Format:
The first line contains the count of pairs in the array based on the condition mentioned above.

Example Input/Output 1:
Input:
5
2 8 7 5 6

Output:
5

Explanation:
The pairs which satisfy the given conditions are (8, 7), (8, 5), (8, 6), (7, 5) and (7, 6).
The count of pairs is 5.
Hence the output is 5

Example Input/Output 2:
Input:
7
51 56 5 25 75 38 73

Output:
8
"""
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n;
    scanf("%d",&n);
    int arr[n], count=0;
    for(int i=0;i<n;i++)
        scanf("%d",&arr[i]);
    for(int i=0;i<n-1;i++)
    {
        for(int j=i+1;j<n;j++)
        {
            if (arr[i]>arr[j])
                count++;
        }
    }
    printf("%d",count);

}
