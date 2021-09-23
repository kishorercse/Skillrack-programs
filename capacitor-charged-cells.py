"""
The program must accept an integer matrix of size R*C consisting of only 1s and 0s. 1 indicates that the cell has a
capacitor that will charge the current cell as well as the 8 possible surrounding cells. The program must mark the
charged cells with C. Finally the program must print the matrix state as the output.

Boundary Condition(s):
2 <= R,C <= 50

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C integer values separated by a space. 

Output Format: 
The first R lines contain the state of the matrix. 

Example Input/Output 1: 
Input: 
3 4 
0 1 0 1 
0 0 0 0 
0 0 0 1 

Output: 
C C C C 
C C C C 
0 0 C C 

Explanation: 
Here R=3, C=4 and the given 3*4 integer matrix is 
0 1 0 1 
0 0 0 0 
0 0 0 1 
The cells that are charged using the capacitors are highlighted below. 
C C C C
C C C C 
0 0 C C 

Example Input/Output 2: 
Input: 
3 4
0 0 0 1 
0 0 0 0 
0 0 0 1 

Output: 
0 0 C C 
0 0 C C 
0 0 C C
"""
r,c=map(int,input().split())
m=[list(map(int,input().split())) for _ in range(r)]
t=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
for i in range(r):
    for j in range(c):
        if m[i][j]==1:
            for x,y in t:
                a=i+x
                b=j+y
                if 0<=a<r and 0<=b<c and m[a][b]!=1:
                    m[a][b]='C'
            m[i][j]='C'
for i in m:
    print(*i)
