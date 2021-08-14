/*
String S is passed as the input to the program. S may or may not have a single underscore embedded in it. The program must reverse the String S till the first underscore and print it as the output.

Example 1:

Input:
abcd_pqrs
Output:
dcba_pqrs

Example 2:

Input:
_kilo
Output:
_kilo

Example 3:

Input:
nounderscore
Output:
erocsrednuon
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    char s[101],t;
    int i,j=0;
    scanf("%[^\n]",s);
    for(i=0;s[i]!='\0';i++){
        if (s[i]=='_')
            break;
    }
    i-=1;
    while (j<i){
        t=s[j];
        s[j]=s[i];
        s[i]=t;
        j+=1;
        i-=1;
    }
    printf("%s",s);
}
