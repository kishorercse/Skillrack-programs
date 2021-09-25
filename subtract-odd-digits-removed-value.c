/*
The program must accept an integer N as the input. The program must find X which is the value obtained from N 
after removing the odd digits. The program must print the value of N-X as the output.

Boundary Condition(s): 
1 <= N <= 10^9 

Input Format: 
The first line contains N. 

Output Format: 
The first line contains an integer value. 

Example Input/Output 1: 
Input: 
12345 

Output: 
12321 
Explanation: 
Here the value of N is 12345. 
The integer obtained by removing the odd digits in 12345 is 24. 
The value of N-X is 12321 (12345-24), which is printed as the output. 

Example Input/Output 2: 
Input: 
4162

Output: 
3700
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n, temp, multiplier=1, oddremoved=0;
    scanf("%d",&n);
    temp=n;
    while(temp!=0){
        int unitdigit = temp%10;
        if (unitdigit%2==0){
            oddremoved = oddremoved + multiplier*unitdigit;
            multiplier*=10;
        }
        temp/=10;
    }
    printf("%d",n-oddremoved);

}
