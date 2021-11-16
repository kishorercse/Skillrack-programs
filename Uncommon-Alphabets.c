/*
The program must accept values of two string S1 and S2 as input. The program must print the uncommon alphabets in both S1 and S2.

Boundary Condition(s):
1 <= Length of string S1 and S2 <= 1000 

Input Format:
The first line contains the value of string S1. 
The second line contains the value of string S2. 

Output Format: 
The first line contains the uncommon alphabet(s) in S2.
The second line contains the uncommon alphabet(s) in S1. 

Example Input/Output 1: 
Input: 
apple
pen

Output:
n 
al

Explanation: 
n is an uncommon alphabet in pen. So, n is printed 
a and l are uncommon alphabets in apple. So, al is printed

Example Input/Output 2: 
Input:
hello
world

Output:
wrd
he
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    char a[1001], b[1001];
    scanf("%s %s",a,b);
    int x[128]={0}, y[128]={0};
    for(int i=0; a[i]; i++)
    {
        x[a[i]]++;
    }
    for(int i=0; b[i]; i++)
    {
        y[b[i]]++;
        if (x[b[i]]==0)
        {
            printf("%c",b[i]);
            x[b[i]]=-1;
        }
    }
    printf("\n");
    for(int i=0; a[i]; i++)
    {
        if (y[a[i]]==0)
        {
            printf("%c",a[i]);
            y[a[i]]=-1;
        }
    }
}
