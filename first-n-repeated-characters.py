"""
The program must accept a string S and then print all the characters which are among the first N repeated characters in S. 

Boundary Condition(s): 
1 <= Length of S <= 1000
1 <= N <= 100

Input Format: 
The first line contains S.
The second line contains N. 

Output Format:
The first line contains the string output.

Example Input/Output 1: 
Input:
abcdeabecdacdbe
4

Output: 
abceabecacbe 

Explanation: 
Though all characters a, b, c, d, e are repeated thrice, the first four repeated characters are a b c e.

Example Input/Output 2: 
Input:
officialwork 
2

Output: 
ffii
"""
s=input().strip()
n=int(input())
l=len(s)
d={}
for i in range(l):
    d[s[i]]=d.get(s[i],0)+1
    if d[s[i]]==2:
        n-=1
        if n==0:
            break
for i in s:
    if d.get(i,0)>=2:
        print(i,end='')
