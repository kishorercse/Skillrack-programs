"""
The program must accept a string S and print only the three digit numbers in it (in the order of occurrence). The most significant digits can also be one or more 0's. If there 
are no three digit numbers in the string, then print -1 as the output.

Hint: Try using Regular Expressions to solve

Input Format:
The first line will contain S.

Output Format:
The first line will contain the three digit numbers separated by a space.

Boundary Conditions:
1 <= Length of S <= 99999

Example Input/Output 1:
Input:
abc55def789KK23GOOD9999910ONEM109ORE19k6

Output:
789 109

Example Input/Output 2:
Input:
ABCDEF

Output:
-1

Example Input/Output 3:
Input:
qYPxm004xktD000Mq9y026lH8pBDz

Output:
004 000 026
"""
import re
s=re.findall("\d+",input().strip())
f=False
for i in s:
    if len(i)==3:
        print(i,end=" ")
        f=True
if not f:
    print(-1)
