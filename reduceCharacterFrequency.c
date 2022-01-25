/*
The function/method reduceCharacterFrequency accepts two arguments str and K representing a string value and an integer value respectively.

The function/method reduceCharacterFrequency must remove the characters after their Kth occurrence in the given string(from left to right). Then the function must return the 
revised string as a new string.

Your task is to implement the function reduceCharacterFrequency so that the program runs successfully.

IMPORTANT: Do not write the main() function as it is already defined.

Example Input/Output 1:
Input:
aabbabcdccbab
2

Output:
aabbcdc

Explanation:
Here the given string is aabbabcdccbab and K=2.
After removing the characters that occur more than 2 times in the given string, the string becomes aabbcdc.

Example Input/Output 2:
Input:
TOOLONGTOURtoolongtour
2

Output:
TOOLNGTURtoolngtur
*/
#include <stdio.h>
#include <stdlib.h>

char* reduceCharacterFrequency(char *str, int K)
{
    int ind=0, count[128]={0};
    static char res[1001];
    for(int i=0;str[i]!='\0';i++)
    {
        if (count[str[i]]<K)
            res[ind++]=str[i];
        count[str[i]]++;
    }
    return res;

}
int main()
{
    char str[1001];
    int K;
    scanf("%s\n%d", str, &K);
    char *newStr = reduceCharacterFrequency(str, K);
    if(newStr == str || newStr == NULL)
    {
        printf("New String is not formed\n");
    }
    if(newStr[0] == ' ' || newStr[0] == '\0')
    {
        printf("String is empty\n");
    }
    printf("%s", newStr);
    return 0;
}
