"""
A M*N matrix having M rows and N columns containing integer values is passed as the input. The matrix must be rotated R times in counter-clock (anti-clock) wise direction and
the resulting matrix must be printed as the output.

Input Format:
The first line will contain the value of M, N and R, each separated by a space. (M is the number of rows, N is the number of cols and R is the rotation count)
The next M lines will contain N integer values

Output Format:
M lines with each line containing N integer values of the rotated matrix (with each value separated by a space).

Constraints:
2 <= M <= 300
2 <= N <= 300
1 <= R <= 10^9
Values of integers in the matrix is from 1 to 10000000

Example Input/Output 1:
Input:
4 4 1
1 2 3 4
5 6 7 8
9 10 11 12
100 101 102 103

Output:
2 3 4 8
1 7 11 12
5 6 10 103
9 100 101 102

Example Input/Output 2:
Input:
5 4 7
1 2 3 4
7 8 9 10
13 14 15 16
19 20 21 22
25 26 27 30

Output:
30 27 26 25
22 9 15 19
16 8 21 13
10 14 20 7
4 3 2 1
"""
m,n,r=map(int,input().split())
mat=[input().split() for _ in range(m)]
rs=cs=0
re=m
ce=n
while rs<re and cs<ce:
    l=[]
    size=(re-rs-2)*2+(ce-cs)*2
    for j in range(cs,ce):
        l.append(mat[rs][j])
    for i in range(rs+1,re):
        l.append(mat[i][ce-1])
    for j in range(ce-2,cs-1,-1):
        l.append(mat[re-1][j])
    for i in range(re-2,rs,-1):
        l.append(mat[i][cs])
    l=l[r%size:]+l[:r%size]
    for j in range(cs,ce):
        mat[rs][j]=l.pop(0)
    rs+=1
    for i in range(rs,re):
        mat[i][ce-1]=l.pop(0)
    ce-=1
    for j in range(ce-1,cs-1,-1):
        mat[re-1][j]=l.pop(0)
    re-=1
    for i in range(re-1,rs-1,-1):
        mat[i][cs]=l.pop(0)
    cs+=1
for i in mat:
    print(*i)
