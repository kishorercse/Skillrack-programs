/*
The function/method getMSBBitMask accepts two arguments SIZE and arr. The integer SIZE represents the size of the integer array arr. The function/method getMSBBitMask must 
return an integer value X whose binary representation indicates the MSB's of the given integers. The presence of MSB's must be indicated by the set bits in the binary
representation of X.   Your task is to implement the function getMSBBitMask so that the program runs successfully.

IMPORTANT: Do not write the main() function as it is already defined. 

Example Input/Output 1: 
Input: 
5 
48 7 12 200 37 

Output: 
172 

Explanation: 
00110000 <- 48 
00000111 <- 7 
00001100 <- 12 
11001000 <- 200 
00100101 <- 37 
X -> 10101100 -> 172 
3rd bit from LSB of 172 indicates the MSB of 7.
4th bit from LSB of 172 indicates the MSB of 12. 
6th bit from LSB of 172 indicates the MSB of both 48 and 37. 
8th bit from LSB of 172 indicates the MSB of 200. 

Example Input/Output 2:
Input: 
4 
7 100 5 4 

Output: 
68*/
#include<stdio.h>
#include <stdlib.h> 

int getMSBBitMask(int SIZE, int arr[])
{
    int result=0;
    for(int i=0;i<SIZE;i++)
    {
        int t=1;
        arr[i]=arr[i]>>1;
        while (arr[i]>0)
        {
            arr[i]=arr[i]>>1;
            t=t<<1;
        }
        result|=t;
    }
    return result;
}

int main() 
{
  int N; 
  scanf("%d", &N); 
  int arr[N];
  for(int index = 0; index < N; index++) 
  { 
    scanf("%d", &arr[index]);
  }
  printf("%d", getMSBBitMask(N, arr)); 
  return 0; 
}
