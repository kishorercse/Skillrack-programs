/*
The function/method evaluateOrder accepts an argument str. The string str contains integers separated by the relational operators (greater than > and less than <).

The function/method evaluateOrder must return the integer value 1 if all the relationships between the integers in the string are true. Else the function must return the 
integer value 0.

Your task is to implement the function evaluateOrder so that the program runs successfully.

IMPORTANT: Do not write the main() function as it is already defined.

Boundary Condition(s):
1 <= Each integer value in the given string <= 10^6

Example Input/Output 1:
Input:
10<20<50>10<400>5<6

Output:
1

Explanation:
10<20 = True
20<50 = True
50>10 = True
10<400 = True
400>5 = True
5<6 = True
All the relationships between the integers are True.
Hence 1 is printed as the output.

Example Input/Output 2:
Input:
450>255<300>301>101<102<555

Output:
0

Explanation:
450>255 = True
255<300 = True
300>301 = False
301>101 = True
101<102 = True
102<555 = True
The 3rd relational operator returns False.
Hence 0 is printed as the output.
*/
#include <stdio.h>
#include <stdlib.h>

int evaluateOrder(char *str)
{
    int a,b,ptr,ind;
    sscanf(str,"%d%n",&a,&ptr);
    char sym;
    while(str[ptr] && sscanf(str+ptr,"%c%d%n",&sym,&b,&ind)==2)
    {
        if ((sym=='>' && a<=b) || (sym=='<' && a>=b))
            return 0;
        ptr+=ind;
        a=b;
    }
    return 1;
   
}

int main()
{
    char str[101];
    scanf("%s", str);
    printf("%d", evaluateOrder(str));
    return 0;
}
