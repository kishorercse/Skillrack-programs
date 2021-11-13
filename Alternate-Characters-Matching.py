"""
The program must accept two string values S1 and S2 having an equal even length as the input. The program must print "YES" if the alternate characters of S1 match the alternate 
characters of S2 ignoring the case. Else the program must print "NO" as the output. 

Boundary Condition(s):
2 <= Length of S1, S2 <= 100 

Input Format: 
The first line contains S1. 
The second line contains S2. 

Output Format: 
The first line contains YES or NO.

Example Input/Output 1:
Input:
abcdef
parcte

Output:
YES

Explanation: 
The characters at the odd positions in S1 = "ace". 
The characters at the even positions in S2 = "ace".
Hence YES is printed as the output. 

Example Input/Output 2: 
Input:
abcdef 
BQDSFU

Output: 
YES

Example Input/Output 3: 
Input:
abcd 
abcd 

Output: 
NO
"""
a=input().strip().lower()
b=input().strip().lower()
x=0
y=1
f1=f2=True
l=len(a)
while x<l or y<l:
    if f1 and a[x]!=b[y]:
        f1=False
    if f2 and a[y]!=b[x]:
        f2=False
    if not f1 and not f2:
        break
    x+=2
    y+=2
if f1 or f2:
    print("YES")
else:
    print("NO")
