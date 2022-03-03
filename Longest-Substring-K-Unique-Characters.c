/*
The program must accept a string S and an integer K as the input. The program must print the longest substring having exactly K unique characters as the output. If there are more than one such substring values in S, the program must print the first occurring one as the output.
Note: At least one substring in S has exactly K unique charaters.

Boundary Condition(s):
1 <= Length of S <= 10^5
1 <= K <= 26

Input Format:
The first line contains S and K separated by a space.

Output Format:
The first line contains the longest substring having exactly K unique characters.

Example Input/Output 1:
Input:
skillrack 3

Output:
kill

Explanation:
Here K = 3.
All possible longest substring values having exactly 3 unique characters are kill, illr and llra.
Here the first occurring longest substring is kill.
Hence the output is kill

Example Input/Output 2:
Input:
abbcdbbaabbace 3

Output:
bbaabba


*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    char str[100001];
    int K, count[128]={0};
    scanf("%s%d",str,&K);
    int start=0, end=0, maxLen=0, unique=0, strLen=strlen(str), maxStart=-1;
    while (end<strLen)
    {
        char ch=str[end];
        if (count[ch]==0)
        {
            unique++;
        }
        count[ch]++;
        if (unique==K)
        {
            int currLen=end-start+1;
            if (currLen>maxLen)
            {
                maxLen=currLen;
                maxStart=start;
            }
        }
        while(unique>K)
        {
            count[str[start]]--;
            if (count[str[start]]==0)
            {
                unique--;
            }
            start++;
        }
        end++;
    }
    for(int index=maxStart;index<maxStart+maxLen;index++)
    {
        printf("%c",str[index]);
    }
}
