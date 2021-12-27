/*
The function/method splitEqualBinary accepts an argument N representing an integer value. The number of bits in the binary representation of N is always even. The 
function/method splitEqualBinary must split the binary representation of N into two equal halves. If the two halves are same, then the function must return the sum of decimal 
equivalents of the two equal halves. Else the function must return the integer N as it is. Your task is to implement the function splitEqualBinary so that the program runs 
successfully. IMPORTANT: Do not write the main() function as it is already defined. 

Example Input/Output 1: 
Input: 
10

Output:
4

Explanation:
Here N = 10.
10 -> 1010 -> 10 == 10.
2 + 2 = 4. 

Example Input/Output 2:
Input:
187 

Output: 
22

Explanation:
Here N = 187. 
187 -> 10111011 -> 1011 == 1011.
11 + 11 = 22.

Example Input/Output 3: 
Input: 
8

Output:
8
*/
#include <stdio.h>
#include <stdlib.h>
char s[301];
int ind=0;
void binary(int N)
{
    if(N==0)
        return;
    binary(N/2);
    s[ind++]=N%2+'0';
}


int splitEqualBinary(int N)
{
    int x;
    binary(N);
    char p[15], q[15], k=0;
    int a=0, b=ind/2;
    while(b<ind)
    {
        p[k]=s[a];
        q[k]=s[b];
        k++;
        if (s[a++]!=s[b++])
            return N;
    }
    int t=ind/2;
    while(t>0)
    {
        t--;
        N>>=1;
    }
    return 2*N;

}
int main()
{
    int N;
    scanf("%d", &N);
    printf("%d", splitEqualBinary(N));
    return 0;
}
