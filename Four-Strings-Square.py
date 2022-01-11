"""
Four strings all having the same length L are passed as the input to the program. The four strings must be printed in a L*L square matrix shape as shown in the example 
input/output.
The string which is on the top will always be the first string in the input. Other three strings can occur in a random order in the input. The sequence of the string can be 
identified by the fact that the last letter of a string will be the first letter of another string (and you can safely assume the last letter will not occur more than once).

Input Format:
The first line contains the string which represents the top of the square matrix.
The next three lines will contain the remaining the three string values which can represent the right, left and bottom side of the squares, but not necessarily in the same order.

Output Format:
The L*L square matrix with these four strings as it's sides as described in the Example Input/Output.

Boundary Conditions:
3 <=  L <= 100

Example Input/Output 1:
Input:
TIGER
YACHT
RANGE
EVERY

Output:
TIGER
H***A
C***N
A***G
YREVE

Example Input/Output 2:
Input:
MAN
DOT
NOD
TIM

Output:
MAN
I*O
TOD
"""
a=input().strip()
b=input().strip()
c=input().strip()
d=input().strip()
l=len(a)
print(a)
if a[0]==c[-1]:
    b,c=c,b
elif a[0]==d[-1]:
    b,d=d,b
if a[-1]==b[0]:
    c,b=b,c
elif a[-1]==d[0]:
    c,d=d,c
star='*'*(l-2)
for i in range(1,l-1):
    print(b[l-i-1],star,c[i],sep='')
print(d[::-1])
