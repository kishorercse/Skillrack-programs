/*
The function/method everyTwoDigitsToInteger accepts an argument N representing an integer value.

The function/method everyTwoDigitsToInteger must form integer values based on the following condition.
- For every two digits D1 and D2 in the integer N, the program must form a new integer by using the digits from D1 to D2.
Then the function must return an integer representing the sum of the resulting integers.

Your task is to implement the function everyTwoDigitsToInteger so that the program runs successfully.

IMPORTANT: Do not write the main() function as it is already defined.

Example Input/Output 1:
Input:
2514

Output:
57900

Explanation:
Here N = 2514.
1st integer: 2345 (2 to 5).
2nd integer: 54321 (5 to 1).
3rd integer: 1234 (1 to 4).
2345 + 54321 + 1234 = 57900.

Example Input/Output 2:
Input:
90109

Output:
10000000010

Explanation:
Here N = 90109.
1st integer: 9876543210 (9 to 0).
2nd integer: 01 -> 1 (0 to 1).
3rd integer: 10 (1 to 0).
4th integer: 0123456789 -> 123456789 (0 to 9).
9876543210 + 1 + 10 + 123456789 = 10000000010.
*/
#include <stdio.h>
#include <stdlib.h>

long long int everyTwoDigitsToInteger(int N)
{
    long long int sum=0;
    while(N>9)
    {
        int a=N/10%10, b=N%10;
        long long int t=0;
        if (a<=b)
        {
            while(a<=b)
            {
                t=t*10+a;
                a++;
            }
        }
        else
        {
            while(a>=b)
            {
                t=t*10+a;
                a--;
            }
        }
        N/=10;
        sum+=t;
    }
    return sum;
}

int main()
{
    int N;
    scanf("%d", &N);
    printf("%lld", everyTwoDigitsToInteger(N));
    return 0;
}
