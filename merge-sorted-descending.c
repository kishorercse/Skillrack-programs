/*
The program must accept two lines of integers (M and N number of integers) which are sorted in ascending order.
The program must merge the two lines of integers such that the merged integers are sorted in descending order. 
Finally, the program must print the merged integers as the output. 

Boundary Condition(s):
1 <= M, N <= 10^5 

Input Format:
The first line contains M and N separated by a space. 
The second line contains M integers separated by a space.
The third line contains N integers separated by a space. 

Output Format:
The first line contains M + N integers separated by a space. 

Example Input/Output 1:
Input: 
4 6 
13 15 17 28 
1 7 14 23 25 26 

Output: 
28 26 25 23 17 15 14 13 7 1

Example Input/Output 2:
Input:
5 3 
8 10 13 23 40 
9 32 39 

Output: 
40 39 32 23 13 10 9 8
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int m,n,i,j,index=0;
    scanf("%d %d",&m,&n);
    int a[m],b[n],r[m+n];
    for(i=0;i<m;i++)
        scanf("%d",&a[i]);
    for(i=0;i<n;i++)
        scanf("%d",&b[i]);
    i=m-1;
    j=n-1;
    while(i>=0 && j>=0){
        if (a[i]>b[j]){
            r[index++]=a[i];
            i--;
        }
        else{
            r[index++]=b[j];
            j--;
        }
    }
    while(i>=0)
        r[index++]=a[i--];
    while(j>=0)
        r[index++]=b[j--];
    for(i=0;i<m+n;i++)
        printf("%d ",r[i]);
}
