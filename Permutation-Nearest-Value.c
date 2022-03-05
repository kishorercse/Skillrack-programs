/*
The program must accept two integers N and X as the input. The program must print the integer value nearest to X with all the digits in N as the output.

Boundary Condition(s):
10 <= N, X <= 10^8

Input Format:
The first lines contains N.

Output Format:
The first lines contains the integer value nearest to X with all the digits in N as the output.

Example Input/Output 1:
Input:
123 200

Output:
213

Explanation:
The integer value nearest to the 200 with all the digits in 123 is 213.

Example Input/Output 2:
Input:
48871 88555

Output:
88471
*/
#include<stdio.h>
#include<stdlib.h>
#include<limits.h>
int x, closest=INT_MAX;

void swap(char *str, int x, int y)
{
    char temp=str[x];
    str[x]=str[y];
    str[y]=temp;
}
void permute(char *str, int left, int right)
{
    if (left==right)
    {
        int curr=atoi(str);
        if (abs(curr-x)<abs(closest-x))
        {
            closest=curr;
        }
        return;
    }
    for(int index=left;index<=right;index++)
    {
        swap(str,left,index);
        permute(str, left+1, right);
        swap(str,left,index);
    }
}

int main()
{
    char n[11];
    int len;
    scanf("%s%n%d",n,&len,&x);
    permute(n,0,len-1);
    printf("%d",closest);

}
