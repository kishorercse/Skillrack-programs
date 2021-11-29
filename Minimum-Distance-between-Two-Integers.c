/*
The program must accept an integer array of size N and two integers X and Y as the input. The program print the minimum distance between X and Y in the array as the output.
Note: The integers X and Y are present in the array.

Boundary Condition(s):
1 <= N <= 100

Input Format:
The first line contains the value of N.
The second line contains N integers separated by space(s).
The third line contains the values of X and Y separated by a space.

Output Format:
The first line contains the minimum distance between X and Y.

Example Input/Output 1:
Input:
10
8 9 5 12 8 4 21 6 2 12
8 12

Output:
2

Explanation:
The possible distances between 8 and 12 are
8 9 5 12 - Here the distance is 4.
12 8 - Here the distance is 2.
8 4 21 6 2 12 - Here the distance is 6.
The minimum distance among all the possible distances is 2.
Hence the output is 2

Example Input/Output 2:
Input:
12
31 18 78 31 86 45 75 48 45 26 57 45
45 31

Output:
3
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
    int x, y, ind1=-1, ind2=-1, min=99999999;
    scanf("%d %d",&x,&y);
    for(int i=0;i<n;i++)
    {
        if (arr[i]==x)
            ind1=i;
        else if(arr[i]==y)
            ind2=i;
        else
            continue;
        if (ind1!=-1 && ind2!=-1)
        {
            int dis=abs(ind1-ind2);
            if (dis<min)
                min=dis;
        }
    }
    printf("%d",min+1);
}
