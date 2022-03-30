/*
The function/method getTotalPrice accepts an argument str representing a text. The text contains the prices of some items as floating point values.

The function/method getTotalPrice must return a floating point value representing the total price of the items mentioned in the text.

Your task is to implement the function getTotalPrice so that the program runs successfully.

Note: The total price will be printed with the precision up to 2 decimal places.


Example Input/Output 1:
Input:
Cost of 5 pens is 50.98 rupees. Cost of a pencil is 4.25.

Output:
55.23

Explanation:
There are two prices (50.98 and 4.25) mentioned in the given text.
So their sum is 55.23 which is printed as the output.

Example Input/Output 2:
Input:
A is 5.60, B is 2.14, C is 100.58 and D is 50.6.

Output:
158.92
*/

#include <stdio.h>
#include <stdlib.h>
int isDouble(char *word)
{
    for(int i=1;word[i]!='\0';i++)
    {
        if (word[i]=='.')
        {
            if (isdigit(word[i-1]) && isdigit(word[i+1]))
                return 1;
            else
                return 0;
        }
    }
    return 0;
}
double getTotalPrice(char *str)
{
    double sum=0;
    int index=0, len=strlen(str), t;
    char word[15], rem[15];
    while(index<len && sscanf(str+index,"%s %n",word,&t)==1)
    {
        if (isDouble(word))
        {
            sum += strtod(word,&rem);
        }
        index+=t;
    }
    return sum;
}

int main()
{
    char str[101];
    scanf("%[^\n\r]", str);
    double totalPrice = getTotalPrice(str);
    printf("%.2lf", totalPrice);
    return 0;
}
