/*
The program must accept an integer matrix of size R*C containing only 1's and 0's as the input. 1 indicates land and 0 indicates water. The program must print the number of 
islands in the given matrix as the output. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically or diagonally.

Boundary Condition(s):
3 <= R, C <= 50

Input Format:
The first line contains R and C separated by a space.
The next R lines, each containing C integers separated by a space.

Output Format:
The first line contains the number of islands in the given matrix.

Example Input/Output 1:
Input:
5 6
0 1 0 1 1 1
1 0 0 1 1 1
1 0 0 1 0 0
0 0 0 1 0 1
0 1 1 0 0 1

Output:
3

Explanation:
The 3 islands in the matrix are highlighted below.
0 1 0 1 1 1
1 0 0 1 1 1
1 0 0 1 0 0
0 0 0 1 0 1
0 1 1 0 0 1

Example Input/Output 2:
Input:
6 4
0 1 1 1
1 0 1 0
1 1 1 0
0 0 0 1
0 1 1 1
1 1 1 1

Output:
1
*/
#include<stdio.h>
#include<stdlib.h>
int R,C;

void traverse(int matrix[R][C], int row, int col)
{
    if (row<0 || row>=R || col<0 || col>=C || matrix[row][col]==0)
    {
        return;
    }
    matrix[row][col]=0;
    traverse(matrix,row-1,col-1);
    traverse(matrix,row-1,col);
    traverse(matrix,row-1,col+1);
    traverse(matrix,row,col-1);
    traverse(matrix,row,col+1);
    traverse(matrix,row+1,col-1);
    traverse(matrix,row+1,col);
    traverse(matrix,row+1,col+1);
}
int main()
{
    scanf("%d %d",&R, &C);
    int matrix[R][C], islandCount=0;
    for(int row=0;row<R;row++)
    {
        for(int col=0;col<C;col++)
        {
            scanf("%d",&matrix[row][col]);
        }
    }
    for(int row=0;row<R;row++)
    {
        for(int col=0;col<C;col++)
        {
            if (matrix[row][col]==1)
            {
                islandCount++;
                traverse(matrix,row,col);
            }
        }
    }
    printf("%d",islandCount);

}
