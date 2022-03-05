/*
The program must accept a string S as the input. The program must print all the permutations of the string S as the output.

Boundary Condition(s):
2 <= Length of S <= 10

Input Format:
The first line contains S.

Output Format:
The lines containing all the permutations of the string S.

Example Input/Output 1:
Input:
abc

Output:
abc
acb
bac
bca
cba
cab

Example Input/Output 2:
Input:
rack

Output:
rack
rakc
rcak
rcka
rkca
rkac
arck
arkc
acrk
ackr
akcr
akrc
cark
cakr
crak
crka
ckra
ckar
kacr
karc
kcar
kcra
krca
krac
*/
#include<stdio.h>
#include<stdlib.h>

void swap(char *str, int x, int y)
{
    char temp=str[x];
    str[x]=str[y];
    str[y]=temp;
}

void permute(char *str, int left, int right)
{
    if (left==right)
    {
        printf("%s\n",str);
        return;
    }
    for(int index=left;index<=right;index++)
    {
        swap(str,left,index);
        permute(str,left+1,right);
        swap(str,left,index);
    }
}
int main()
{
    char s[11];
    int len;
    scanf("%s%n",s,&len);
    permute(s,0,len-1);
}
