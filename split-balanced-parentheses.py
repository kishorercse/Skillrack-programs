"""
The program must accept a string S as the input. The string S contains only parentheses, where each open parenthesis '('
has a matching close parenthesis ')'. The program must split the string S into as many substrings as possible, where the
parentheses in each substring must be balanced.

Boundary Condition(s):
2 <= Length of S <= 100

Input Format:
The first line contains S.

Output Format:
The lines contain the substrings of S based on the given conditions.

Example Input/Output 1: 
Input: 
()() 

Output: 
() 
() 
Explanation: 
There are two balanced substrings in S.
Hence the output is 
() 
() 
Example Input/Output 2: 
Input: 
()((())())((()))(()(())()) 

Output: 
() 
((())()) 
((())) 
(()(())()) 

Example Input/Output 3: 
Input: 
(()(()()))()(((()))()(()))(()((()))(())())(())() 
Output: 
(()(()())) 
() 
(((()))()(())) 
(()((()))(())()) 
(()) 
()
"""
def balanced(s):
    a=0
    for i in s:
        if i=='(':
            a+=1
        elif i==')':
            a-=1
            if a<0:
                return False
    if a==0:
        return True
    return False
s=input().strip()
l=len(s)
i=0
while i<l:
    for j in range(i+2,l+1,2):
        if balanced(s[i:j]):
            print(s[i:j])
            i=j
            break
