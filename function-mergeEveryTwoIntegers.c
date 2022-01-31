/*
The function/method mergeEveryTwoIntegers accepts two arguments - SIZE and arr. The integer SIZE represents the size of the integer array arr.

The function/method mergeEveryTwoIntegers must merge every two integers X and Y in the array based on the following conditions.
- The integers X and Y can be merged only if the sum of the last digit of X and the first digit of Y is less than or equal to 9.
- If it is not possible to merge X and Y, then the function must keep the two integers as they are.
Finally, the function must return the resulting integers as an array.

Note: The size of the given array is always even.

Your task is to implement the function mergeEveryTwoIntegers so that the program runs successfully.

The following structure is used to represent the boundedArray and is already defined in the default code (Do not write this definition again in your code).
typedef struct BoundedArray
{
    int SIZE;
    long long int *arr;
} boundedArray;

IMPORTANT: Do not write the main() function as it is already defined.

Example Input/Output 1:
Input:
6
124 182 606 504 255 42

Output:
12582 606 504 2592

Explanation:
124 182 -> 12(4+1)82 -> 12582
606 504 -> Cannot be merged -> 606 504
255 42 -> 25(5+4)2 -> 2592

Example Input/Output 2:
Input:
4
1325564 8075456 4521210 5987655

Output:
1325564 8075456 4521215987655

Example Input/Output 3:
Input:
8
8991 800 8250 7006 16 543 4002 6372

Output:
899900 8257006 16 543 4008372
*/
#include <stdio.h>
#include <stdlib.h>

typedef struct BoundedArray
{
    int SIZE;
    long long int *arr;
} boundedArray;

boundedArray* mergeEveryTwoIntegers(int SIZE, int *arr)
{
    boundedArray *b=malloc(sizeof(boundedArray));
    b->SIZE=0;
    b->arr=malloc(sizeof(long long int)*SIZE);
    for(int i=0;i<SIZE;i+=2)
    {
        int x=arr[i]%10, y=arr[i+1], pw=1, yRem=0;
        while(y>9)
        {
            yRem=y%10*pw+yRem;
            y/=10;
            pw*=10;
        }
        if (x+y<=9)
        {
            b->arr[b->SIZE++]=(long long int)(arr[i]/10*10+(x+y))*pw+yRem;
        }
        else
        {
            b->arr[b->SIZE++]=arr[i];
            b->arr[b->SIZE++]=arr[i+1];
        }
        
    }
    return b;

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
    boundedArray *bArr = mergeEveryTwoIntegers(N, arr);
    for(int index = 0; index < bArr->SIZE; index++)
    {
        printf("%lld ", bArr->arr[index]);
    }
    return 0;
}
