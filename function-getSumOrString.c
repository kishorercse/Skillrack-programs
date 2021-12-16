/*
The function/method getSumOrString accepts an argument str. The string str contains the integer values separated by a space or the alphabets separated by a space.

The function/method getSumOrString must return a string value based on the following conditions.
- If the string str contains integers, then the function must return their sum as a string.
- Else the function must form a string by concatenating the alphabets and return the string.

Your task is to implement the function getSumOrString so that the program runs successfully.

IMPORTANT: Do not write the main() function as it is already defined.

Example Input/Output 1:
Input:
12 45 7 -200 6100

Output:
5964

Explanation:
The given string contains the integer values separated by a space.
12 + 45 + 7 + (-200) + 6100 = 5964.

Example Input/Output 2:
Input:
S k i l l R a c k

Output:
SkillRack

Explanation:
The given string contains the alphabets separated by a space.
S k i l l R a c k -> SkillRack.
*/
#include <stdio.h>
#include <stdlib.h>

char* getSumOrString(char *str)
{
    static char res[101];
    int len=strlen(str);
    if (isdigit(str[0]) || str[0]=='-')
    {
        int ptr=0, sum=0, n, t;
        while(ptr<len && sscanf(str+ptr,"%d %n",&n,&t)==1)
        {
            sum+=n;
            ptr+=t;
        }
        sprintf(res,"%d",sum);
    }
    else
    {
        int ptr=0, ind=0;
        char ch;
        while (ptr<len && sscanf(str+ptr,"%c",&ch)==1)
        {
            res[ind++]=ch;
            ptr+=2;
        }
    }
    return res;
    
}
int main()
{
    char str[101];
    scanf("%[^\n\r]", str);
    char *result = getSumOrString(str);
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
