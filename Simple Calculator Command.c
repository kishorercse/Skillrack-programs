/*
A string S is passed as input. S will contain two integer values separated by one of these alphabets -A,S,M,D where
-A or a is for addition
-S or s is for subtraction
-M or m is for multiplication
-D or d is for division

The program must perform the necessary operation and print the result as the output. (Ignore any floating point values just print the integer result)

Example 1:

Input:
5A11
Output:
16

Example 2:

Input:
120d6
Output:
20
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int a,b;
    char c;
    scanf("%d%c%d",&a,&c,&b);
    c=tolower(c);
    switch(c){
        case 'a':
            printf("%d",a+b);
            break;
        case 's':
            printf("%d",a-b);
            break;
        case 'm':
            printf("%d",a*b);
            break;
        case 'd':
            printf("%d",a/b);
    }

}
