/*
The function/method sortSubstrings accepts two arguments str and K. The str represents a string value whose length is always divisible by the integer K.

The function/method sortSubstrings must split the given string into substrings of equal length K. Then the function must sort the substrings and return them.

Your task is to implement the function sortSubstrings so that the program runs successfully.

The following structure is used to represent the boundedArray and is already defined in the default code (Do not write this definition again in your code).
typedef struct BoundedArray
{
    int SIZE;
    char **words;
} boundedArray;

IMPORTANT: Do not write the main() function as it is already defined.

Example Input/Output 1:
Input:
skillrack
3

Output:
ack llr ski

Explanation:
Here K = 3.
After dividing the given string skillrack into substrings of length 3, the substrings are ski, llr and ack.
So they are printed in sorted order.

Example Input/Output 2:
Input:
internationalairport
4

Output:
inte iona lair port rnat
*/
#include <stdio.h>
#include <stdlib.h>

typedef struct BoundedArray
{
    int SIZE;
    char **words;
} boundedArray;

boundedArray* sortSubstrings(char *str, int K)
{
    int len=strlen(str), n=len/K;
    boundedArray *ba=malloc(sizeof(boundedArray));
    ba->words=malloc(sizeof(char*)*n);
    ba->SIZE=0;
    for(int i=0;i<len;i+=K)
    {
        ba->words[ba->SIZE]=malloc(sizeof(char)*(K+1));
        for(int j=0;j<K;j++)
        {
            ba->words[ba->SIZE][j]=str[i+j];
        }
        ba->SIZE++;
    }
    for(int i=0;i<n-1;i++)
    {
        for(int j=0;j<n-i-1;j++)
        {
            if (strcmp(ba->words[j],ba->words[j+1])>0)
            {
                char temp[K+1];
                strcpy(temp,ba->words[j]);
                strcpy(ba->words[j],ba->words[j+1]);
                strcpy(ba->words[j+1],temp);
            }
        }
    }
    return ba;
}

int main()
{
    char str[101];
    int K;
    scanf("%s\n%d", str, &K);
    boundedArray *bArr = sortSubstrings(str, K);
    if(bArr == NULL || bArr->SIZE == 0 || bArr->words == NULL
            || bArr->words[0][0] == '\0' || bArr->words[0][0] == ' ')
    {
        printf("String values are not formed\n");
    }
    for(int index = 0; index < bArr->SIZE; index++)
    {
        printf("%s ", bArr->words[index]);
    }
    return 0;
}
