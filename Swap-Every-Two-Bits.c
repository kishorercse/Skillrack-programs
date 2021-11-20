/*
The program must accept an integer N as the input. The program must swap every two bits in the binary representation of N from LSB and print the revised value of N as the output.
If the number of bits in the binary representation of N is odd, then consider a leading zero in its binary representation to swap every two bits. Please fill in the blanks with
code so that the program runs successfully.

Boundary Condition(s): 
1 <= N < 2^8

Input Format: 
The first line contains N.

Output Format: 
The first line contains the revised value of N. 

Example Input/Output 1: 
Input: 
218 

Output: 
229 

Explanation: 
The binary representation of 218 is 11011010. 
After swapping every two bits in the binary representation of 218, the binary representation becomes 11100101
The decimal equivalent of 11100101 is 229 which is printed as the output.

Example Input/Output 2: 
Input:
154 

Output: 
101 

Example Input/Output 3: 
Input: 
7

Output:
11 

Explanation: 
The binary representation of 7 is 0111. 
After swapping every two bits in the binary representation of 7, the binary representation becomes 1011. 
The decimal equivalent of 1011 is 11 which is printed as the output.
*/
#include <stdio.h>
#include <stdlib.h>
int main()
{
  int N; 
  scanf("%d", &N);
  printf("%d", ((N&85) <<1) | ((N&170)>>1)); 
  return 0;
}
