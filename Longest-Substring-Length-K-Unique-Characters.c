/*
The program must accept a string S and an integer K as the input. The program must print the length of the longest substring having exactly K unique characters as the output.

Boundary Condition(s):
1 <= Length of S <= 10^5
1 <= K <= 26

Input Format:
The first line contains S and K separated by a space.

Output Format:
The first line contains the length of the longest substring having exactly K unique characters.

Example Input/Output 1:
Input:
mirror 2

Output:
4

Explanation:
Here K = 2.
The longest substring having exactly 2 unique characters is rror.
So the length of the longest substring rror is 4.
Hence the output is 4

Example Input/Output 2:
Input:
abbcdbbaabbace 3

Output:
8
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    char str[100001];
    int K, start=0, end=0, strLen, maxLen=0, unique=0, count[128]={0};
    scanf("%s%d",str,&K);
    strLen=strlen(str);
    while(end<strLen) 
    {
        char ch=str[end];
        if (count[ch]==0)
        {
            unique++;
        }
        count[ch]++;
        if (unique==K)
        {
            int t=end-start+1;
            maxLen=t>maxLen?t:maxLen;
        }
        else if (unique>K)
        {
            while(unique>K)
            {
                count[str[start]]--;
                if (count[str[start]]==0)
                {
                    unique--;
                }
                start++;
            }
        }
        end++;
    }
    printf("%d",maxLen);
}
