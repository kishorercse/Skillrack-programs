/*
The program must accept an RxC matrix and an integer K as the input. The program must find the first two occurrences of K in the given matrix. 
Then the program must print the smallest sub-matrix which contains the first two occurrences of K as the output. 
Note: The matrix must be traversed from left to right for each row starting from the first row to find the first two occurrences of K. 
Boundary Condition(s): 
1 <= R, C <= 100 1 <= K, Each integer value <= 10^8 
Input Format: The first line contains R, C and K separated by a space. 
The next R lines contain C integers each separated by a space. 
Output Format: The lines contain the sub-matrix as per the given condition. 
Example Input/Output 1: 
Input: 
5 4 
30 48 42 17 
32 52 23 30 
34 44 30 33 
11 20 15 30 
75 26 60 44 84 
Output: 
23 30 30 33 
Explanation: 
The first occurrence of 30 is highlighted in blue and the second occurrence of 30 is highlighted in red. 
48 42 17 32 
52 23 30 34 
44 30 33 11 
20 15 30 75 
26 60 44 84 
The smallest sub-matrix containing these two integers are printed as the output.
*/
#include<stdio.h>
#include<stdlib.h>
#define min(a,b) a<b?a:b
#define max(a,b) a>b?a:b

int main()
{
    int r,c,k;
    scanf("%d %d %d",&r,&c,&k);
    int m[r][c],arr[2][2],cnt=0;
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            scanf("%d",&m[i][j]);
            if (m[i][j]==k && cnt<2){
                arr[cnt][0]=i;
                arr[cnt][1]=j;
                cnt+=1;
            }
        }
    }
    int i=min(arr[0][0],arr[1][0]);
    int jj=min(arr[0][1],arr[1][1]);
    r=max(arr[0][0],arr[1][0]);
    c=max(arr[0][1],arr[1][1]);
    for(;i<=r;i++){
        for(int j=jj;j<=c;j++){
            printf("%d ",m[i][j]);
        }
        printf("\n");
    }

}
