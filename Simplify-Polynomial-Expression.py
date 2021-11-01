"""
The program must accept a string S representing a polynomial expression. The program must simplify the given polynomial expression by combining the like terms (i.e., combining 
the terms having the same exponent values). Then the program must print the simplified polynomial expression. The terms in the simplified polynomial must be sorted by their 
exponent values in descending order. If there are no terms in the simplified polynomial expression, then the program must print 0 as the output. 

Boundary Condition(s): 
5 <= Length of S <= 100

Input Format: 
The first line contains S.

Output Format: 
The first line contains the simplified polynomial expression or 0. 

Example Input/Output 1:
Input:
-4x^1+3x^2-7x^0+9x^1-12x^2-5x^4 

Output: 
-5x^4-9x^2+5x^1-7x^0 

Explanation: 
+3x^2 and -12x^2 are combined as -9x^2.
-4x^1 and +9x^1 are combined as 5x^1. 
So the simplified polynomial expression is -5x^4-9x^2+5x^1-7x^0. 

Example Input/Output 2: 
Input: 
+105x^3+5x^5+99x^4-105x^3+5x^5-10x^5 

Output: 
+99x^4 

Example Input/Output 3: 
Input: 
+1x^1-2x^50-1x^1+2x^50 

Output: 
0
"""
s=input().strip()
d={}
l=len(s)
i=0
a=b=''
f=True
while i<l:
    if s[i].isalpha():
        f=False
    elif s[i] in "+-":
        if a and b:
            t=(b,int(b[b.index('^')+1:]))
            d[t]=d.get(t,0)+int(a)
        a=b=''
        f=True
    if f:
        a+=s[i]
    else:
        b+=s[i]
    i+=1
t=(b,int(b[b.index('^')+1:]))
d[t]=d.get(t,0)+int(a)
f=False
for i in sorted(d.items(),key=lambda x:x[0][1],reverse=True):
    if i[-1]!=0:
        f=True
        if i[-1]>=0:
            print('+',end='')
        print(i[-1],i[0][0],sep='',end='')
if not f:
    print(0)
