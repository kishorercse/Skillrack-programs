/*
The program must accept a series of Parentheses as a string. The program must print Valid if the parentheses are balanced. Else the program must print Invalid.

Boundary Condition(s):
1 <= Length of string <= 1000

Input Format:
The first line contains the string.

Output Format:
The first line contains Valid or Invalid.

Example Input/Output 1:
Input:
(( ))

Output:
Valid

Example Input/Output 2:
Input:
(( ( ))

Output:
Invalid
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    char ch, stack[1001];
    int i=-1;
    while(scanf("%c",&ch)==1){
        if (ch=='('){
            stack[++i]=ch;
        }
        else if(ch==')'){
            if (i==-1 || stack[i]!='('){
                printf("Invalid");
                return;
            }
            i-=1;
        }
    }
    if (i==-1)
        printf("Valid");
    else
        printf("Invalid");
}
