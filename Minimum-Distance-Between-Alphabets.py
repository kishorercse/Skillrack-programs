"""
Given a string S and two alphabets C1 and C2 present in S, find the minimum distance D  between C1 and C2 in S.

Input Format:
The first line will contain S.
The second line will contain C1 and C2 separated by a space.

Output Format:
The first line will contain D.

Boundary Conditions:
2 <= Length of S <= 100

Example Input/Output 1:
Input:
spaceship
c s

Output:
1
"""
s=input().strip()
a,b=input().split()
l=len(s)
mn=l
x=y=-1
for i in range(l):
    if s[i]==a or s[i]==b:
        prev=i
        break
for i in range(prev+1,l):
    if s[i]==a or s[i]==b:
        if a==b or s[i]!=s[prev]:
            mn=min(i-prev,mn)
        prev=i
print(mn-1)
