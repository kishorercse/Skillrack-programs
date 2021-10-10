"""
Given a string S, the program must print the substring based on following conditions. 
-The substring must be the longest one of all the possible substring in the given string. 
-There must not be any repeating characters in the substring. 
-If there is more than one substring satisfying the above two conditions, then print the substring which occurs first. 
-The length of the substring must be atleast 3.
If there is no substring satisfying all the above conditions then the program must print -1. 

Boundary Condition(s): 
1 <= Length of S <= 10^5 

Input Format: 
The first line contains S. 

Output Format: 
The first line contains the substring or -1. 

Example Input/Output 1: 
Input: 
manager 

Output: 
nager 

Example Input/Output 2: 
Input: 
abcdabcdabcd 

Output: 
abcd 

Example Input/Output 3: 
Input: 
abababbaab 

Output: 
-1
"""
s=input().strip()
l=len(s)
a = b = mx = 0
d={}
ind=-1
for i in range(l):
    if s[i] in d:
        t=b-a
        if t>=3 and t>mx:
            mx=t
            ind=[a,b]
        a=max(a,d[s[i]]+1)
    d[s[i]]=i
    b+=1
t=b-a
if t>=3 and t>mx:
    mx=t
    ind=[a,b+1]
if ind==-1:
    print(-1)
else:
    print(s[ind[0]:ind[1]])
