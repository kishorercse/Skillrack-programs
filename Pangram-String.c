/*
A string S is passed as the input to the program. If S is a pangram, the program must print yes else it must print no. Uppercase and lower case letters of an alphabet are 
considered the same.

Pangram definition from WikiPedia: A Pangram (Greek: pan gramma, "every letter") or holoalphabetic sentence for a given alphabet is a sentence using every letter of the 
alphabet at least once.

Input Format:
The first line contains S

Output Format:
The first line contains the value yes or no depending on whether S is a pangram or not.

Boundary Conditions:
5 <= Length of S <= 1000

Example Input/Output 1:
Input:
Five jumping wizards hex bolty quick

Output:
yes

Example Input/Output 2:
Input:
abcdefghijklqrstuvwxyz

Output:
no

Explanation:
The alphabets mnop are not present.
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int arr[26]={0}, tot=0;
    char s[1001];
    scanf("%[^\n]",s);
    for(int i=0;s[i];i++)
    {
        if (s[i]!=' ')
        {
            s[i]=tolower(s[i]);
            if (arr[s[i]-97]==0)
            {
                arr[s[i]-97]=1;
                tot+=1;
                if(tot==26)
                {
                    printf("yes");
                    return 0;
                }
            }
        }
    }
    printf("no");
}
