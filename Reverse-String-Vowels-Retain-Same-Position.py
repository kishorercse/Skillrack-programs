"""
Given a string S1 as the input, the program must reverse the string, keeping the vowels in the same position. 

Input Format:
The first line contains S1 

Output Format:
The first line contains S1 reversed with vowels retaining the same position. 

Boundary Conditions: 
1 <= Length of S1 <= 1000

Example Input/Output 1:
Input: 
abhcezjqu

Output:
aqjzechbu
"""
s=list(input().strip())
i=0
j=len(s)-1
while i<j:
    if s[i] not in "AEIOUaeiou" and s[j] not in "AEIOUaeiou":
        s[i],s[j]=s[j],s[i]
        i+=1
        j-=1
    while i<j and s[i] in "AEIOUaeiou":
        i+=1
    while i<j and s[j] in "AEIOUaeiou":
        j-=1
print(*s,sep='')
