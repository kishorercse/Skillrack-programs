/*
The program must accept N integers and an integer X as the input. The integers form a sequence starting from the smallest integer to the largest integer. There are some 
integers which are missing in the sequence formed by all the integers from the smallest integer to the largest integer. The program must print the Xth smallest missing 
integer in the given integers as the output. Else the program must print -1 as the output.

Boundary Condition(s):
1 <= N, X <= 100
1 <= Array Element Value <= 100

Input Format:
The first line contains N and X separated by a space.
The second line contains N integers separated by space.

Output Format:
The first line contains either Xth missing integer or -1.

Example Input/Output 1:
Input:
5 3
2 7 4 5 10

Output:
8

Explanation:
The sorted elements are 2 4 5 7 10
The missing element between 2 and 4 is 3. So, the first missing element is 3.
The missing element between 5 and 7 is 6. So, the second missing element is 6.
The missing elements between 7 and 10 are 8 and 9. So, the third missing element is 8 and the fourth missing element is 9.
Value of X is 3. So the third missing element 8 is printed.

Example Input/Output 2:
Input:
7 10
12 7 9 18 10 15 19

Output:
-1


*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n,x;
    scanf("%d %d",&n,&x);
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
        int t=arr[i];
        arr[i]=arr[minIndex];
        arr[minIndex]=t;
    }
    int f=0;
    for(int i=1;i<n;i++)
    {
        if (arr[i]!=arr[i-1])
        {
            if (arr[i]-1!=arr[i-1])
                x-=arr[i]-arr[i-1]-1;
                if (x<=0)
                {
                    printf("%d",arr[i]+x-1);
                    f=1;
                    break;
                }
        }
    }    
    if (f==0)
        printf("-1");

}
