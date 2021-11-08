/*
The program must accept a character matrix of size RxC as the input. The program must replace all the vowels by the asterisk *. Then the program must remove the row(s) and 
column(s) which are having all the characters as asterisk *. Finally, the program must print the modified matrix as the output. If all the rows and columns are removed from 
the matrix then the program must print -1 as the output. 

Boundary Condition(s): 
2 <= R, C <= 50 
a <= Matrix element value <= z 

Input Format: 
The first line contains the values of R and C separated by a space. 
The next R lines contain C characters each separated by a space. 

Output Format:
The list of lines containing the characters of the modified matrix or the first line contains -1. 

Example Input/Output 1: 
Input:
4 5
s x n u l
a i e a o
a f v i j
o m e e y

Output:
s x n l
* f v j
* m * y 

Explanation: 
The vowels are replaced by the asterisk *. Now the matrix becomes 
s x n * l
* * * * *
* f v * j
* m * * y 
Here all the characters in the 2nd row and 4th column are asterisks. 
So they are removed from the matrix. 
Hence the output is 
s x n l
* f v j
* m * y 

Example Input/Output 2: 
Input: 
3 3 
e i e
a e o
e e e

Output: 
-1
*/
#include<stdio.h>
#include<stdlib.h>

int isVowel(char ch)
{
    ch=tolower(ch);
    return ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u';
}
int main()
{
    int r,c;
    scanf("%d %d\n",&r,&c);
    int row[r], col[c];
    char m[r][c];
    memset(row, 0, r*sizeof(int));
    memset(col, 0, c*sizeof(int));
    for(int i=0;i<r;i++)
    {
        for(int j=0;j<c;j++)
        {
            scanf("%c ",&m[i][j]);
            if (isVowel(m[i][j])){
                m[i][j]='*';
                row[i]++;
                col[j]++;
            }
        }
    }
    int w=0;
    for(int i=0;i<r;i++)
    {
        int flag=0;
        for(int j=0;j<c;j++)
        {
            if (row[i]!=c && col[j]!=r)
            {
                flag=1;
                printf("%c ",m[i][j]);
            }
        }
        if (flag==1){
            w=1;
            printf("\n");
        }
    }
    if (w==0)
        printf("-1");

}
