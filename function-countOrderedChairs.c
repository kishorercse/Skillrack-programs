/*
The function/method countOrderedChairs accepts an argument str representing a string value. The string str contains only unique lower case alphabets. Each alphabet in the string
str represents a chair.
The function/method countOrderedChairs must return an integer representing the number of chairs arranged in alphabetical order with respect to their positions. The order of the
26 chairs must be abcdefghijklmnopqrstuvwxyz.

Your task is to implement the function countOrderedChairs so that the program runs successfully.

IMPORTANT: Do not write the main() function as it is already defined.

Example Input/Output 1:
Input:
abcdwxyz

Output:
4

Explanation:
Only the first 4 chairs(a, b, c and d) are arranged in alphabetical order with respect to their positions.
The position of the chair w must be 23.
The position of the chair x must be 24.
The position of the chair y must be 25.
The position of the chair z must be 26.

Example Input/Output 2:
Input:
abcxyzghij

Output:
7

Explanation:
The chairs a, b, c, g, h, i and j are arranged in alphabetical order with respect to their positions.
*/
#include <stdio.h>
#include <stdlib.h>

int countOrderedChairs(char *str)
{
    int count=0, ch='a';
    for(int i=0;str[i];i++)
    {
        if (str[i]==ch)
            count++;
        ch++;
    }
    return count;
}

int main()
{
    char str[27];
    scanf("%s", str);
    printf("%d", countOrderedChairs(str));
    return 0;
}
