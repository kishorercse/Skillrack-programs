/*
The program must accept an integer array of size N and an integer S as the input. The program must print Yes if any of the sub-arrays is having the sum of their elements as S. 
Else the program must print No as the output.

Boundary Condition(s):
2 <= N <= 10^5
1 <= Each integer value <= 1000

Input Format:
The first line contains N.
The second line contains N integers separated by a space.
The third line contains S.

Output Format:
The first line contains Yes or No.

Example Input/Output 1:
Input:
5
5 10 50 20 25
45

Output:
Yes

Explanation:
The integers in the sub-array which is having the sum of their elements as 45 are given below.
20 25

Example Input/Output 2:
Input:
6
4 7 1 5 4 6
14

Output:
No
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int N, S;
    scanf("%d",&N);
    int arr[N];
    for(int index=0;index<N;index++)
    {
        scanf("%d",&arr[index]);
    }
    scanf("%d",&S);
    int left=0, right=0, sum=arr[0];
    while(right<N)
    {
        if (sum==S)
        {
            printf("Yes");
            return;
        }
        if (sum>S)
        {
            sum-=arr[left];
            left++;
        }
        else
        {
            sum+=arr[++right];
        }
    }
    printf("No");

}
