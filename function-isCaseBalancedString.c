/*
The function/method isCaseBalancedString accepts an argument str. The string str contains only alphabets.

The function/method isCaseBalancedString must check if the given string is a case balanced string or not based on the following conditions.
- If a string is formed using the first half of the lower case alphabets and the second half of the upper case alphabets, or the first half of the upper case alphabets and the
second half of the lower case alphabets in the English alphabet set, then it is a case balanced string. Else the string is not a case balanced string.
The function must return 1 if the given string is a case balanced string. Else the function must return 0.

Your task is to implement the function isCaseBalancedString so that the program runs successfully.

IMPORTANT: Do not implement the main() function as it is already defined.

Boundary Condition(s):
1 <= Length of S <= 100

Example Input/Output 1:
Input:
elePhaNT

Output:
1

Explanation:
The lower case alphabets in the given string are e, l, e, h and a (All are from the first half of the English alphabet set).
The upper case alphabets in the given string are P, N and T (All are from the second half of the English alphabet set).
Here the given string is formed using the first half of the lower case alphabets and the second half of the upper case alphabets. So 1 is printed.

Example Input/Output 2:
Input:
sKILLrACK

Output:
1

Example Input/Output 3:
Input:
noteBOOK

Output:
0
*/
#include <stdio.h>
#include <stdlib.h>

int isCaseBalancedString(char *str)
{
    int fhl=0, shu=0, fhu=0, shl=0;
    for(int i=0;str[i];i++)
    {
        if (str[i]>='a' && str[i]<='m')
            fhl=1;
        else if(str[i]>='n' && str[i]<='z')
            shl=1;
        else if(str[i]>='A' && str[i]<='M')
            fhu=1;
        else if(str[i]>='N' && str[i]<='Z')
            shu=1;

    }
    return (fhl+shu+fhu+shl==1) || (fhl==1 && shu==1 && fhu==0 && shl==0) || (fhu==1 && shl==1 && fhl==0 && shu==0);
}

int main()
{
    char str[101];
    scanf("%s", str);
    printf("%d", isCaseBalancedString(str));
    return 0;
}
