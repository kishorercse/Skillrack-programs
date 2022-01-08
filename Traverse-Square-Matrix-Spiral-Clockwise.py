"""
A square matrix of size N*N is provided. The program must traverse the matrix spirally and print the elements in a single line.

Input Format:
The first line contains N.
Next N lines, contain N column values C(i,j) each separated by a space.

Output Format:
The first line contains N*N values separated by a space.

Boundary Conditions:
2 <= N <= 100
0 <= C(i,j) <= 9999

Example Input/Output 1:
Input:
2
1 2
3 4

Output:
1 2 4 3

Example Input/Output 2:
Input:
4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

Output:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

Example Input/Output 3:
Input:
5
2 7 7 7 9
10 2 4 2 10
2 9 4 9 2
7 15 10 14 10
12 9 15 12 2

Output:
2 7 7 7 9 10 2 10 2 12 15 9 12 7 2 10 2 4 2 9 14 10 15 9 4
"""
n=int(input())
m=[input().split() for _ in range(n)]
rs,re=0,n
cs,ce=0,n
while rs<re and cs<ce:
    for j in range(cs,ce):
        print(m[rs][j],end=' ')
    rs+=1
    for i in range(rs,re):
        print(m[i][ce-1],end=' ')
    ce-=1
    for j in range(ce-1,cs,-1):
        print(m[re-1][j],end=' ')
    re-=1
    for i in range(re,rs-1,-1):
        print(m[i][cs],end=' ')
    cs+=1
