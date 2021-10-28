"""
The program must accept a string S of odd length as the input. The program must print the horizontally concatenated triangle pattern of the string S based on the following 
conditions. 
- The first triangle must be formed using all L characters of S, where L = length of the string S. 
- The second triangle must be formed using the first L-2 characters of S. 
- The third triangle must be formed using the first L-3 characters of S. 
- Similarly, the remaining triangles must be formed and printed horizontally. 
The empty spaces between the triangles must be printed as asterisks. 

Boundary Condition(s): 
3 <= Length of S <= 49 

Input Format: 
The first line contains S. 

Output Format: 
The first (L+1)/2 lines contain the horizontally concatenated triangle pattern based on the given conditions. 

Example Input/Output 1: 
Input: 
hello 

Output: 
**h 
*hel**h 
hellohelh 

Explanation: 
Here S = "hello". 
The 1st triangle is formed using all 5 characters. 
**h 
*hel 
hello 

The 2nd triangle is formed using the first 3 characters. 
*h 
hel 

The 3rd triangle is formed using the first character. 
h 
So the three triangles are printed horizontally. 

Example Input/Output 2: 
Input: 
SkillRack 
Output: 
****S 
***Ski******S 
**Skill****Ski****S 
*SkillRa**Skill**Ski**S 
SkillRackSkillRaSkillSkiS
"""
s=input().strip()
l=len(s)
t=(l+1)//2
p=t-1
for i in range(t):
    p=t-1-i
    for j in range((i+1)*2-1,0,-2):
        print('*'*p,end='')
        print(s[:j],end='')
        if j!=1:
            print('*'*p,end='')
    print()
