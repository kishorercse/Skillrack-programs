"""
The program must accept a string S as the input. The program must print the desired pattern as shown in the Example Input/Output section. 

Boundary Condition(s): 
3 <= Length of S <= 50 

Input Format: 
The first line contains S. 

Output Format: 
The lines containing the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1: 
Input:
code 

Output: 
codedoc 
o*****o 
d*****d 
e*****e 
d*****d 
o*****o 
codedoc 

Example Input/Output 2: 
Input: 
marks 

Output:
markskram
a*******a
r*******r
k*******k
s*******s
k*******k
r*******r
a*******a
markskram
"""
s=input().strip()
s+=s[:-1][::-1]
l=len(s)
star='*'*(l-2)
print(s)
for i in range(1,l-1):
    print(s[i],s[l-1-i],sep=star)
print(s)
