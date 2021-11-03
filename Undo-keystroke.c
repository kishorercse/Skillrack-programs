/*
A series of keystrokes as a string is given as the input to the program. The character * represents undo action to clear the last entered keystroke. The program must print the 
string typed after applying the undo operations as the output. 

Boundary Condition(s): 
1 <= Length of each string <= 100 

Input Format: 
The first line contains the string.

Output Format:
The first line contains the string after applying the undo operations as the output. 

Example Input/Output 1: 
Input: 
lucky * draty**w 

Output:
lucky draw 

Example Input/Output 2:
Input:
trui**yhap*rd 

Output:
tryhard
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    char stack[101];
    int top=-1;
    char ch;
    while(scanf("%c",&ch)==1){
        if (ch=='\n' || ch=='\r')
            break;
        if (ch=='*'){
            if (top!=-1)
                top--;
        }
        else
            stack[++top]=ch;
    }
    stack[++top]='\0';
    printf("%s",stack);

}
