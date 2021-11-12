/*
The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section. 

Boundary Condition(s): 
2 <= N <= 50

Input Format: 
The first line contains N. 

Output Format:
The first N lines containing the desired pattern as shown in the Example Input/Output section. 

Example Input/Output 1: 
Input: 
3

Output: 
1a 2b 3c 
4d 5e 6f 
7g 8h 9i 

Example Input/Output 2:
Input: 
6 

Output: 
1a 2b 3c 4d 5e 6f 
7g 8h 9i 10j 11k 12l
13m 14n 15o 16p 17q 18r
19s 20t 21u 22v 23w 24x
25y 26z 27a 28b 29c 30d
31e 32f 33g 34h 35i 36j
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n, t=1;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            printf("%d%c ",t,96+(t%26==0?26:t%26));
            t++;
        }
        printf("\n");
    }

}
