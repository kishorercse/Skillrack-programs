/*
Given a 9×9 sudoku the program must evaluate it for its correctness. The program must check both the sub matrix correctness and the entire sudoku correctness using the 
following rules.
Rule 1: Each 3*3 sub matrix must contain all digits from 1 to 9.
Rule 2: The digits 1 to 9 must not repeat in a given or column in the 9*9 sudoku matrix.

Boundary Condition(s):
Sudoku matrix is 9*9 matrix

Input Format:
9 lines containing 9 integer values representing the column values.

Output Format:
The first line contains VALID or INVALID    

Example Input/Output 1:
Input:
1 1 3 6 8 7 2 4 9
8 4 9 5 2 1 6 3 7
2 6 7 3 4 9 5 8 1
1 5 8 4 6 3 9 7 2
9 7 4 2 1 8 3 6 5
3 2 6 7 9 5 4 1 8
7 8 2 9 3 4 1 5 6
6 3 5 1 7 2 8 9 4
1 9 4 8 5 6 7 2 3

Output:
INVALID

Explanation:
1 is repeated along first row. (Also 1 is repeated along first column).

Example Input/Output 2:
Input:
5 1 3 6 8 7 2 4 9
8 4 9 5 2 1 6 3 7
2 6 7 3 4 9 5 8 1
1 5 8 4 6 3 9 7 2
9 7 4 2 1 8 3 6 5
3 2 6 7 9 5 4 1 8
7 8 2 9 3 4 1 5 6
6 3 5 1 7 2 8 9 4
4 9 1 8 5 6 7 2 3

Output:
VALID
*/
#include<stdio.h>
#include<stdlib.h>
#define N 9
int main()
{
    int rowFlags[9], colFlags[9], subFlags[9];
    int digit;
    for(int ctr=0;ctr<9;ctr++)
    {
        rowFlags[ctr]=colFlags[ctr]=subFlags[ctr]=1;
    }
    for(int row=0;row<N;row++)
    {
        for(int col=0;col<N;col++)
        {
            scanf("%d",&digit);
            rowFlags[row]|=(1<<digit);
            colFlags[col]|=(1<<digit);
            subFlags[(row/3)*3+(col/3)]|=(1<<digit);
        }
    }
    int total=(1<<10)-1;
    for(int ctr=0;ctr<9;ctr++)
    {
        if (rowFlags[ctr]!=total || colFlags[ctr]!=total || subFlags[ctr]!=total)
        {
            printf("INVALID");
            return;
        }
    }
    printf("VALID");
}
