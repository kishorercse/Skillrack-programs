"""
The program must accept a string S as the input. The program must toggle the case of the alphabets if two or more alphabets of the same case occur consecutively in the string S.
Then the program must print the revised string as the output. 

Boundary Condition(s): 
2 <= Length of S <= 1000 

Input Format:
The first line contains S. 

Output Format: 
The first line contains the revised string.

Example Input/Output 1: 
Input:
breadANDjam 

Output: 
BREADandJAM 

Explanation: 
Here S = breadANDjam.
bread -> BREAD 
AND -> and 
jam -> JAM 
Now the string becomes BREADandJAM. 

Example Input/Output 2: 
Input: 
SkillRack 

Output:
SKILLRACK 

Example Input/Output 3: 
Input:
aAbBcCdDee 

Output:
aAbBcCdDEE
"""
s=input().strip()
l=len(s)
i=0
while i<l:
    j=i+1
    while j<l and s[j-1].islower()==s[j].islower():
        j+=1
    if j>i+1:
        print(s[i:j].swapcase(),end='')
    else:
        print(s[i:j],end='')
    i=j
