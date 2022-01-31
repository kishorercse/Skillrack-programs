/*
The function/method getPositionDigitsSum accepts two arguments SIZE and arr. The integer SIZE represents the size of the integer array arr.

The function/method getPositionDigitsSum must return an array containing the sum of digits in the same positions among the given N integers.

Your task is to implement the function getPositionDigitsSum so that the program runs successfully.

The following structure is used to represent the boundedArray and is already defined in the default code (Do not write this definition again in your code).
typedef struct BoundedArray
{
    int SIZE;
    int *arr;
} boundedArray;

IMPORTANT: Do not write the main() function as it is already defined.

Example Input/Output 1:
Input:
4
1247 204 69 36548

Output:
3 7 9 14 28
 
Explanation:
7 + 4 + 9 + 8 = 28 (ones).
4 + 0 + 6 + 4 = 14 (tens).
2 + 2 + 5 = 9 (hundreds).
1 + 6 = 7 (thousands).
3 = 3 (ten thousands).

Example Input/Output 2:
Input:
3
5680 600 90000

Output:
9 5 12 8 0
*/
#include <stdio.h>
#include <stdlib.h>

typedef struct BoundedArray
{
    int SIZE;
    int *arr;
} boundedArray;

boundedArray *getPositionDigitsSum(int SIZE, int *arr)
{
    boundedArray *ba=malloc(sizeof(boundedArray));
    ba->SIZE=0;
    ba->arr=malloc(sizeof(int)*8);
    while (1)
    {
        int f=0;
        ba->arr[ba->SIZE]=0;
        for(int i=0;i<SIZE;i++)
        {
            if (arr[i]!=0)
                f=1;
            ba->arr[ba->SIZE]+=arr[i]%10;
            arr[i]/=10;
        }
        if (f==0)
            break;
        else
            ba->SIZE++;
    }
    int i=0, j=ba->SIZE-1;
    while(i<j)
    {
        int t=ba->arr[i];
        ba->arr[i]=ba->arr[j];
        ba->arr[j]=t;
        i++;
        j--;
    }
    return ba;
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
    boundedArray *bArr = getPositionDigitsSum(N, arr);
    if(bArr == NULL || bArr->arr == NULL || bArr->arr == arr)
    {
        printf("Array is not formed\n");
    }
    if(bArr->SIZE <= 0)
    {
        printf("Invalid size for the array\n");
    }
    for(int index = 0; index < bArr->SIZE; index++)
    {
        printf("%d ", bArr->arr[index]);
    }
    return 0;
}
