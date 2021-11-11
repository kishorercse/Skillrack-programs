"""
The program must accept a character matrix of size RxC and a string P representing a path inside the matrix as the input. The string P contains the alphabets T, R, L and B. The 
path P always starts from the top-left position of the matrix (i.e., the first row and first column of the matrix). The program must print all the characters which are present 
in the path P as the output.
The path movements are given below. 
T - Move one position towards Top.
R - Move one position towards Right. 
L - Move one position towards Left. 
B - Move one position towards Bottom. 

Boundary Condition(s): 
2 <= R, C <= 50
1 <= Length of P <= 100

Input Format:
The first line contains R and C separated by a space.
The next R lines, each containing C characters separated by a space. 
The (R+2)nd line contains P. 

Output Format:
The first line contains the characters as per the given condition(s).

Example Input/Output 1:
Input: 
4 6
e e g x a a
c z c g d r 
n t o n n t
v b j d r h 
BBRRRRTLLLBB

Output: 
ecntonndgcztb 

Explanation: 
The path BBRRRRTLLLBB in the given 4x6 matrix is highlighted below. 
e e g x a a
c z c g d r
n t o n n t
v b j d r h
The characters which are present in the path BBRRRRTLLLBB are ecntonndgcztb. 
So ecntonndgcztb is printed as the output.

Example Input/Output 2:
Input: 
5 3 
P b 9
I e 3
W 9 Y
Z # w
5 y K
RBRTLBBBL 

Output:
Pbe39be9#Z
"""
r,c=map(int,input().split())
m=[input().split() for _ in range(r)]
p=input().strip()
i,j=0,0
print(m[i][j],end='')
for ch in p:
    if ch=='T':
        i-=1
    elif ch=='R':
        j+=1
    elif ch=='L':
        j-=1
    else:
        i+=1
    print(m[i][j],end='')
