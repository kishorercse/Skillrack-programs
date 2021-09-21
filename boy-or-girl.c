/*
The program must accept a character CH as the input. 
The program must print the output based on the following conditions. 
- If CH is b or B then print BOY. 
- If CH is g or G then print GIRL. 

Input Format: 
The first line contains the value of CH. 

Output Format: The first line contains either BOY or GIRL. 

Example Input/Output 1: 
Input:
b 

Output: 
BOY 

Example Input/Output 2: 
Input: 
G

Output: 
GIRL
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    char ch;
    scanf("%c",&ch);
    ch=tolower(ch);
    if (ch=='b')
        printf("BOY");
    else
        printf("GIRL");
}
