"""
The program must accept a character matrix of size R*C and a string S as input. The program must print YES if the string S can be formed by traversing the matrix. The matrix can be traversed only through the neighbor elements (horizontally, vertically and diagonally adjacent elements) starting from any position. The program must print NO if the string cannot be formed from the matrix.
Note: Character in a position cannot be used more than once to form the string.

Boundary Condition(s):
2 <= R, C <= 50
2 <= Length of S <= 50


 
Input Format:
The first line contains the value of R and C separated by a space.
The next R lines contain C characters separated by space(s).
The (R+2)th line contains the string S.

Output Format:
The first line contains the either YES or NO.

Example Input/Output 1:
Input:
3 4
l o n g
c h a r
t y p e
grape

Output:
YES

Explanation:
l o n g
c h a r
t y p e

Example Input/Output 2:
Input:
5 5
a p p l e
s u g a r
g r a p e
p h o t o
a l e o n
tapeapple

Output:
NO
"""
def find_word(i,j,ind,t):
    if ind==l:
        return True
    for a,b in arr:
        x,y=i+a,j+b
        if 0<=x<r and 0<=y<c and s[ind]==m[x][y] and [x,y] not in t:
            if find_word(x,y,ind+1,t[:]+[[x,y]]):
                return True
r,c=map(int,input().split())
m=[input().split() for _ in range(r)]
s=input().strip()
arr=[[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
l=len(s)
for i in range(r):
    for j in range(c):
        if m[i][j]==s[0]:
            if find_word(i,j,1,[[i,j]]):
                print("YES")
                exit()
print("NO")
