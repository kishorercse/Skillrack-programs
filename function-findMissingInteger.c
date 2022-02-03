/*
The function/method findMissingInteger accepts three arguments R, C and matrix. The integers R and C represent the size of the integer matrix. The given matrix contains a 
series of R*C consecutive positive integers but exactly one integer is missing. The missing integer is denoted by -1 in the matrix.

The function/method findMissingInteger must find the missing integer and replace -1 with the missing integer in the matrix.

Note: The first and last values in the series of R*C consecutive positive integers are always present in the matrix.

Your task is to implement the function findMissingInteger so that the program runs successfully.

IMPORTANT: Do not implement the main() function as it is already defined.

Example Input/Output 1:
Input:
3 3
2 9 7
6 3 1
-1 5 8

Output:
2 9 7
6 3 1
4 5 8

Explanation:
Here R = 3 and C = 3.
The matrix contains all the positive integers from 1 to 9, but 4 is missing.
Hence -1 is replaced with 4.
2 9 7
6 3 1
4 5 8

Example Input/Output 2:
Input:
5 4
30 23 21 28
29 19 11 25
22 13 15 -1
20 17 18 14
26 24 16 12

Output:
30 23 21 28
29 19 11 25
22 13 15 27
20 17 18 14
26 24 16 12
*/
#include <stdio.h>
#include <stdlib.h>

void findMissingInteger(int R, int C, int matrix[R][C])
{
    int min=9999999, t=R*C, row, col, arr[t];
    memset(arr,0,t*sizeof(int));
    for(int i=0;i<R;i++)
    {
        for(int j=0;j<C;j++)
        {
            if (matrix[i][j]==-1)
            {
                row=i;
                col=j;
            }
            else if (matrix[i][j]<min)
            {
                min=matrix[i][j];
            }
        }
    }
    for(int i=0;i<R;i++)
    {
        for(int j=0;j<C;j++)
        {
            if (matrix[i][j]!=-1)
            {
                arr[matrix[i][j]-min]=1;
            }
        }
    }
    for(int i=0;i<t;i++)
    {
        if (arr[i]==0)
        {
            matrix[row][col]=i+min;
            return;
        }
    }
    

}

int main()
{
    int R, C;
    scanf("%d %d", &R, &C);
    int matrix[R][C];
    for(int row = 0; row < R; row++)
    {
        for(int col = 0; col < C; col++)
        {
            scanf("%d", &matrix[row][col]);
        }
    }
    findMissingInteger(R, C, matrix);
    for(int row = 0; row < R; row++)
    {
        for(int col = 0; col < C; col++)
        {
            printf("%d ", matrix[row][col]);
        }
        printf("\n");
    }
    return 0;
}
