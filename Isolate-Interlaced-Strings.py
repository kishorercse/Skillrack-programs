"""
Two string values S1 and S2 are interlaced and passed as a single input string S. Given L1 which is the length of S1, print S1 and S2 as the output.

Input Format:
The first line contains S.
The second line contains L1.

Output Format:
The first line contains S1.
The second line contains S2.

Boundary Conditions:
4 <= LENGTH(S) <= 100
1 <= LENGTH(S1) <= 99
1 <= LENGTH(S2) <= 99

Example Input/Output 1:
Input:
LBARZIYSK
4

Output:
LAZY
BRISK
"""
s=list(input().strip())
l=len(s)
l1=int(input())
l2=l-l1
i=0
s1=''
s2=''
while i<l:
    if l1>0:
        s1+=s[i]
        i+=1
        l1-=1
    if l2>0:
        s2+=s[i]
        i+=1
        l2-=1
print(s1)
print(s2)
