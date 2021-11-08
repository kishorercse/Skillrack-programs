/*
You must implement the function printRepeatNextPattern(int N) which accepts an integer N as the input. The function must print the desired pattern as shown in the Example 
Input/Output section. 

Boundary Condition(s): 
3 <= N <= 100 

Input Format: 
The first line contains the value of N. 

Output Format: 
The first N lines containing the desired pattern as shown in the Example Input/Output section. 

Example Input/Output 1: 
Input: 
4 

Output: 
1222 
2333 
3444 
4555 

Example Input/Output 2: 
Input: 
7 

Output:
1222222
2333333
3444444
4555555
5666666
6777777
7888888
*/
#include <stdio.h>
void printRepeatNextPattern(int N)
{
    for(int i=1; i<=N; i++)
    {
        printf("%d",i);
        for(int j=1; j<N; j++)
            printf("%d",i+1);
        printf("\n");
    }

}

int main()
{
    int N;
    scanf("%d",&N);
    printRepeatNextPattern(N);
    return 0;
}
