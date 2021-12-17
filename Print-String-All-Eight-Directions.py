"""
The program must accept a string S as the input. The program must print the string in all 8 possible directions as shown in the Example Input/Output section.

Boundary Condition(s):
2 <= Length of S <= 50

Input Format:
The first line contains S.

Output Format:
The lines contain the string S in all 8 possible directions as shown in the Example Input/Output section.

Example Input/Output 1:
Input:
CART

Output:
T * * T * * T
* R * R * R *
* * A A A * *
T R A C A R T
* * A A A * *
* R * R * R *
T * * T * * T

Explanation:
Here the given string is CART.
So the string CART is printed in all 8 possible directions as given below.
T * * T * * T
* R * R * R *
* * A A A * *
T R A C A R T
* * A A A * *
* R * R * R *
T * * T * * T
The asterisks in the above pattern represent the empty spaces.

Example Input/Output 2:
Input:
tiger

Output:
r * * * r * * * r
* e * * e * * e *
* * g * g * g * *
* * * i i i * * *
r e g i t i g e r
* * * i i i * * *
* * g * g * g * *
* e * * e * * e *
r * * * r * * * r
"""
s=input().strip()
l=len(s)
m=[]
for i in range(l-1):
    t='* '*i + s[l-i-1]+ ' ' + '* '*(l-i-2)
    t+=s[l-i-1]+t[::-1]
    m.insert(0,t)
    print(t)
print(*s[-1:0:-1],*s)
for i in m:
    print(i)
