/*
The program must accept the alphabets emitted by the two signal systems (S1, S2) as the input. The program must print the length of the longest common signal emitted by these
two signal systems as the output.

Boundary Condition(s):
1 <= Length of S1, S2 <= 10^4

Input Format:
The first line contains S1.
The second line contains S2.

Output Format:
The first line contains the length of the longest common signal emitted by the two signal systems.

Example Input/Output 1:
Input:
nose
raise

Output:
2

Explanation:
se is the longest common signal whose length is 2.

Example Input/Output 2:
Input:
abcdelkgxwvu
abclkgxyz

Output:
4
*/
#include<stdio.h>
#include<stdlib.h>
#define MAX(x,y) ((x>y)?x:y)
int main()
{
    char s1[10001], s2[10001];
    scanf("%s %s",s1,s2);
    int l1=strlen(s1), l2=strlen(s2), dp[l1][l2], maxLen=0;
    for(int i=0;i<l1;i++)
    {
        for(int j=0;j<l2;j++)
        {
            if (s1[i]==s2[j])
            {
                if (i>=1 && j>=1)
                {
                    dp[i][j]=dp[i-1][j-1]+1;
                }
                else
                {
                    dp[i][j]=1;
                }
                maxLen=MAX(dp[i][j],maxLen);
            }
            else
            {
                dp[i][j]=0;
            }
        }
    }
    printf("%d",maxLen);

}
