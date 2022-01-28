/*
The program must accept a string S containing one or more words as the input. For each word in S, the program must swap the first and the last characters. Then the program must
print the modified string S as the output.

Boundary Condition(s):
2 <= Length of S <= 100
2 <= Length of each word in S <= 20

Input Format:
The first line contains S.

Output Format:
The first line contains the modified string S.

Example Input/Output 1:
Input:
Family member #123

Output:
yamilF rembem 312#

Example Input/Output 2:
Input:
Hope for the best

Output:
eopH rof eht tesb

Example Input/Output 3:
Input:
Programming pl@tform

Output:
grogramminP ml@tforp
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    char s[101];
    int i=0,start=0;
    scanf("%[^\n]",s);
    while(1)
    {
        if (s[i]==' ' || s[i]=='\0')
        {
            char ch=s[start];
            s[start]=s[i-1];
            s[i-1]=ch;
            start=i+1;
            if (s[i]=='\0')
                break;
        }
        i++;
    }
    printf("%s",s);

}
