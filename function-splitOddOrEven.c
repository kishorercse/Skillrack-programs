/*
The function/method splitOddOrEven accepts two arguments SIZE and arr. The integer SIZE represents the size of the integer array arr. Each integer in the array contains an even number of digits.

The function/method splitOddOrEven must split each integer X in the array based on the following conditions.
- If both the halves of the integer X are odd or even, then the function must split the integer X into two equal halves. Else the function must keep the integer as it is.
Finally, the function must return an array containing the resulting integers in sorted order.

Note: Consider 0 as an even integer.

Your task is to define the function splitOddOrEven so that the program runs successfully.

The following structure is used to represent the boundedArray and is already defined in the default code (Do not write this definition again in your code).
typedef struct BoundedArray
{
    int SIZE;
    int *arr;
} boundedArray;

IMPORTANT: Do not write the main() function as it is already defined.

Boundary Condition(s):
10 <= Each integer value < 10^8

Example Input/Output 1:
Input:
4
5167 42 7249 781543

Output:
2 4 51 67 543 781 7249

Explanation:
5167 -> 51 and 67 (Both are odd integers)
42 -> 4 and 2 (Both are even integer)
7249 -> 72 and 49 (72 is even but 49 is odd). So 7249 remains the same.
781543 -> 781 and 543 (Both are odd integers)
After sorting the resulting integers, the integers become
2 4 51 67 543 781 7249

Example Input/Output 2:
Input:
5
122399 1010 4004 55 500500

Output:
4 5 5 10 10 40 500 500 122399
*/
#include <stdio.h>
#include <stdlib.h>

typedef struct BoundedArray
{
    int SIZE;
    int *arr;
} boundedArray;

boundedArray* splitOddOrEven(int SIZE, int *arr)
{
    boundedArray *ba=malloc(sizeof(boundedArray));
    ba->SIZE=0;
    ba->arr=malloc(sizeof(int)*SIZE*2);
    for(int i=0;i<SIZE;i++)
    {
        int n=(int)ceil(log10(arr[i]))/2;
        int p=pow(10,n), a=arr[i]/p, b=arr[i]%p;
        if (arr[i]!=10 && a%2==b%2)
        {
            ba->arr[ba->SIZE++]=a;
            ba->arr[ba->SIZE++]=b;
        }
        else
        {
            ba->arr[ba->SIZE++]=arr[i];
        }
    }
    for(int i=0;i<ba->SIZE-1;i++)
    {
        for(int j=0;j<ba->SIZE-i-1;j++)
        {
            if (ba->arr[j]>ba->arr[j+1])
            {
                int temp=ba->arr[j];
                ba->arr[j]=ba->arr[j+1];
                ba->arr[j+1]=temp;
            }
        }
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
    boundedArray *bArr = splitOddOrEven(N, arr);
    if(bArr == NULL)
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
