/*
The program must accept N lower case alphabets in alphabetical order as the input. The program must print the missing alphabets in the given series of N alphabets as the output. 

Note: At least one alphabet is always missing in the given series of N alphabets. 

Boundary Condition(s):
2 <= N <= 15 

Example Input/Output 1:
Input:
5
a c e h k 

Output: 
b d f g i j 

Explanation: 
b is missing between a and c. 
d is missing between c and e.
f and g are missing between e and h. 
i and j are missing between h and k.

Example Input/Output 2:
Input: 
8
d h m o p q t u 

Output:
e f g i j k l n r s
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n;
    scanf("%d\n",&n);
    char a,b;
    scanf("%c ",&a);
    for(int i=1;i<n;i++)
    {
        scanf("%c ",&b);
        a++;
        while(a<b)
        {
            printf("%c ",a++);
        }
        a=b;
    } 

}
