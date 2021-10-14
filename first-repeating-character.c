/*
A string S is passed as the input. S has at least one repeating character. The program must print the first repeating character C.

Input Format: 
The first line contains S. 

Output Format:
The first line contains C. 

Boundary Conditions: 
Length of S will be from 3 to 100.

Example Input/Output 1:
Input:
abcdexyzbwqpoolj 

Output: 
b
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    char s[101];
    int len;
    scanf("%[^\n]%n",s,&len);
    int count[128]={0}, arr[len];
    for(int i=len-1;i>=0;i--){
        count[s[i]]++;
        arr[i]=count[s[i]];
    }
    for(int i=0;i<len;i++){
        if (arr[i]>1){
            printf("%c",s[i]);
            break;
        }
    }

}
