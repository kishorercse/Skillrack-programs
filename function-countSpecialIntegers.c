/*
The function/method countSpecialIntegers accepts four arguments L, R, A and B. The first two arguments L, R represent a range of integer values. The next two arguments A, B 
represent two nonzero digits.

The function/method countSpecialIntegers must return an integer representing the count of special integers present in the range from L to R. A special integer is an integer 
divisible by both A and B, and contains the digits A and B at least once.

Your task is to implement the function countSpecialIntegers so that the program runs successfully.

IMPORTANT: Do not write the main() function as it is already defined.

Boundary Condition(s):
10 <= L < R <= 10^6
1 <= A, B <= 9

Example Input/Output 1:
Input:
1800 2500
3 6

Output:
7

Explanation:
Here L = 1800, R = 2500, A = 3 and B = 6.
There are 7 special integers present in the range from 1800 to 2500.
1836 2136 2316 2346 2364 2376 2436

Example Input/Output 2:
Input:
5000 9999
4 7

Output:
16

Explanation:
Here L = 5000, R = 9999, A = 4 and B = 7.
There are 16 special integers present in the range from 5000 to 9999.
5740 6748 7084 7140 7224 7364 7420 7448 7476 7504 7644 7784 7840 7924 8764 9744
*/
#include <stdio.h>
#include <stdlib.h>

int gcd(int a, int b)
{
    if (b==0)
        return a;
    return gcd(b,a%b);
}
int countSpecialIntegers(int L, int R, int A, int B)
{
    int d=A*B/gcd(A,B), count=0;
    if (L%d!=0)
        L+=d-L%d;
    while(L<=R)
    {
        int temp=L, f1=0, f2=0;
        while (temp>0)
        {
            int r=temp%10;
            if (r==A)
                f1=1;
            else if (r==B)
                f2=1;
            if (f1==1 && f2==1)
            {
                count++;
                break;
            }
            temp/=10;
        }
        L+=d;
    }
    return count;

}

int main()
{
    int L, R, A, B;
    scanf("%d %d %d %d", &L, &R, &A, &B);
    printf("%d", countSpecialIntegers(L, R, A, B));
    return 0;
}
