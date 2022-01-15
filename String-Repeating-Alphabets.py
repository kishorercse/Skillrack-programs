"""
Given a string S as the input, print the distinct alphabets in S that occur more than once. The alphabets must be printed based on the order of their occurrence in S.

Input Format:
The first line contains S.

Output Format:
The first line contains the distinct alphabets in S that occur more than once.

Boundary Conditions:
2 <= LENGTH of S <= 200

Example Input/Output 1:
Input:
Apple

Output:
p

Example Input/Output 2:
Input:
environment

Output:
en
"""
s=input().strip()
count={}
for i in s:
    count[i]=count.get(i,0)+1
for i in s:
    if count[i]>1:
        print(i,end='')
        count[i]=-1
