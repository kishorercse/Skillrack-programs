/*
The function/method findNextWordPosition accepts an argument str. The string str contains multiple words.

The function/method findNextWordPosition must print the output based on the following conditions.
- For each word in the given string, the function must print the position of the next word with the same last character.
- Consider the words in circular fashion when finding the next word with the same last character.

Your task is to implement the function findNextWordPosition so that the program runs successfully.

IMPORTANT: Do not write the main() function as it is already defined.

Example Input/Output 1:
Input:
pen table desk admin junction rock

Output:
4 2 6 5 1 3

Explanation:
pen -> admin (4th word)
table -> table (2nd word)
desk -> rock (6th word)
admin -> junction (5th word)
junction -> pen (1st word)
rock -> desk (3rd word)
Hence the output is
4 2 6 5 1 3

Example Input/Output 2:
Input:
one two three four five

Output:
3 2 5 4 1
*/
#include <stdio.h>
#include <stdlib.h>

void findNextWordPosition(char *str)
{
    char res[30][30];
    int ind=0, ptr=0, t;
    while(str[ptr] && sscanf(str+ptr,"%s %n",res[ind++],&t))
    {
        ptr+=t;
    }
    for(int i=0;i<ind;i++)
    {
        char ch=res[i][strlen(res[i])-1];
        for(int j=(i+1)%ind;;j=(j+1)%ind)
        {
            if (ch==res[j][strlen(res[j])-1])
            {
                printf("%d ",j+1);
                break;
            }
        }
    }

}
int main()
{
    char str[101];
    scanf("%[^\n\r]", str);
    findNextWordPosition(str);
    return 0;
}
