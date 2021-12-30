/*
The function/method removeAlphabetsEvaluateExp accepts an argument str. The string str represents an arithmetic expression but some alphabets are inserted in the expression.

The function/method removeAlphabetsEvaluateExp must remove those alphabets and evaluate the expression. Then the function must return an integer representing the result of the 
expression.

Note:
- The operators in the expression are addition (+), subtraction (-), multiplication (*) and division (/).
- Evaluation must be done from left to right direction.

Your task is to implement the function removeAlphabetsEvaluateExp so that the program runs successfully.

IMPORTANT: Do not write the main() function as it is already defined.

Example Input/Output 1:
Input:
ab4cd+e2f0g-hi5hello*how3are-1you

Output:
56

Explanation:
After removing the alphabets in the given string, the string becomes "4+20-5*3-1".
4+20-5*3-1 => 24-5*3-1
24-5*3-1 => 19*3-1
19*3-1 => 57-1
57-1 => 56

Example Input/Output 2:
Input:
100cow/cat25lions+4*5tiger-255

Output:
-215

Explanation:
After removing the alphabets in the given string, the string becomes "100/25+4*5-255".
100/25+4*5-255 => 4+4*5-255
4+4*5-255 => 8*5-255
40-255 => -215
*/
#include<stdio.h>
#include<stdlib.h>

int isSymbol(char ch)
{
    return ch=='+' || ch=='-' || ch=='*' || ch=='/';
}
int removeAlphabetsEvaluateExp(char *expression)
{
    int res=0, n=0, i=0, f=-1;
    for(i=0;expression[i];i++)
    {
        if (isdigit(expression[i]))
            res=res*10+(expression[i]-'0');
        else if(isSymbol(expression[i]))
        {
            if (expression[i]=='+')
            {
                f=0;
            }
            else if(expression[i]=='-')
            {
                f=1;
            }
            else if(expression[i]=='*')
            {
                f=2;
            }
            else if(expression[i]=='/')
            {
                f=3;
            }
            break;
        }
    }
    i++;
    while(expression[i])
    {
        if (isdigit(expression[i]))
            n=n*10+(expression[i]-'0');
        else if(isSymbol(expression[i]))
        {
            if (f==0)
                res+=n;
            else if(f==1)
                res-=n;
            else if(f==2)
                res*=n;
            else if(f==3)
                res/=n;
            if (expression[i]=='+')
                f=0;
            else if(expression[i]=='-')
                f=1;
            else if(expression[i]=='*')
                f=2;
            else if(expression[i]=='/')
                f=3;
            n=0;
        }
        i++;
    }
    if (f==0)
        res+=n;
    else if(f==1)
        res-=n;
    else if(f==2)
        res*=n;
    else if(f==3)
        res/=n;
    return res;
}
int main()
{
    char expression[101];
    scanf("%s", expression);
    printf("%d", removeAlphabetsEvaluateExp(expression));
    return 0;
}
