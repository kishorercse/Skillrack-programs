/*
The program must accept two integer arrays of same size N as the input. The program must print the elements if the first element in the first array is equal to the Nth 
element in the second array, then the second element in the first array is equal to the N-1th element in the second array and so on. If there is no element is equal then 
the program must print -1 as the output.

Boundary Condition(s):
2 <= N <= 100
1 <= Array Element Value <= 100000

Input Format:
The first line contains the value of N.
The second line contains N integers separated by space(s).
The third line contains N integers separated by space(s).

Output Format:
The first line contains either the integers in the array separated by space(s) or -1.

Example Input/Output 1:
Input:
5
4 12 55 98 53
43 98 34 33 4

Output:
4 98

Explanation:
The first element in the first array is 4 and the fifth element in the second array is 4 both are same
The second element in the first array is 12 and the fourth element in the second array is 33 both are different
The third element in the first array is 55 and the third element in the second array is 34 both are different
The fourth element in the first array is 98 and the second element in the second array is 98 both are same
The fifth element in the first array is 53 and the first element in the second array is 43 both are different
Hence the output is 4 98

Example Input/Output 2:
Input:
10
56 6 3 59 53 40 28 7 23 57
53 30 18 33 4 13 56 55 9 12 

Output:
-1
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n;
    scanf("%d",&n);
    int arr1[n],arr2[n],flag=0;
    for(int i=0;i<n;i++)
        scanf("%d",&arr1[i]);
    for(int i=n-1;i>=0;i--)
        scanf("%d",&arr2[i]);
    for(int i=0;i<n;i++)
    {
        if (arr1[i]==arr2[i])
        {
            printf("%d ",arr1[i]);
            flag=1;
        }
    }
    if (flag==0)
        printf("-1");

}
