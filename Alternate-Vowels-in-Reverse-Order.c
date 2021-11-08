/*
The program must accept two string values S1 and S2 as the input. The program must print the vowels in S1 and S2 alternatively in the reverse order. If S1 contains more vowels 
than S2 then the program must print the remaining vowels in S1 in the reverse order. If S2 contains more vowels than S1 then the program must print the remaining vowels in S2 
in the reverse order. The alphabets in S1 and S2 are always in lower case. Note: At least one vowel is always present in either S1 or S2. 

Boundary Condition(s):
2 <= Length of S1 and S2 <= 100 

Input Format:
The first line contains the string S1.
The second line contains the string S2.

Output Format: 
The first line contains the vowels alternatively based on the above conditions. 

Example Input/Output 1:
Input:
environment
jungle 

Output: 
eeouie 

Explanation: 
ee is printed from S1 and S2.
ou is printed from S1 and S2.
Here S1 contains more vowels than S2.
The remaining vowels in S1 which do not have matching pairs in S2 are e and i. So they are printed in reverse order after "eeou". 
Hence the output is eeouie 

Example Input/Output 2: 
Input: 
center 
backspace 

Output: 
eeeaa
*/
#include<stdio.h>
#include<stdlib.h>

int isVowel(char ch)
{
    return ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u';
}
int main()
{
    char a[101], b[101];
    scanf("%s %s",a,b);
    int x=strlen(a)-1, y=strlen(b)-1;
    while(x>=0 || y>=0){
        while(x>=0)
        {
            if (isVowel(a[x]))
            {
                printf("%c",a[x--]);
                break;
            }
            x--;
        }
        while(y>=0)
        {
            if (isVowel(b[y]))
            {
                printf("%c",b[y--]);
                break;
            }
            y--;
        }
    }
}
