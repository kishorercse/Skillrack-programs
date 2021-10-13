/*
The first line contains ch1 and ch2. 
The second line contains X and Y.

Output Format:
The lines contain all the possible version numbers that can be formed.

Example Input/Output 1:
Input: 
a
b
1
2

Output:
a1.a.1 
a1.a.2 
a1.b.1 
a1.b.2 
a2.a.1 
a2.a.2 
a2.b.1 
a2.b.2 
b1.a.1 
b1.a.2 
b1.b.1 
b1.b.2 
b2.a.1 
b2.a.2 
b2.b.1 
b2.b.2 

Explanation: 
Here the given two alphabets are a, b and the given two integers are 1, 2. All possible version numbers that can be formed using the given alphabet range and 
integer range are printed as the output.

Example Input/Output 2: 
Input:
x y
7 9

Output:
x7.x.7
x7.x.8 
x7.x.9 
x7.y.7 
x7.y.8 
x7.y.9 
x8.x.7
x8.x.8 
x8.x.9
x8.y.7
x8.y.8
x8.y.9 
x9.x.7 
x9.x.8
x9.x.9 
x9.y.7
x9.y.8 
x9.y.9
y7.x.7
y7.x.8 
y7.x.9 
y7.y.7 
y7.y.8 
y7.y.9 
y8.x.7 
y8.x.8
y8.x.9 
y8.y.7 
y8.y.8 
y8.y.9 
y9.x.7 
y9.x.8 
y9.x.9 
y9.y.7
y9.y.8 
y9.y.9 
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    char a,b;
    int x,y;
    scanf("%c %c\n%d %d",&a,&b,&x,&y);
    for(char i=a;i<=b;i++){
        for(int j=x;j<=y;j++){
            for(char k=a;k<=b;k++){
                for(int l=x;l<=y;l++){
                    printf("%c%d.%c.%d\n",i,j,k,l);
                }
            }
        }
    }

}
