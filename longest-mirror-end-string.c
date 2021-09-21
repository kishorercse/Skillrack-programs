/*
The program must accept a string S and print the longest mirror end substring. The mirror end substring is
present in the beginning of the string and also at the end of the string in the reverse order. If there is 
no such mirror end string, then the program must print 0 as the output. 

Boundary Condition(s): 
1 <= Length of S <= 100 

Input Format: 
The first line contains S. 

Output Format: 
The first line contains a string value. 

Example Input/Output 1: 
Input: 
abefba 

Output: 
ab 

Example Input/Output 2: 
Input: 
abacus 

Output: 
0

Example Input/Output 3: 
Input: 
level 

Output: 
level
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int i=0,j;
    char s[101];
    scanf("%s%n",s,&j);
    j-=1;
    while(i<=j){
        if (s[i]!=s[j]){
            s[i]='\0';
            break;
        }
        i+=1;
        j-=1;
    }
    if (i==0)
        printf("0");
    else
        printf("%s",s);
    return 0;
}
