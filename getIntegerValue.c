/*
The function/method getIntegerValue accepts an argument N. The integer N represents a modified version of an integer X. The integer X contains only the digits other than 0s and 
1s. The integer N is formed by replacing exactly one digit with its binary representation in the integer X. The function/method getIntegerValue must find the value of X and 
return the integer X. 
Your task is to implement the function getIntegerValue so that the program runs successfully.
IMPORTANT: Do not write the main() function as it is already defined. 

Example Input/Output 1:
Input: 
9101485

Output: 
95485 

Explanation: 
Here N = 9101485.
101 -> 5.
So X = 95485. 

Example Input/Output 2: 
Input: 
45109

Output: 
4529 

Explanation:
Here N = 45109.
10 -> 2.
So X = 4529.

Example Input/Output 3:
Input: 
2341001 

Output: 
2349
*/

#include <stdio.h>
#include <stdlib.h>
int getIntegerValue(int N)
{
    int b=1, num=0, binNum=0, t, ten=1;
    while (N>0 && N%10>1)
    {
        num=num*10+N%10;
        N/=10;
        ten*=10;
    }
    t=N%10;
    while(N>0 && t<=1)
    {
        binNum+=t*b;
        b=b<<1;
        N/=10;
        t=N%10;
    }
    int tmp=binNum, ten2=1;
    while (tmp!=0){
        tmp/=10;
        ten2*=10;
    }
    int revNum=0;
    while(num!=0)
    {
        revNum=revNum*10+num%10;
        num/=10;
    }
    return (N*ten2+binNum)*ten+revNum;
    
}
int main() 
{
  int N; 
  scanf("%d", &N); 
  printf("%d", getIntegerValue(N));
  return 0;
}
