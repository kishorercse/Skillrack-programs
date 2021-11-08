/*
The program must accept two long values X, Y and print their HCF (GCD). 

Input Format: 
The first line contains X and Y separated by a space. 

Output Format: 
The first line contains the HCF (GCD) of X and Y. 

Boundary Condition(s): 
1 <= X, Y <= 10^18 

Example Input/Output 1: 
Input: 
20 30 

Output: 
10 

Example Input/Output 2: 
Input: 
999999999999 151515151515 

Output: 
30303030303
*/
#include<stdio.h>
#include<stdlib.h>
#define ULL unsigned long long int

ULL hcf(ULL a, ULL b)
{
    return (b==0) ? a : hcf(b,a%b);
}
int main()
{
    ULL a,b;
    scanf("%llu %llu",&a,&b);
    printf("%llu",hcf(a,b));
}
