"""
This is a typical chess game where your opponent first places a random number of Knights, Rooks, Bishops and Queens on an NxN chessboard and then you have to place your king 
safely on the chessboard such that it should not be under attack by any piece.

The program must accept an integer N representing the size of a chessboard and the indices of K Knights, R Rooks, B Bishops and Q Queens as the input. The program must print 
the number of squares on the chessboard such that your King is not attacked by any of your opponent’s pieces.

Note:
The Knight moves two squares horizontally or vertically and then one more square at a right-angle.
The Rook moves in a straight line either horizontally or vertically.
The Bishop moves in a straight line diagonally on the board.
The Queen moves in a straight line either vertically, horizontally or diagonally.

Boundary Condition(s):
2 <= N <= 50
0 <= K + R + B + Q <= N*N
0 <= Indices of each piece <= N-1

Input Format:
The first line contains N.
The next line contains K, number of Knights. The next K lines, each contains two integers denoting the indices of the Knights.
The next line contains R, number of Rooks. The next R lines, each contains two integers denoting the indices of the Rooks.
The next line contains B, number of Bishops. The next B lines, each contains two integers denoting the indices of the Bishops.
The next line contains Q, number of Queens. The next Q lines, each contains two integers denoting the indices of the Queens.

Output Format:
The first line contains an integer representing the number of squares where King can be placed safely.

Example Input/Output 1:
Input:
4
2
0 0
1 1
1
2 2
0
1
3 3

Output:
2

Explanation:
The 4×4 chessboard with 2 Knights, 1 Rook and 1 Queen is given below.
K * * *
* K * *
* * R *
* * * Q
Each asterisk in the above chessboard indicates an empty square.
There are two squares to keep the king safe. i.e., (0, 1) and (1, 0).
K S * *
S K * *
* * R *
* * * Q
S indicates a safe position to place the King.

Example Input/Output 2:
Input:
8
4
2 6
3 2
5 6
7 7
4
2 2
4 6
6 4
7 5
4
0 4
1 1
1 6
5 1
2
3 5
6 0

Output
5

Explanation:
The 8×8 chessboard with 4 Knights, 4 Rooks, 4 Bishops and 2 Queens is given below.
* * * * B * * *
* B * * * * B *
* * R * * * K *
* * K * * Q * *
* * * * * * R *
* B * * * * K *
Q * * * R * * *
* * * * * R * K
Each asterisk in the above chessboard indicates an empty square.
There are five squares to keep the king safe. i.e., (0, 1), (0, 3), (1, 7), (3, 1) and (5, 7).
* S * S B * * *
* B * * * * B S
* * R * * * K *
* S K * * Q * *
* * * * * * R *
* B * * * * K S
Q * * * R * * *
* * * * * R * K
S indicates a safe position to place the King.

Example Input/Output 3:
Input:
3
1
0 2
1
0 0
2
2 2
1 0
0

Output:
2
"""
def knight(a,b):
    if a<n-2:
        if b>=1 and m[a+2][b-1]=='*':
            m[a+2][b-1]=True
        if b<n-1 and m[a+2][b+1]=='*':
            m[a+2][b+1]=True
    if a>=2:
        if b>=1 and m[a-2][b-1]=='*':
            m[a-2][b-1]=True
        if b<n-1 and m[a-2][b+1]=='*':
            m[a-2][b+1]=True
    if b<n-2:
        if a>=1 and m[a-1][b+2]=='*':
            m[a-1][b+2]=True
        if a<n-1 and m[a+1][b+2]=='*':
            m[a+1][b+2]=True
    if b>=2:
        if a>=1 and m[a-1][b-2]=='*':
            m[a-1][b-2]=True
        if a<n-1 and m[a+1][b-2]=='*':
            m[a+1][b-2]=True
def rook(a,b):
    x,y=a-1,b-1
    f1=f2=True
    while x>=0 or y>=0:
        if f1 and x>=0:
            if m[x][b]=='*' or m[x][b]==True:
                m[x][b]=True
            else:
                f1=False
        if f2 and y>=0:
            if m[a][y]=='*' or m[a][y]==True:
                m[a][y]=True
            else:
                f2=False
        x-=1
        y-=1
    x,y=a+1,b+1
    f1=f2=True
    while x<n or y<n:
        if f1 and x<n:
            if m[x][b]=='*' or m[x][b]==True:
                m[x][b]=True
            else:
                f1=False
        if f2 and y<n:
            if m[a][y]=='*' or m[a][y]==True:
                m[a][y]=True
            else:
                f2=False
        x+=1
        y+=1
def bishop(a,b):
    x,y,z=a-1,b-1,b+1
    f1=f2=True
    while x>=0 and (y>=0 or z<n):
        if f1 and y>=0:
            if m[x][y]=='*' or m[x][y]==True:
                m[x][y]=True
            else:
                f1=False
        if f2 and z<n:
            if m[x][z]=='*' or m[x][z]==True:
                m[x][z]=True
            else:
                f2=False
        x-=1
        y-=1
        z+=1
    x,y,z=a+1,b-1,b+1
    f1=f2=True
    while x<n and (y>=0 or z<n):
        if f1 and y>=0:
            if m[x][y]=='*' or m[x][y]==True:
                m[x][y]=True
            else:
                f1=False
        if f2 and z<n:
            if m[x][z]=='*' or m[x][z]==True:
                m[x][z]=True
            else:
                f2=False
        x+=1
        y-=1
        z+=1
n=int(input())
m=[['*']*n for _ in range(n)]
t="KRBQ"
safe=0
for i in range(4):
    ctr=int(input())
    while ctr>0:
        x,y=map(int,input().split())
        m[x][y]=t[i]
        ctr-=1
for i in range(n):
    for j in range(n):
        if m[i][j]=='K':
            knight(i,j)
        elif m[i][j]=='R':
            rook(i,j)
        elif m[i][j]=='B':
            bishop(i,j)
        elif m[i][j]=='Q':
            rook(i,j)
            bishop(i,j)
for i in range(n):
    for j in range(n):
        if m[i][j]=='*':
            safe+=1
print(safe)
