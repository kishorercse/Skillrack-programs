/*
The program must accept N string values as the input. The program must print the common characters in all the N string values in sorted order as the output.
Note: At least one character is always present in all the N string values.

Boundary Condition(s):
2 <= N <= 10^4
1 <= Length of each string <= 10^4

Input Format:
The first line contains N.
The next N lines, each containing a string.

Output Format:
The first line contains the common characters in all the N string values in sorted order.

Example Input/Output 1:
Input:
5
engine
manager
generation
pen
mentor

Output:
en

Explanation:
The common characters in all the given 5 string values are e and n.
Hence the output is en

Example Input/Output 2:
Input:
3
Africa
Australia
Antarctica

Output:
Aair

Example Input/Output 3:
Input:
2
bbBBB
bbBBB

Output:
Bb
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int count[128]={0}, N;
    scanf("%d",&N);
    char str[10001];
    for(int ctr=1;ctr<=N;ctr++)
    {
        scanf("%s",str);
        for(int index=0;str[index]!='\0';index++)
        {
            if (count[str[index]]==ctr-1)
            {
                count[str[index]]+=1;
            }
        }
    }
    for(int index=1;index<128;index++)
    {
        if (count[index]==N)
        {
            printf("%c",index);
        }
    }

}
