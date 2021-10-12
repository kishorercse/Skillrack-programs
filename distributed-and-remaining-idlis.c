/*
There are M idlis in a plate. The idlis are to be shared equally among N friends. The program must print the number of idlis received by each one of them and the number of idlis
remaining after distributed equally as the output. 

Example Input/Output 1:
Input:
10 2 

Output: 
5 0 

Example Input/Output 2:
Input:
15 7 

Output:
2 1
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int m,n;
    scanf("%d %d",&m,&n);
    printf("%d %d",m/n,m%n);

}
