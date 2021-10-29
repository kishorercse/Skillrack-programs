"""
The program must accept a string S containing only alphabets as the input. Each alphabet(ignoring case) has a weight as given below. 
A = 0 
B = 1 
C = Weight of A + Weight of B 
D = Weight of B + Weight of C and so on. 
The program must print the total weight of the alphabets in the given string S as the output. 

Boundary Condition(s): 
1 <= Length of S <= 100

Input Format: 
The first line contains S. 

Output Format: 
The first line contains an integer value representing the total weight of the alphabets. 

Example Input/Output 1: 
Input: 
Bat 

Output: 
4182 

Explanation: 
Here S = "Bat". 
B = 1 
a = 0 
t = 4181 
So their sum is 4182 (1 + 0 + 4181). 

Example Input/Output 2: 
Input: 
SkillRack

Output: 
4491 

Explanation: 
Here S = "SkillRack". 
S = 2584 
k = 55 
i = 21 
l = 89 
l = 89 
R = 1597 
a = 0 
c = 1 
k = 55 
So their sum is 4491 (2584 + 55 + 21 + 89 + 89 + 1597 + 0 + 1 + 55).
"""
s=input().strip().lower()
l=[0,1]
for _ in range(24):
    l.append(l[-1]+l[-2])
weight=0
for i in s:
    weight+=l[ord(i)-97]
print(weight)
