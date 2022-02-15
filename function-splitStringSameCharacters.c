/*
The function/method splitStringSameCharacters accept an argument str representing a string value.

The function/method splitStringSameCharacters must split the given string at which a character occurs exactly twice consecutively. Then the function must print the 
resulting words as the output.

Your task is to implement the function splitStringSameCharacters so that the program runs successfully.

IMPORTANT: Do not write the main() function as it is already defined.

Example Input/Output 1:
Input:
moonlighttiger

Output:
mo onlight tiger

Explanation:
Here the given string is moonlighttiger.
The characters 'o' and 't' occur exactly twice consecutively.
After splitting the string at which the characters occur exactly twice consecutively, the string becomes
mo onlight tiger

Example Input/Output 2:
Input:
aabbbccddddeeeeeeffgggg

Output:
a abbbc cddddeeeeeef fgggg
*/
#include <stdio.h>
#include <stdlib.h>

void splitStringSameCharacters(char *str)
{
    char res[1001], ch=str[0];
    int ind=0,count=1,i;
    for (i=1;str[i]!='\0';i++)
    {
        if (str[i]==ch)
        {
            count++;
        }
        else
        {
            if (count==2)
            {
                res[ind]='\0';
                printf("%s ",res);
                ind=0;
                res[0]=ch;
                res[1]='\0';
            }
            ch=str[i];
            count=1;
        }
        res[ind++]=str[i-1];
    }
    res[ind]='\0';
    if (count==2)
        printf("%s %c",res,str[i-1]);
    else
        printf("%s%c",res,str[i-1]);

}

int main()
{
    char str[1001];
    scanf("%s", str);
    splitStringSameCharacters(str);
    return 0;
}
