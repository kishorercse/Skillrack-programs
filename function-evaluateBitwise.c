/*
The function/method evaluateBitwise accepts three arguments str1, str2 and ch. str1 and str2 represent two string values containing a's and b's. ch represents a bitwise operator 
('&', '|' or '^'). The function/method evaluateBitwise must perform the specified bitwise operation between the given two string values by considering a's as 0's and b's as 1's. 
Then the function must return a new string value representing the result of the bitwise operation. 

Note: Both str1 and str2 have an equal length.
Your task is to implement the function evaluateBitwise so that the program runs successfully.

Boundary Condition(s): 
1 <= Length of str1 and str2 <= 1000

Example Input/Output 1:
Input:
babaab 
abbaba 
&

Output: 
aabaaa 

Explanation:
In the bitwise AND operation, 
a & a = a 
a & b = a 
b & a = a 
b & b = b 
babaab & abbaba = aabaaa.

Example Input/Output 2:
Input: 
babaab 
abbaba 
|

Output: 
bbbabb 

Example Input/Output 3: 
Input: 
babaab 
abbaba
^ 

Output:
bbaabb 
*/
#include <stdio.h> 
#include <stdlib.h>
char* evaluateBitwise(char str1[], char str2[], char ch)
{
    static char s[1001];
    for(int i=0;str1[i];i++){
        int a=(str1[i]=='a')?0:1, b=(str2[i]=='a')?0:1, res;
        if (ch=='&')
            res=a&b;
        else if(ch=='|')
            res=a|b;
        else
            res=a^b;
        s[i]=(res==0)?'a':'b';
    }
    return s;
}
int main() 
{
  char str1[1001], str2[1001];
  char ch;
  scanf("%s\n%s\n%c", str1, str2, &ch);
  char *result = evaluateBitwise(str1, str2, ch);
  if(str1 == result || str2 == result)
  {
    printf("New string is not formed\n");
  } 
  if(result[0] == '\0' || result[1] == ' ') 
  {
    printf("String is empty\n");
  }
  printf("%s", result); 
  return 0; 
}
