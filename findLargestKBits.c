/*
The function/method findLargestKBits accepts two arguments str and K. The string str contains only 0s and 1s. K represents an integer value. The function/method findLargestKBits 
must an integer representing the largest possible integer that can be formed using exactly K consecutive bits in the given string. Note: The value of K is always less than or 
equal to the length of the given string. Your task is to implement the function findLargestKBits so that the program runs successfully. IMPORTANT: Do not write the main() function 
as it is already defined. 

Boundary Condition(s): 
1 <= Length of the string <= 1000 
1 <= K <= 31 

Example Input/Output 1: 
Input: 
001001101100 
4 

Output: 
13 

Explanation: 
Here K = 4. All possible ways are given below. 
0010 -> 2 
0100 -> 4 
1001 -> 9 
0011 -> 3 
0110 -> 6 
1101 -> 13
1011 -> 11
0110 -> 6 
1100 -> 12 
The largest possible integer using 4 consecutive bits is 13. 

Example Input/Output 2: 
Input:
1100111011 
3 

Output: 
7 
*/
#include <stdio.h> 
#include <stdlib.h>
int findLargestKBits(char *str, int K)
{
    int len=strlen(str), mx=-1;
    for(int i=0;i<=len-K;i++){
        int t=0, p=1;
        for(int j=i+K-1;j>=i;j--){
            t+=p*(str[j]=='0'?0:1);
            p*=2;
        
        }
        if (t>mx)
            mx=t;
    }
    return mx;
}
int main() 
{ 
  char str[1001]; 
  int K; 
  scanf("%s\n%d", str, &K); 
  printf("%d", findLargestKBits(str, K)); 
  return 0; 
}
