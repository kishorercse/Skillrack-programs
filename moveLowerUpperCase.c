/*
The function/ method moveLowerUpperCase accepts an argument str representing a string value (without any spaces).

The function/ method move all the lower case alphabets to the beginning and all the upper case alphabets to the
end. Then the function must return the modified string value as a new string.

Your task is to implement the function moveLowerUpperCase so that program runs successfully.

Boundary Condition(s):
1 <= Length of the string <= 1000

Input Format:
The first line contains the string value.

Output Format:
The first line contains the modified string value.

Example Input/Output 1: 
Input: 
5OranGesAretheRe 

Output: 
ranesrethee5OGAR

Explanation:
Here the given string is 5OranGesAretheRe. 
The lower case alphabets in the given string are r a n e s r e t h e e. 
The upper case alphabets in the given string are O G A R. 
After moving all the lower case alphabets to the beginning and all the upper case alphabets to the end, the string becomes ranesrethee5OGAR. 

Example Input/Output 2:
Input:
5Tiger2OWL3ox1Lion6FOX

Output:
igeroxion52316TOWLLFOX
*/
#include <stdio.h> 
#include <stdlib.h> 

char* moveLowerUpperCase(char *str)
{
    char *low=malloc(sizeof(char)*1001), *up=malloc(sizeof(char)*1001), *dig=malloc(sizeof(char)*1001);
    int ind=0, ind2=0, ind3=0;
    for(int i=0;str[i];i++){
        if(islower(str[i]))
            low[ind++]=str[i];
        else if(isupper(str[i]))
            up[ind2++]=str[i];
        else
            dig[ind3++]=str[i];
    }
    strcat(low,dig);
    strcat(low,up);
    return low;
}

int main()
{ 
  char str[1001]; 
  scanf("%s", str);
  char *ptr = moveLowerUpperCase(str);
  if(str == ptr) 
  {
    printf("New string is not formed\n"); 
  }
  if(ptr[0] == '\0') 
  { 
    printf("String is empty\n"); 
  } 
  printf("%s", ptr); 
}
