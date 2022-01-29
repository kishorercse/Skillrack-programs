/*
The program must accept an integer matrix of size RxC as the input. The program must print the number of 3x3 submatrices having only odd integers as the output.
Note: The values of R and C are always divisible by 3.

Boundary Condition(s):
3 <= R, C <= 48

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C integers separated by a space.

Output Format:
The first line contains the number of 3x3 submatrices having only odd integers.

Example Input/Output 1:
Input:
6 9
21 88 72 85 47 21 79 51 13
24 31 70 37 35 41 89 29 51
31 62 36 25 33 87 23 83 59
53 93 49 16 61 41 71 73 15
35 21 83 84 71 13 23 67 79
77 43 75 81 60 79 39 69 57

Output:
4

Example Input/Output 2:
Input:
3 6
95 25 41 69 28 39
49 81 85 53 17 55
11 57 93 71 73 95

Output:
1

Example Input/Output 3:
Input:
9 9
89 85 17 59 98 17 15 99 49
91 73 45 19 70 13 63 45 91
89 89 93 36 22 42 63 25 29
87 35 71 88 46 79 31 84 81
75 33 67 19 47 28 95 80 10
99 79 81 82 88 74 53 36 60
33 97 93 29 97 73 67 99 15
31 23 43 77 19 11 59 33 77
59 43 27 16 59 39 33 17 71

Output:
5
*/
#include<stdio.h>
#include<stdlib.h>
int r,c;
int allOdd(int row, int col, int m[r][c])
{
    for(int i=row;i<row+3;i++)
    {
        for(int j=col;j<col+3;j++)
        {
            if (m[i][j]%2==0)
                return 0;
        }
    }
    return 1;
}
int main()
{
    scanf("%d %d",&r,&c);
    int m[r][c], count=0;
    for(int i=0;i<r;i++)
        for(int j=0;j<c;j++)
            scanf("%d",&m[i][j]);
    for(int i=0;i<=r-3;i+=3)
    {
        for(int j=0;j<=c-3;j+=3)
        {
            if (allOdd(i,j,m))
                count++;
        }
    }
    printf("%d",count);

}
