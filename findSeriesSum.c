/*
The function/method findSeriesSum accepts an argument str representing a string value. The string str contains a series of integers but some integers are denoted by their binary
representations. The function/method findSeriesSum must find the decimal value for each binary representation in the given string. Then the function must return an integer 
representing the sum of all the integers present in the given series. 
Your task is to implement the function findSeriesSum so that the program runs successfully. 

IMPORTANT: Do not write the main() function as it is already defined. 

Boundary Condition(s):
1 <= Each integer value in the series <= 10^7 

Example Input/Output 1:
Input: 
45 32 1010 5 10111 60

Output:
175 

Explanation: 
In the given series, two integers are denoted by their binary representations. 
1010 -> 10
10111 -> 23
Sum = 45 + 32 + 10 + 5 + 23 + 60 = 175.

Example Input/Output 2:
Input:
10 111 1005 1114 101 

Output: 
2133 
*/

#include <stdio.h>
#include <stdlib.h> 

int findSeriesSum(char *str)
{
    int sum=0, decimal, binary, decimalFlag, power;
    for(int i=0;str[i]!='\0';i++)
    {
        decimalFlag=0;
        decimal=0;
        int startIndex=i;
        while(isdigit(str[i]))
        {
            decimal=decimal*10+str[i]-'0';
            if (str[i]!='0' && str[i]!='1')
                decimalFlag=1;
            i++;
        }
        if (decimalFlag==1)
            sum+=decimal;
        else
        {
            binary=0;
            int len=i-startIndex;
            power=1<<(len-1);
            while(startIndex<i)
            {
                binary+=power*(str[startIndex++]-'0');
                power=power>>1;
            }
            sum+=binary;
        }
    }
    return sum;
}
int main() 
{
  char str[101]; 
  scanf("%[^\n\r]", str); 
  printf("%d", findSeriesSum(str)); 
  return 0;
}
