"""
The program must accept a string S representing a polynomial expression and the value of x as the input. The program must invert the sign of each term in the given polynomial 
expression. Then the program must print the revised polynomial expression. Finally, the program must evaluate the revised polynomial expression and print the result as the 
output.

Note: In the given polynomial expression, the terms are arranged in any order.

Boundary Condition(s):
5 <= Length of S <= 25
1 <= x <= 9

Input Format:
The first line contains S.
The second line contains x.

Output Format:
The first line contains the revised polynomial expression.
The second line contains the result of the revised polynomial expression.

Example Input/Output 1:
Input:
+10x^2+4x^1-3x^0
2

Output:
-10x^2-4x^1+3x^0
-45

Explanation:
Here x = 2.
f(x) = +10x^2+4x^1-3x^0.
After inverting the sign, the polynomial expression becomes f(x) = -10x^2-4x^1+3x^0.
f(x) = -10x^2-4x^1+3x^0
= -10*(2^2)-4*(2^1)+3*(2^0)
= -(10*4)-(4*2)+(3*1)
= -40-8+3
= -45

Example Input/Output 2:
Input:
-4x^4-2x^2-3x^1+8x^0
3

Output:
+4x^4+2x^2+3x^1-8x^0
343
"""
s=list(input().strip())
x=int(input())
l=len(s)
ans=0
if s[0]=='+':
    s[0]='-'
else:
    s[0]='+'
t=s[0]
for i in range(1,l):
    if s[i] in "+-":
        if s[i]=='+':
            s[i]='-'
        else:
            s[i]='+'
        a,b=t.split('x^')
        ans+=int(a)*(x**int(b))
        t=''
    t+=s[i]
a,b=t.split('x^')
ans+=int(a)*(x**int(b))
print(''.join(s))
print(ans)
