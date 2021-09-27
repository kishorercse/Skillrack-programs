/*
The program must accept an integer N as the input. The program must print the minimum number of replacements needed for N to become 1 based on the following conditions: 
- If N is even, replace N with N/2.
- If N is odd, replace N with either N + 1 or N - 1. 

Boundary Condition(s): 
1 <= N <= 231 - 1 

Input Format: 
The first line contains the value of N. 

Output Format: 
The first line contains the integer value denoting the minimum number of replacements required. 

Example Input/Output 1:
Input: 
7 

Output: 
4

Explanation: 
The minimum number of replacements needed to change 7 to 1 are 7->8->4->2->1.
Hence 4 is the output 

Example Input/Output 2: 
Input: 
3 

Output: 
2
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    long int n;
    int min=0;
    scanf("%ld",&n);
    while(n!=1){
        if (n%2==0)
            n/=2;
        else{
            if (n%4==1 || n==3)
                n-=1;
            else
                n+=1;
        }
        min+=1;
    }
    printf("%d",min);

}
