/*The function/method solveExpression accepts an argument expression representing an expression as given below.

val1+val2=val3 or val1*val2=val3

In the above expression, one of the three values will be replaced with X.

The function/method solveExpression solve the given expression and find the value of X. Then the function must return the integer value X.

Your task is to implement the function solveExpression so that the program runs successfully.

IMPORTANT: Do not implement the main() function as it is already defined.

Example Input/Output 1:
Input:
5+X=7

Output:
2

Explanation:
If X = 2, then the expression becomes 5+2=7.

Example Input/Output 2:
Input:
4*5=X

Output:
20

Example Input/Output 3:
Input:
X+2=100

Output:
98

Example Input/Output 4:
Input:
X*2=100

Output:
50
*/
#include <stdio.h>
#include <stdlib.h>

int solveExpression(char *expression)
{
    char a[10],b[10],c[10];
    char sym;
    sscanf(expression,"%[^+|*]%c%[^=]=%s",a,&sym,b,c);
    int x,y,z;
    sscanf(a,"%d",&x);
    sscanf(b,"%d",&y);
    sscanf(c,"%d",&z);
    if (sym=='+')
    {
        if (a[0]=='X')
            return z-y;
        else if(b[0]=='X')
            return z-x;
        else
            return x+y;
    }
    else
    {
        if (a[0]=='X')
            return z/y;
        else if(b[0]=='X')
            return z/x;
        else
            return x*y;
    }

}
int main()
{
    char expression[51];
    scanf("%s", expression);
    printf("%d", solveExpression(expression));
    return 0;
}

