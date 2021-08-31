/*
The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output sections.

Boundary Condition(s):
1 <= N <= 100

Input Format:
The first line contains the value of N.

Output Format:
The first 2*N lines contain the desired pattern as shown in the Example Input/Output sections.

Example Input/Output 1:
Input:
4

Output:
1
2*3
4*5*6
7*8*9*10
7*8*9*10
4*5*6
2*3
1

Example Input/Output 2:
Input:
7

Output:
1
2*3
4*5*6
7*8*9*10
11*12*13*14*15
16*17*18*19*20*21
22*23*24*25*26*27*28
22*23*24*25*26*27*28
16*17*18*19*20*21
11*12*13*14*15
7*8*9*10
4*5*6
2*3
1
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n,t=1;
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        for(int j=t;j<t+i-1;j++){
            printf("%d*",j);
        }
        printf("%d\n",t+i-1);
        t+=i;
    }
    t-=1;
    for(int i=n;i>=1;i--){
        for(int j=t-i+1;j<t;j++){
            printf("%d*",j);
        }
        printf("%d\n",t);
        t-=i;
    }

}
