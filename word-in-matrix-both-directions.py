"""
The program must accept a string S and a character matrix of size RxC as the input. The program must print yes as the output if the string S 
is found in the character matrix arranged either vertically or horizontally (in any direction left to right, right to left, top to bottom 
or bottom to top). Else the program must print no as the output. 

Boundary Condition(s): 
1 <= R, C <= 100 
1 <= Length of S <= 100 

Input Format: 
The first line contains the string S. 
The second line contains R and C separated by a space. 
The next R lines contain C characters each separated by a space. 

Output Format: 
The first line contains yes or no. 
Example Input/Output 1: 
Input:
try
5 4 
n e y q 
z w r i 
c t t y 
u r r w 
r k z x 

Output: 
yes 

Explanation: 
The string try starts at the position (3,3) and ends at the position (1,3). Hence yes is printed. 

Example Input/Output 2: 
Input: 
help 
5 5 
w t h v a 
l h f g t 
p n g f s
a h e l r
b v u q p

Output: 
no
"""
s=input().strip()
rev_s=''.join(reversed(s))
l=len(s)
r,c=map(int,input().split())
mat=[input().split() for _ in range(r)]
for i in range(r):
    for j in range(c-l+1):
        if all(s[k]==mat[i][j+k] for k in range(l)) or all(rev_s[k]==mat[i][j+k] for k in range(l)):
            print("yes")
            exit()
for j in range(c):
    for i in range(r-l+1):
        if all(s[k]==mat[i+k][j] for k in range(l)) or all(rev_s[k]==mat[i+k][j] for k in range(l)):
            print("yes")
            exit()
print("no")
