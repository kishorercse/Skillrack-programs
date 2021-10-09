"""
The program must accept a string S containing only alphabets as the input. The program must print all the alphabets of S in alphabetical order with respect to their 
positions as shown in the Example Input/Output section.

Boundary Condition(s): 
3 <= Length of S <= 100

Input Format: 
The first line contains S. 

Output Format: 
The lines containing the desired pattern as shown in the Example Input/Output section. 

Example Input/Output 1: 
Input:
Tenth

Output: 
*e*** 
****h
**n** 
T**t*

Example Input/Output 2:
Input:
SkillRack

Output:
******a**
*******c*
**i******
*k******k
***ll****
*****R*** 
S********
"""
s=input().strip()
a=sorted(set(s.lower()))
for i in a:
    for ch in s:
        if i==ch or i.upper()==ch:
            print(ch,end='')
        else:
            print('*',end='')
    print()
