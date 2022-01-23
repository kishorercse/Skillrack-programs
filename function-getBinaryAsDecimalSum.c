/*
The function/method getBinaryAsDecimalSum accepts two arguments SIZE and arr. The integer SIZE represents the size of the integer array. The number of bits in the binary 
representation of each integer in the array is always less than or equal to 8.

The function/method getBinaryAsDecimalSum must find the binary representation of each integer in the given array. Then the function must return an integer representing the sum 
of the binary values by considering them as decimal numbers.

Your task is to implement the function getBinaryAsDecimalSum so that the program runs successfully.

IMPORTANT: Do not write the main() function as it is already defined.

Example Input/Output 1:
Input:
4
10 5 7 8

Output:
2222

Explanation:
Here N = 4.
10 -> 1010
5 -> 101
7 -> 111
8 -> 1000
1010+101+111+1000 = 2222.

Example Input/Output 2:
Input:
9
1 2 3 4 5 6 7 8 9

Output:
2445
*/
#include <stdio.h>
#include <stdlib.h>

int binary(int n)
{
    if (n==0)
        return 0;
    return binary(n/2)*10+n%2;
}
int getBinaryAsDecimalSum(int SIZE, int *arr)
{
    int sum=0;
    for(int i=0;i<SIZE;i++)
    {
        sum+=binary(arr[i]);
    }
    return sum;   
}

int main()
{
    int N;
    scanf("%d", &N);
    int arr[N];
    for(int index = 0; index < N; index++)
    {
        scanf("%d", &arr[index]);
    }
    printf("%d", getBinaryAsDecimalSum(N, arr));
    return 0;
}
