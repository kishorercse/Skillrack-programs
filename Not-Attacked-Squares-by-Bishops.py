"""
In an empty NxN chessboard, certain bishops are placed in different squares. A bishop can move along the main diagonal or opposite diagonal. Hence all the squares along the main diagonal or opposite diagonal in which the bishop can travel can be attacked by the bishop. The program must accept an integer matrix representing the chessboard as the input. The program must print the number of squares that are NOT attacked by the bishops places in the chessboard. 1 indicates the placement of a bishop in the chessboard and 0 indicates the empty squares.

Boundary Condition(s):
2 <= N <= 1000

Input Format:
The first line contains N.
The next N lines each contain N integers separated by a space.

Output Format:
The first line contains the number of squares that are NOT attacked by the bishops places in the chessboard.

Example Input/Output 1:
Input:
5
0 0 0 1 0
1 0 0 0 0
0 0 1 0 0
0 0 0 0 0
1 0 0 0 0

Output:
7

Explanation:
The squares which are NOT attacked by the bishops are represented by a X. As 7 squares are not attacked the output is 7.
0 0 X 1 0
1 0 0 0 0
X 0 1 X X
0 0 0 0 X
1 X X 0 0

Example Input/Output 2:
Input:
7
0 0 0 0 0 0 1
0 1 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0 
0 0 0 0 0 0 0
0 1 0 0 0 0 0
0 0 0 0 0 0 0

Output:
32
"""
n=int(input())
m=[list(map(int,input().split())) for _ in range(n)]
notAttacked=n*n
for i in range(n):
    for j in range(n):
        if m[i][j]==1:
            notAttacked-=1
            a,b,c=i-1,j-1,j+1
            while a>=0 and (b>=0 or c<n):
                if b>=0:
                    if m[a][b]==1:
                        b=-1
                    elif m[a][b]!=-1:
                        m[a][b]=-1
                        notAttacked-=1
                if c<n:
                    if m[a][c]==1:
                        c=n
                    elif m[a][c]!=-1:
                        m[a][c]=-1
                        notAttacked-=1
                a-=1
                b-=1
                c+=1
            a,b,c=i+1,j-1,j+1
            while a<n and (b>=0 or c<n):
                if b>=0:
                    if m[a][b]==1:
                        b=-1
                    elif m[a][b]!=-1:
                        m[a][b]=-1
                        notAttacked-=1
                if c<n:
                    if m[a][c]==1:
                        c=n
                    elif m[a][c]!=-1:
                        m[a][c]=-1
                        notAttacked-=1
                a+=1
                b-=1
                c+=1
print(notAttacked)
