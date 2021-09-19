/*
The program must accept an integer N as the input. The program must print the absolute difference
between the first two and last two digits in N as the output. 

Boundary Condition(s): 
10^3 <= N <= 10^17

Input Format: 
The first line contains the value of N. 

Output Format:
The first line contains the absolute difference between the first two and last two digits in N. 

Example Input/Output 1: 
Input:
21546 

Output: 
25 

Explanation:
The first two digit in 21546 is 21. 
The last two digit in 21546 is 46. 
The absolute difference of 21 and 46 is 25. 

Example Input/Output 2: 
Input: 351684617 

Output: 18
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int a;
    long int n;
    scanf("%ld",&n);
    a=n%100;
    while(n>99)
        n/=10;
    printf("%d",abs(n-a));

}
