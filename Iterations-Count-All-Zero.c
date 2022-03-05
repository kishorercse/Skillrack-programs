/*
The program must accept an integer matrix of size R*C and an integer K as the input. For each occurrence of K in the matrix, the program must replace K and all the adjacent 
non-zero cell values with zero which are to it's left, right, top and bottom. The program must repeat the process untill all the values become zero. The program must print how
many times the process has to be performed to convert all the cell values to zero.

Boundary Condition(s):
2 <= R, C <= 50

Input Format:
The first line contains R and C separated by a space.
The next R lines, each containing C integers separated by a space.
The (R+2)nd line contains K.

Output Format:
The first line contains an integer representing the number of times the above process has to be performed to convert all the cell values to zero.

Example Input/Output 1:
Input:
5 5
5 6 0 5 6
1 8 8 0 2
5 5 5 0 6
4 5 5 5 0
8 8 8 8 8
6

Output:
2

Explanation:
After performing the process for the first occurrence of 6, the matrix becomes
0 0 0 5 6
0 0 0 0 2
0 0 0 0 6
0 0 0 0 0
0 0 0 0 0
After performing the process for the second occurrence of 6, the matrix becomes
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
Now, all the cell values in the matrix become zero.
Hence the output is 2

Example Input/Output 2:
Input:
4 5
5 0 0 5 6
1 0 8 1 0
0 5 0 0 6
4 5 0 5 2
5

Output:
4
*/
#include<stdio.h>
#include<stdlib.h>
int R, C;

void traverse(int matrix[R][C], int row, int col)
{
    if (row<0 || row>=R || col<0 || col>=C || matrix[row][col]==0)
    {
        return;
    }
    matrix[row][col]=0;
    traverse(matrix, row+1, col);
    traverse(matrix, row-1, col);
    traverse(matrix, row, col+1);
    traverse(matrix, row, col-1);
}
int main()
{
    scanf("%d%d",&R,&C);
    int matrix[R][C], K, iterationCount=0;
    for(int row=0;row<R;row++)
    {
        for(int col=0;col<C;col++)
        {
            scanf("%d",&matrix[row][col]);
        }
    }
    scanf("%d",&K);
    for(int row=0;row<R;row++)
    {
        for(int col=0;col<C;col++)
        {
            if (matrix[row][col]==K)
            {
                iterationCount++;
                traverse(matrix, row, col);
            }
        }
    }
    printf("%d",iterationCount);

}
