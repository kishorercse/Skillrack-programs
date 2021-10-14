/*
An odd length string S is passed as the input. The middle three letters of S must be printed as the output. 

Input Format:
First line will contain the string value S 

Output Format: 
First line will contain the middle three letters of S.

Boundary Conditions:
Length of S is from 5 to 100

Example Input/Output 1:
Input: 
level 

Output: 
eve 

Example Input/Output 2:
Input:
manager 

Output:
nag
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    char s[101];
    int len,t;
    scanf("%s%n",s,&len);
    t=len/2;
    for(int i=t-1;i<=len-t;i++){
        printf("%c",s[i]);
    }

}
