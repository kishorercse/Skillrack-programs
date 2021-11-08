/*
You must implement the function printZigZagTrianglePattern(int N) which accepts an integer N as the input. The function must print the desired pattern as shown in the Example 
Input/Output section. 

Boundary Condition(s):
2 <= N <= 100 

Input Format: 
The first line contains the value of N. 

Output Format: 
The first N lines containing the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
Input: 
4 

Output: 
1 
3*2
4*5*6 
10*9*8*7 

Example Input/Output 2: 
Input: 
7 

Output: 
1 
3*2 
4*5*6 
10*9*8*7 
11*12*13*14*15 
21*20*19*18*17*16 
22*23*24*25*26*27*28
*/
#include <stdio.h>

void printZigZagTrianglePattern(int N)
{
  int diff, printVal=1;
  for(int i=1; i<=N; i++)
  {
    if (i%2!=0)
    {
      diff=1;
      printVal+=(i-1);
    }
    else
    {
      diff=-1;
      printVal+=i;
    }
    for(int j=1; j<i; j++)
    {
      printf("%d*",printVal);
      printVal+=diff;
    }
    printf("%d\n",printVal);
  }
}

int main()
{
  int N;
  scanf("%d",&N);
  printZigZagTrianglePattern(N);
}
