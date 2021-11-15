/*
The function/method concatSameValues accepts two arguments SIZE and arr. The integer SIZE represents the size of the integer array arr. The function/method concatSameValues must
form an integer array based on the following conditions. 
- If two integers are equal in the given array, then the function must concatenate those integers as a single integer. 
- After concatenating all possible integers, then the function must sort the array in ascending order. 
Finally, the function must return the sorted array. 

The following structure is used to represent the boundedArray and is already defined in the default code (Do not write this definition again in your code). 
typedef struct BoundedArray 
{
  int SIZE; int *arr; 
} boundedArray;

IMPORTANT: Do not write the main() function as it is already defined. 

Boundary Condition(s): 
1 <= Each integer value <= 9999

Example Input/Output 1: 
Input:
7
10 50 10 50 200 15 10 

Output:
10 15 200 1010 5050

Explanation: 
10 and 10 are concatenated as 1010. 
50 and 50 are concatenated as 5050. 
So the integers [1010, 5050, 200, 15, 10] are sorted and printed as the output.

Example Input/Output 2:
Input: 
12
980 1 4 5 5 2 3 3 3 1 4 980 

Output:
2 3 11 33 44 55 980980 

Example Input/Output 3:
Input:
5
11 11 1 1 1111 

Output:
11 1111 1111
*/
#include <stdio.h>
#include <stdlib.h>

typedef struct BoundedArray
{
  int SIZE; 
  int *arr;
} boundedArray;

void sort(int SIZE,int *arr)
{
    for(int i=0;i<SIZE-1;i++)
    {
        for(int j=0;j<SIZE-i-1;j++)
        {
            if(arr[j]>arr[j+1])
            {
                int t=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=t;
            }
        }
    }
}
boundedArray* concatSameValues(int SIZE, int *arr)
{
    sort(SIZE,arr);
    boundedArray *bArr=(boundedArray*)malloc(sizeof(boundedArray));
    bArr->arr=(int*)malloc(sizeof(int)*SIZE);
    bArr->SIZE=0;
    int count=0;
    char str[10];
    for(int i=1;i<SIZE;i++){
        if (arr[i]==arr[i-1])
        {
            sprintf(str,"%d%d",arr[i],arr[i]);
            arr[i]=-1;
            bArr->arr[bArr->SIZE++]=atoi(str);
            i++;
        }
        else
        {
            bArr->arr[bArr->SIZE++]=arr[i-1];
        }
    }
    if (arr[SIZE-1]!=-1)
        bArr->arr[bArr->SIZE++]=arr[SIZE-1];
    sort(bArr->SIZE,bArr->arr);
    return bArr;
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
  boundedArray *bArr = concatSameValues(N, arr);
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
