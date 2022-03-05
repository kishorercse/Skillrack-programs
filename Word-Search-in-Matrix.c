/*
The program must accept a character matrix of size R*C and a string S as input. The program must search the string S in the given R*C character matrix by traversing
horizontally and vertically. If the string S is found in the matrix, the program must print yes. Else the program must print no as the output.

Boundary Condition(s):
2 <= R, C, Length of S <= 50

Input Format:
The first line contains R and C separated by a space.
The next R lines, each containing C characters separated by a space.
The (R+2)nd line contains the string S.

Output Format:
The first line contains the either yes or no.

Example Input/Output 1:
Input:
5 8
k e r t u n o p
r a i n q b o w
v a n g u e c l
r a t t o n g h
h w y f n x o g
ringtone

Output:
yes

Explanation:
Here, the string ringtone is found in the given matrix and it is highlighted below.
k e r t u n o p
r a i n q b o w
v a n g u e c l
r a t t o n g h
h w y f n x o g

Example Input/Output 2:
Input:
4 7
p o k r a n w
m e n e e r l
j h g i n o v
a d f q s t c
engineering

Output:
no
*/
#include<stdio.h>
#include<stdlib.h>
int R, C, found=0;

void search(char matrix[R][C], int row, int col, char *word, int index)
{
    if (word[index]==NULL)
    {
        found=1;
        return;
    }
    if (row<0 || row>=R || col<0 || col>=C || found==1 || matrix[row][col]!=word[index])
    {
        return;
    }
    char backup=matrix[row][col];
    matrix[row][col]='-';
    search(matrix,row+1,col,word,index+1);
    search(matrix,row-1,col,word,index+1);
    search(matrix,row,col-1,word,index+1);
    search(matrix,row,col+1,word,index+1);
    matrix[row][col]=backup;
}
int main()
{
    scanf("%d%d",&R,&C);
    char matrix[R][C], word[51], str[2];
    for(int row=0;row<R;row++)
    {
        for(int col=0;col<C;col++)
        {
            scanf("%s",str);
            matrix[row][col]=str[0];
        }
    }
    scanf("%s",word);
    for(int row=0;row<R;row++)
    {
        for(int col=0;col<C;col++)
        {
            if (matrix[row][col]==word[0])
            {
                search(matrix,row,col,word,0);
                if (found==1)
                {
                    printf("yes");
                    return;
                }
            }
        }
    }
    printf("no");
    
}
