/*
The function/method stringToDecimal accepts an argument str representing a string value. The string str contains only alphabets. The function/method stringToDecimal must return 
an integer X whose binary representation is formed by replacing each odd ASCII alphabet with 1 and each even ASCII alphabet with 0 in the given string.

Your task is to implement the function stringToDecimal so that the program runs successfully.

IMPORTANT: Do not write the main() function as it is already defined.

Boundary Condition(s):
1 <= Length of the string str <= 50 

Example Input/Output 1:
Input: 
Moon 

Output:
14

Explanation: 
The ASCII value of M is 77.
The ASCII value of o is 111.
The ASCII value of n is 110.
So Moon -> 1110 -> 14.

Example Input/Output 2: 
Input: 
SouthIndia 

Output: 
915 

#include <stdio.h> 
#include <stdlib.h>  ucs19235@rmkec Save Run UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC UCS19235@RMKEC*/
long long int stringToDecimal(char *str)
{
    long long int result=0, base=1;
    int len=strlen(str)-1;
    while(len>=0){
        if (str[len]&1)
            result+=base;
        base*=2;
        len-=1;
    }
    return result;
}

int main() 
{ 
  char str[51]; 
  scanf("%s", str); 
  printf("%lld", stringToDecimal(str)); 
  return 0; 
}
