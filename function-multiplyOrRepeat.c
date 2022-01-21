/*
The function/method multiplyOrRepeat accepts an argument str. The string str contains two positive integers(X, Y) separated by an asterisk or a word(W) and a positive integer(N)
separated by an asterisk.

The function/method multiplyOrRepeat must return a string based on the following conditions.
- If the given string contains two integers, then the function must return their product as a string.
- Else the function must form a string by repeating the word N times. Then the function must return the resulting string.

Your task is to implement the function multiplyOrRepeat so that the program runs successfully.

IMPORTANT: Do not write the main() function as it is already defined.

Example Input/Output 1:
Input:
15*120

Output:
1800

Explanation:
The given string contains two integers(15 and 120) separated by an asterisk.
So their product is printed as the output.

Example Input/Output 2:
Input:
Skill*4

Output:
SkillSkillSkillSkill

Explanation:
The given string contains a word and an integer("Skill" and 4) separated by an asterisk.
So the word "Skill" is repeated 4 times.

Example Input/Output 3:
Input:
10*CSE

Output:
CSECSECSECSECSECSECSECSECSECSE
*/
#include <stdio.h>
#include <stdlib.h>

char* multiplyOrRepeat(char *str)
{
    int len=strlen(str), x, y;
    static char res[101];
    if (isalpha(str[0]))
    {
        sscanf(str,"%[^*]*%d",res,&x);
    }
    else if (isalpha(str[len-1]))
    {
        sscanf(str,"%d*%s",&x,res);
    }
    else
    {
        sscanf(str,"%d*%d",&x,&y);
        sprintf(res,"%d",x*y);
        return res;
    }
    char temp[101];
    sprintf(temp,"%s",res);
    while (x-- > 1)
    {
        sprintf(res,"%s%s",res,temp);
    }
    return res;
}


int main()
{
    char str[101];
    scanf("%s", str);
    char *result = multiplyOrRepeat(str);
    if(result == NULL || result == str)
    {
        printf("String is not formed\n");
    }
    if(result[0] == '\0' || result[0] == ' ')
    {
        printf("String is empty\n");
    }
    printf("%s", result);
    return 0;
}
