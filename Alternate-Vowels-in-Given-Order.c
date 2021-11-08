/*
The program must accept two string values S1 and S2 containing only alphabets as the input. The program must print the vowels in S1 and S2 alternatively in the given order. 
If S1 contains more vowels than S2 then the program must print the remaining vowels in S1 in the given order. If S2 contains more vowels than S1 then the program must print 
the remaining vowels in S2 in the given order. Note: At least one vowel is always present in either S1 or S2.

Boundary Condition(s): 
2 <= Length of S1, S2 <= 100 

Input Format: 
The first line contains S1. 
The second line contains S2. 

Output Format: 
The first line contains the vowels alternatively based on the given conditions.

Example Input/Output 1:
Input: 
environment 
jungle 

Output: 
euieoe 

Explanation: 
eu is printed from the string values environment and jungle.
ie is printed from the string values environment and jungle. 
Here, the string environment contains more vowels than the string jungle.
The remaining vowels in the string environment which do not have matching pairs in the string jungle are o and e. So they are printed after "euie".
Hence the output is euieoe 

Example Input/Output 2: 
Input: 
CENTER 
BACKSPACE 

Output: 
EAEAE
*/
#include<stdio.h>
#include<stdlib.h>

int isVowel(char ch)
{
    ch=tolower(ch);
    return ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u';
}
int main()
{
    char a[101], b[101];
    scanf("%s %s",a,b);
    int i=0, j=0;
    while (a[i] || b[j])
    {
        while(a[i])
        {
            if (isVowel(a[i]))
            {
                printf("%c",a[i++]);
                break;
            }
            i++;
        }
        while(b[j])
        {
            if (isVowel(b[j]))
            {
                printf("%c",b[j++]);
                break;
            }
            j++;
        }
    }
}
