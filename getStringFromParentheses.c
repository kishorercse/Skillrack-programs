/*
The function/method getStringFromParentheses accepts an argument str representing a string value. The string str contains alphabets and a pair of parentheses.

The function/method getStringFromParentheses must return a string containing all the characters between the open parenthesis and the close parenthesis in the given string. 
If there are no characters between the pair of parentheses, then the function must return -1 as a string value. Consider string in circular fashion when finding the characters
between the open parenthesis and the close parenthesis.

Your task is to implement the function getStringFromParentheses so that it passes all the test cases.

Example Input/Output 1:
Input:
abcd(SkillRack)pqrs

Output:
SkillRack

Explanation:
Here the given string value is abcd(SkillRack)pqrs.
All the characters between the pair of parentheses are SkillRack.
So SkillRack is printed as the output.

Example Input/Output 2:
Input:
abcdef)ghij(klmno

Output:
klmnoabcdef

Example Input/Output 3:
Input:
bank()account

Output:
-1

Example Input/Output 4:
Input:
)donkey(

Output:
-1
*/
#include <stdio.h>
#include <stdlib.h>

char* getStringFromParentheses(char *str)
{
    static char res[101];
    int resIndex=0, start, len=strlen(str);
    for(int i=0;str[i]!='\0';i++)
    {
        if (str[i]=='(')
        {
            start=(i+1)%len;
            break;
        }
    }
    while(str[start]!=')')
    {
        res[resIndex++]=str[start];
        start=(start+1)%len;
    }
    if (resIndex==0)
        return "-1";
    return res;
}

int main() 
{
  char str[101];
  scanf("%s", str);
  char *newStr = getStringFromParentheses(str);
  if(newStr == NULL || newStr == str) 
  {
    printf("New string is not formed\n"); 
  }
  if(newStr[0] == '\0' || newStr[0] == ' ') 
  {
    printf("String is empty\n"); 
  }
  printf("%s", newStr); 
  return 0; 
}
