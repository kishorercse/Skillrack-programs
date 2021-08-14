/*
A string S is passed as input.  S will contain multiple integer values followed by an alphabet.  The program must expand the alphabets based on the previous integer value.

Example 1:

Input:
4a5h
Output:
aaaahhhhh

Explanation:

As it is 4a and 5h, four a’s are printed followed by 5h’s

Example 2:

Input:
1k2b4k
Output:
kbbkkkk
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n;
    char c;
    while(scanf("%d%c",&n,&c)==2){
        while(n>0){
            printf("%c",c);
            n-=1;
        }
    }
}
