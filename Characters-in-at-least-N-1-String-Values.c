/*
The program must accept N string values as the input. The program must print the common characters that are present in N or N-1 string values in sorted order as the output.
Note: At least one character is always present in N or N-1 string values.

Boundary Condition(s):
3 <= N <= 10^4
1 <= Length of each string <= 10^4

Input Format:
The first line contains N.
The next N lines, each containing a string.

Output Format:
The first line contains the common characters in sorted order that are present in N or N-1 string values in sorted order.

Example Input/Output 1:
Input:
3
orange
apple
pineapple

Output:
aelnp

Explanation:
The common characters that are present in 3 or 2 string values are a, e, l, n and p.
Hence the output is aelnp

Example Input/Output 2:
Input:
4
HardWork
HomeWork
Hungry
Wood

Output:
HWor
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int N, count[128]={0};
    scanf("%d",&N);
    char str[10001];
    for(int ctr=0;ctr<N;ctr++)
    {
        scanf("%s",str);
        int strCount[128]={0};
        for(int index=0;str[index]!='\0';index++)
        {
            char ch=str[index];
            if (strCount[ch]==0 && count[ch]>=ctr-1)
            {
                count[ch]++;
            }
            strCount[ch]++;
        }
    }
    for(int index=1;index<128;index++)
    {
        if (count[index]>=N-1)
        {
            printf("%c",index);
        }
    }

}
