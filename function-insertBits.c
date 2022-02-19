/*
The function/method insertBits accepts two arguments X and Y representing two integer values.

The function/method insertBits must insert all the bits of Y after the last set bit in X. Then the function must return an integer representing the revised value of X.

Your task is to implement the function insertBits so that the program runs successfully.

IMPORTANT: Do not write the main() function as it is already defined.

Example Input/Output 1:
Input:
10 14

Output:
188

Explanation:
10 -> 1010
14 -> 1110
After inserting 1110 after the last set bit in 1010, the binary representation of X becomes 10111100.
The decimal equivalent of 10111100 is 188.

Example Input/Output 2:
Input:
152 9

Output:
2504

Explanation:
152 -> 10011000
9 -> 1001
After inserting 1001 after the last set bit in 10011000, the binary representation of X becomes 100111001000.
The decimal equivalent of 100111001000 is 2504.
*/
#include <stdio.h>
#include <stdlib.h>

int insertBits(int X, int Y)
{
    int binaryLen=log2(Y)+1, lastZeros=0;
    while(X>0)
    {
        if (X&1)
        {
            X<<=binaryLen;
            X|=Y;
            X<<=lastZeros;
            return X;
        }
        X>>=1;
        lastZeros+=1;
    }
}

int main()
{
    int X, Y;
    scanf("%d %d", &X, &Y);
    printf("%d", insertBits(X, Y));
    return 0;
}
