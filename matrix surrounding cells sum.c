/*The program must accept an R*C matrix containing integer values. An integer N is also passed as the input. 
The program must find the first occurrence of N in the matrix and print the sum S of the surrounding integer values. 

Note: The integer N always occurs at least once in the matrix. 

Boundary Condition(s): 

2 <= R, C <= 10 

Input Format: 
The first line contains R and C separated by a space.
Next R lines contain C integer values each. 
The R+2nd line contains the value of N. 

Output Format: 
The first line contains the value of S. 

Example Input/Output 1: 
Input: 
5 4 
1 2 3 4 
6 7 8 9 
1 5 20 3 
5 4 3 2 
6 8 7 4 
20 

Output: 
41 

Explanation: 
Sum = 7+8+9+5+3+4+3+2 = 41. 

Example Input/Output 2: 

Input: 
5 4 
1 2 3 4 
6 7 8 9 
1 5 20 3 
5 4 3 2 
6 8 7 4 
9 
Output: 
38
*/
#include<stdio.h>
#include<stdlib.h>

int max(int a,int b){
    return (a>b)?a:b;
}

int min(int a,int b){
    return (a<b)?a:b;
}
int main()
{
    int r,c;
    scanf("%d %d",&r,&c);
    int m[r][c],n;
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            scanf("%d",&m[i][j]);
        }
    }
    scanf("%d",&n);
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            if (m[i][j]==n){
                int sum=0;
                for(int row=max(0,i-1);row<=min(r-1,i+1);row++){
                    for(int col=max(0,j-1);col<=min(c-1,j+1);col++){
                        sum+=m[row][col];
                    }
                }
                printf("%d",sum-m[i][j]);
                return 0;
            }
        }
    }
}
