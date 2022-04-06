/*
The function/method sortBasedOnDigits accepts two arguments SIZE and arr. The integer SIZE represents the size of the integer array arr.

The function/method sortBasedOnDigits must sort the integers in the given array based on digits starting from the most significant digit.

IMPORTANT: Do not write the main() function as it is already defined.

Example Input/Output 1:
Input:
6
200 2 22 32 3 4

Output:
2 200 22 3 32 4

Explanation:
Here N=6 and the given 6 integers are 200 2 22 32 3 4.
After sorting the given array based on digits starting from the most significant digit, the array becomes 2 200 22 3 32 4.

Example Input/Output 2:
Input:
5
124 1201 204 230 104

Output:
104 1201 124 204 230
*/

#include <stdio.h>
#include <stdlib.h>

int digCmp(int a, int b) 
{
    int x=pow(10,(int)log10(a)), y=pow(10,(int)log10(b));
    while(x>=1 && y>=1) 
    {
        int d1=(a/x)%10, d2=(b/y)%10;
        if (d1>d2)
        {
            return 1;
        }
        else if (d1<d2)
        {
            return 0;
        }
        x/=10;
        y/=10;
    }
    if (x!=0 && y==0)
        return 1;
    return 0;
}
void sortBasedOnDigits(int SIZE, int *arr)
{
    for(int i=0;i<SIZE-1;i++) {
        for(int j=0;j<SIZE-i-1;j++) {
            if (digCmp(arr[j],arr[j+1])==1) {
                int t=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=t;
            }
        }
    }

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
    sortBasedOnDigits(N, arr);
    for(int index = 0; index < N; index++)
    {
        printf("%d ", arr[index]);
    }
    return 0;
}
