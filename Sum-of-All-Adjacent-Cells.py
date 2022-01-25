/*
The program must accept an integer matrix of size RxC as the input. For each integer X in the matrix, the program must print the sum of integers in all the adjacent cells 
(i.e., top-left, top, top-right, left, right, bottom-left, bottom and bottom-right).

Boundary Condition(s):
2 <= R, C <= 50
1 <= Each matrix element <= 1000

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C integers separated by a space.

Output Format:
The first R lines, each contains C integers separated by a space.

Example Input/Output 1:
Input:
4 5
9 2 5 5 9
2 8 7 2 1
3 6 6 5 9
7 1 4 7 9

Output:
12 31 24 24 8
28 40 39 47 30
24 38 40 45 24
10 26 25 33 21

Example Input/Output 2:
Input:
5 5
47 14 40 28 50
27 35 41 26 26
29 42 21 20 35
31 41 14 15 23
26 39 18 20 24

Output:
76 190 144 183 80
167 261 226 261 159
176 239 234 201 110
177 220 216 175 114
111 130 129 94 58

Example Input/Output 3:
Input:
7 4
1 5 2 5
7 4 7 3
9 9 7 5
4 5 1 4
1 5 8 7
6 5 3 1
1 8 6 2

Output:
16 21 24 12
28 47 40 26
29 44 38 22
29 44 50 28
25 33 31 17
20 38 42 26
19 21 19 10
*/
#include<stdio.h>
#include<stdlib.h>

int getSum(int r, int c, int m[r][c], int x, int y)
{
    int rowDiff[]={-1,-1,-1,0,0,1,1,1};
    int colDiff[]={-1,0,1,-1,1,-1,0,1};
    int sum=0;
    for(int i=0;i<8;i++)
    {
        int a=x+rowDiff[i], b=y+colDiff[i];
        if (a>=0 && a<r && b>=0 && b<c)
        {
            sum+=m[a][b];
        }
    }
    return sum;
}
int main()
{
    int r,c;
    scanf("%d %d",&r,&c);
    int m[r][c];
    for(int i=0;i<r;i++)
    {
        for(int j=0;j<c;j++)
        {
            scanf("%d",&m[i][j]);
        }
    }
    for(int i=0;i<r;i++)
    {
        for(int j=0;j<c;j++)
        {
            printf("%d ",getSum(r,c,m,i,j));
        }
        printf("\n");
    }

}
