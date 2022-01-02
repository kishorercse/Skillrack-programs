/*
The function/method concatOrAdd accepts two arguments str1 and str2 representing two string values. The values of both str1 and str2 can be integers or floating point
values or words.

The function/method concatOrAdd must return a string based on the following conditions.
- If both str1 and str2 are integers, then the function return their sum as a string.
- If both str1 and str2 are floating point values, then the function return their sum with the precision up to 2 decimal places as a string.
- Otherwise, the function must concatenate both the words and return the concatenated string.

Your task is to implement the function concatOrAdd so that the program runs successfully.

IMPORTANT: Do not write the main() function as it is already defined.

Example Input/Output 1:
Input:
300 450

Output:
750

Explanation:
Both the values are integer values.
So their sum is printed.

Example Input/Output 2:
Input:
15.52 123.676

Output:
139.20

Explanation:
Both the values are floating point values.
So their sum is printed with the precision up to 2 decimal places.

Example Input/Output 3:
Input:
Skill Rack

Output:
SkillRack

Explanation:
Both the values are string values(words).
So they are concatenated and printed as the output.
*/
#include <stdio.h>
#include <stdlib.h>

int isFloat(char *s)
{
    for(int i=0;s[i];i++)
        if (s[i]=='.')
            return 1;
    return 0;
}
char* concatOrAdd(char *str1, char *str2)
{
    static char res[101];
    if (isalpha(str1[0]))
        sprintf(res,"%s%s",str1,str2);
    else
    {
        double a,b;
        sscanf(str1,"%lf",&a);
        sscanf(str2,"%lf",&b);
        if(isFloat(str1))
            sprintf(res,"%.2lf",a+b);
        else
            sprintf(res,"%.0lf",a+b);
    }
    return res;

}

#include <stdio.h>
#include <stdlib.h>

int main()
{
    char str1[101], str2[101];
    scanf("%s %s", str1, str2);
    char *str = concatOrAdd(str1, str2);
    if(str == str1 || str == str2)
    {
        printf("New string is not formed\n");
    }
    if(str[0] == '\0' || str[0] == ' ')
    {
        printf("String is empty\n");
    }
    printf("%s", str);
    return 0;
}
