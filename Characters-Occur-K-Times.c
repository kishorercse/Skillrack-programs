/*
The program must accept two string values S1 and S2 and print the characters that occur K or more times in both S1 and S2. The program must also print the characters that occur 
just once in both S1 and S2. The characters must be printed in the same order as they appear in S2.

Boundary Condition(s):
2 <= Length of S1, S2 <= 100
2 <= K <= 20

Input Format:
The first line contains S1.
The second line contains S2.
The third line contains K.

Output Format:
The first line contains the characters based on the given conditions.

Example Input/Output 1:
Input:
bookkeeper
repeated
3

Output:
repee

Example Input/Output 2:
Input:
Man@ger
Green
2

Output:
rn

Example Input/Output 3:
Input:
Mississippi
Possessiveness
4

Output:
ssssss
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    char s1[101], s2[101];
    int count1[128]={0}, count2[128]={0}, k;
    scanf("%s%s%d",s1,s2,&k);
    for(int i=0;s1[i];i++)
        count1[s1[i]]++;
    for(int i=0;s2[i];i++)
        count2[s2[i]]++;
    for(int i=0;s2[i];i++)
    {
        if ((count1[s2[i]]==1 && count2[s2[i]]==1) || (count1[s2[i]]>=k && count2[s2[i]]>=k))
            printf("%c",s2[i]);
    }

}
