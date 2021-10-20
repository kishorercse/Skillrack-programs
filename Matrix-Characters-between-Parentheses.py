"""
The program must accept a character matrix of size R*C as the input. The matrix contains alphabets and a pair of parentheses. The program must print the characters present 
between the open parenthesis and the close parenthesis as the output. Consider the rows of the matrix in circular fashion (i.e., top to bottom for rows where left to right
in each row). 
 
Boundary Condition(s): 
2 <= R, C <= 50 

Input Format: 
The first line contains R and C separated by a space. 
The next R lines, each contains C characters separated by a space. 

Output Format: 
The first line contains the characters present between the open parenthesis and the close parenthesis. 

Example Input/Output 1: 
Input: 
6 6 
h f j b f d 
l q g t h q
p l ( s k i
l l r a c k 
) k f e j h 
u t s s x c 

Output: 
skillrack 

Explanation: 
The characters present between the open parenthesis and the close parenthesis are highlighted below. 
h f j b f d 
l q g t h q 
p l ( s k i 
l l r a c k 
) k f e j h 
u t s s x c 
Hence the output is skillrack 

Example Input/Output 2: 
Input:
4 5 
d g ) y h 
w l r n b 
a e u ( v 
z l m k e 

Output: 
vzlmkedg 

Example Input/Output 3: 
Input: 
3 3 
a b c 
) ( f 
g h i 

Output: 
fghiabc
"""
r,c=map(int,input().split())
m=[input().split() for _ in range(r)]
s=''
s2=''
open=close=end=False
add=True
for i in m:
    for j in i:
        if j=='(':
            open=True
            add=True
            if open and not close:
                s=''
        elif j==')':
            close=True
            if open and close:
                end=True
                break
            else:
                add=False
                s2=s
                s=''
        else:
            if add:
                s+=j
    if end:
        break
print(s+s2)
