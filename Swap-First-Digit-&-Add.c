/*
The program must accept two integers X and Y as the input. The program must swap the first digit in X and Y. Then the program must print the sum of the modified values of X and
Y as the output.

Boundary Condition(s):
1 <= X, Y <= 10^8

Input Format:
The first line contains X and Y separated by a space.

Output Format:
The first line contains the sum of the modified values of X and Y.

Example Input/Output 1:
Input:
598 1024

Output:
5222

Example Input/Output 2:
Input:
123 78

Output:
741

Example Input/Output 3:
Input:
6 56

Output:
71


*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int x,y;
    scanf("%d %d",&x,&y);
    int xRem=0,xMul=1;
    while(x>9)
    {
        xRem=x%10*xMul+xRem;
        xMul*=10;
        x/=10;
    }
    int yRem=0,yMul=1;
    while(y>9)
    {
        yRem=y%10*yMul+yRem;
        yMul*=10;
        y/=10;
    }
    printf("%d",(x*yMul+yRem)+(y*xMul+xRem));
    
}
