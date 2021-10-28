"""
The program must accept a string S, a character CH and an integer X as the input. The program must fold the string up or down starting from the Xth character. The character CH 
denotes the folding type (u or U for up, d or D for down). The program must print the folded string as the output. The empty spaces must be printed as asterisks.

Boundary Condition(s): 
2 <= Length of S <= 1000 
2 <= X <= Length of S 

Input Format: 
The first line contains S. 
The second line contains CH and X separated by a space. 

Output Format: 
The first two lines contain the folded string based on the given conditions.

Example Input/Output 1: 
Input: 
SkillRack 
U 6 

Output: 
*kcaR 
Skill 
Explanation: 
Here S = "SkillRack", CH = 'U' and X = 6. 
So the string S is folded up from the 6th character. 
Hence the output is 
*kcaR 
Skill 

Example Input/Output 2: 
Input: 
SkillRack 
d 3 

Output: 
*****Sk 
kcaRlli 

Example Input/Output 3: 
Input: 
notebook 
u 5 

Output: 
koob 
note
"""
s=input().strip()
ch,x=input().split()
x=int(x)-1
l=len(s)
if ch=='u' or ch=='U':
    print('*'*(2*x-l)+s[x:][::-1])
    print('*'*(l-2*x)+s[:x])
else:
    print('*'*(l-2*x)+s[:x])
    print('*'*(2*x-l)+s[x:][::-1])
