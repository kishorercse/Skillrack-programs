/*
The function/method findVowelsBitMask accepts an argument str representing a string value. The function/method findVowelsBitMask must return an integer value X whose binary 
representation indicates the presence of vowels in the given string by ignoring case. The 5 vowels (aeiou or AEIOU) are mapped to 5 bits in the binary representation of X starting
from LSB(least significant bit). The presence of the vowels must be indicated by the set bits in the binary representation of X. 

Your task is to implement the function findVowelsBitMask so that the program runs successfully. 

IMPORTANT: Do not write the main() function as it is already defined. 

Example Input/Output 1: 
Input: 
SkillRack 

Output: 
5 

Explanation: 
There are two vowels 'i' and 'a' in the string "SkillRack". 
So the binary representation of X = 00101. 
The 1st bit from LSB indicates the presence of the vowel 'a'. 
The 3rd bit from LSB indicates the presence of the vowel 'i'. 
The decimal equivalent of 00101 is 5. 

Example Input/Output 2: 
Input: 
Archaeologist 

Output: 
15 Explanation: 
The binary representation of 15 is 01111.
The last four bits indicate the presence of the vowels 'o', 'i', 'e' and 'a'.
*/
#include <stdio.h> 
#include <stdlib.h>

int findVowelsBitMask(char str[])
{
    int x=0;
    for(int i=0;str[i];i++){
        str[i]=tolower(str[i]);
        if (str[i]=='a' && !(x&1))
            x+=1;
        else if(str[i]=='e' && !((x>>1)&1))
            x+=2;
        else if (str[i]=='i' && !((x>>2)&1))
            x+=4;
        else if(str[i]=='o' && !((x>>3)&1))
            x+=8;
        else if(str[i]=='u' && !((x>>4)&1))
            x+=16;
    }
    return x;

}
int main() 
{ 
  char str[101]; 
  scanf("%s", str); 
  printf("%d", findVowelsBitMask(str)); 
  return 0; 
}
