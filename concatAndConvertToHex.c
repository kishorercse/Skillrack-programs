/*
The function/method concatAndConvertToHex accepts two arguments - SIZE and arr. The integer SIZE represents the size of the integer array arr. The function/method 
concatAndConvertToHex must find the binary representation of each integer in the given array. Then the function must concatenate all the binary representations and print its 
hexadecimal equivalent. 

Boundary Condition(s):
1 <= SIZE <= 100 
1 <= Each integer value <= 10^6 

Example Input/Output 1: 
Input:
5 
120 50 75 64 44 

Output: 
1E329702C 

Explanation: 
120 -> 1111000
50 -> 110010 
75 -> 1001011 
64 -> 1000000 
44 -> 101100 
The concatenated binary representation is given below.
111100011001010010111000000101100 
The hexadecimal equivalent is 1E329702C. 

Example Input/Output 2: 
Input: 
8 
497 313 917 429 796 53 952 99 

Output: 
3E339E575B8E6BDC63 

Explanation: 
497 -> 111110001 
313 -> 100111001 
917 -> 1110010101 
429 -> 110101101 
796 -> 1100011100 
53 -> 110101 
952 -> 1110111000 
99 -> 1100011 
The concatenated binary representation is given below. 
1111100011001110011110010101110101101110001110011010111101110001100011 
The hexadecimal equivalent is 3E339E575B8E6BDC63.

Example Input/Output 3: 
Input:
4 
8 10 5 1 

Output: 
8AB 
*/
#include <stdio.h>
#include <stdlib.h> 

int bin[10000],index=0;

void decimalToBinary(int n){
    if (n==0)
        return;
    decimalToBinary(n>>1);
    bin[index++]=n%2;
}
void concatAndConvertToHex(int SIZE, int arr[])
{
    for(int i=0;i<SIZE;i++){
        decimalToBinary(arr[i]);
    }
    int t=index%4,x=1,value=0,i=t;
    t-=1;
    while (t>=0){
        if (bin[t]==1)
            value+=x;
        x=x<<1;
        t-=1;
    }
    if (i!=0)
        printf("%d",value);
    for(;i<index;i+=4)
    {
        x=8;
        value=0;
        for(int j=i;j<i+4;j++)
        {
            if (bin[j]==1)
                value+=x;
            x=x>>1;
        }
        if (value>=10)
            printf("%c",'A'+value-10);
        else
            printf("%d",value);
    }
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
  concatAndConvertToHex(N, arr); 
  return 0; 
}
