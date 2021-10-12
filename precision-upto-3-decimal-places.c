/*
The program must accept two integers X and Y as the input. The program must print the integer value with precision upto 3 decimal places when X is divided by Y 
as the output.

Example Input/Output 1:
Input: 
5 3 

Output:
1.667

Example Input/Output 2:
Input:
10 8 

Output: 
1.250
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int x,y;
    scanf("%d %d",&x,&y);
    printf("%.2f",x*1.0/y);

}
