/*
A table is sold at Rs. X after allowing a discount of Y%. The program must print the Marked Price (original price before discount) as the output. 

Formula:
X = Marked Price * ( 1 - Y/100) 

Example Input/Output 1:
Input:
5225 5 

Output: 
5500

Example Input/Output 2: 
Input: 
250 0 

Output:
250
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int x,y;
    scanf("%d %d",&x,&y);
    printf("%d",x*100/(100-y));
}
