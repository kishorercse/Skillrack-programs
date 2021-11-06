"""
There is a large rectangular grid of length L and breadth B. The side which represents the breadth is perpendicular to X axis. A painter paints N smaller rectangular grids which
are within the above large rectangular grid with different colours. The co-ordinates of the smaller rectangular grids which are painted are passed as the input to the program. 
The top-left, bottom-left, top-right, bottom-right co-ordinates can be passed in any order and the x and y co-ordinates positions are relative to the bottom-left position of the 
larger rectangular grid. The program must finally print the painted unit rectangular grids represented by an asterisk * and the unpainted rectangular grids by a hash # 

Boundary Condition(s): 
1 <= L, B, N <= 100 

Input Format: 
The first line contains L and B separated by a space. 
The second line contains N.
The next N*4 lines contain the co-ordinates of the smaller rectangular grids being painted. 

Output Format:
B lines containing L columns represented by * or # 

Example Input/Output 1: 
Input: 
10 10
2
2 5
2 10
7 5
7 10
3 6
3 2
6 6
6 2

Output:
##*****###
##*****###
##*****###
##*****###
##*****###
###***####
###***####
###***####
##########
##########
"""
l,b=map(int,input().split())
n=int(input())
m=[['#']*l for _ in range(b)]
for _ in range(n):
    x1=y1=101
    x2=y2=-1
    for _ in range(4):
        p,q=map(int,input().split())
        x1=min(p,x1)
        x2=max(p,x2)
        y1=min(q,y1)
        y2=max(q,y2)
    for i in range(y1,y2):
        for j in range(x1,x2):
            m[i][j]='*'
for i in range(b-1,-1,-1):
    print(*m[i],sep='')
