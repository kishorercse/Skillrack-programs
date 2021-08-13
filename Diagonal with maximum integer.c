/*The program must accept an integer matrix of size RxC as the input. The program must print the elements in the 
diagonal (from lower left to upper right of the matrix) which has the maximum integer among the integers in the matrix. 
If the maximum integer is occurred more than once then consider the first occurred one. 
Boundary Condition(s): 
2 <= R, C <= 50 
1 <= Each integer value <= 999 
Input Format: 
The first line contains the values of R and C separated by a space. The next R lines each contain C integers separated by space(s). 
Output Format: The first line contains the integers in the diagonal which have the maximum integer among the integers in the matrix separated by a space.
Example Input/Output 1: 
Input: 
3 4 
86 81 44 95 
71 16 84 63 
90 75 37 21 
Output: 
75 84 95 
Explanation: The maximum integer in the matrix is 95. So the elements in its diagonal are 75, 84 and 95. Hence the output is 75 84 95 
Example Input/Output 2: 
Input: 
6 3 
12 70 18 
75 45 54
59 26 55 
30 26 75 
88 71 78 
66 96 27 
Output: 
96 78
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int r,c,mx=0;
    scanf("%d %d",&r,&c);
    int m[r][c],x,y;
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            scanf("%d ",&m[i][j]);
            if (m[i][j]>mx){
                mx=m[i][j];
                x=i;
                y=j;
            }
        }
    }
    int a=r-1-x,b=y,mn=a<b?a:b;
    a=x+mn;
    b=y-mn;
    while (a>=0 && b<c){
        if (a>=0 && a<r && b>=0 && b<c)
            printf("%d ",m[a][b]);
        b+=1;
        a-=1;
    }

}
