/*
The function/method findMissingBit accepts two arguments str and X. The string str represents the binary representation of the integer X but exactly one bit is missing.

The function/method findMissingBit must find the missing bit in the string S and return the missing bit as an integer value.

Your task is to implement the function findMissingBit so that the program runs successfully.

IMPORTANT: Do not write the main() function as it is already defined.

Example Input/Output 1:
Input:
10111
45

Output:
0

Explanation:
The string S = "10111".
The binary representation of 45 is 101101.
The missing bit in the string S is 0, which is printed as the output.

Example Input/Output 2:
Input:
111
15

Output:
1
*/
#include <stdio.h>
#include <stdlib.h>

int findMissingBit(char *str, int X)
{
    int count[2];
    while(X>0)
    {
        count[X%2]++;
        X/=2;
    }
    for(int i=0;str[i];i++)
    {
        count[str[i]-'0']--;
    }
    if (count[0]==1)
        return 0;
    else
        return 1;
}
int main()
{
    char str[101];
    int X;
    scanf("%s\n%d", str, &X);
    printf("%d", findMissingBit(str, X));
    return 0;
}
