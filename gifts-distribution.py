/*
A celebrity on the day of her birthday is distributing N gift boxes to school children. Each school gets X gift boxes. Given N and X as the input, 
the program must print the number of schools that can each get X gift boxes.

Example Input/Output 1: 
Input: 
500 25 

Output: 
20 

Example Input/Output 2: 
Input: 
950 20 

Output: 
47
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n,x;
    scanf("%d %d",&n,&x);
    printf("%d",n/x);

}
