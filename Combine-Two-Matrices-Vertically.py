"""
The program must accept two integer matrices M1 and M2 are of equal size R*C as the input. The first column or the last column of M2 always occurs in M1. The program
must combine the given two matrices vertically based on that common column. Finally, the program must print the combined matrix as the output. The sum of integers 
must be printed in the common part of the combined matrix.
Note: There is always only one way to combine the given two matrices.

Boundary Condition(s):
2 <= R, C <= 50
1 <= Matrix element value <= 1000

Input Format:
The first line contains R and C separated by a space.
The next R lines from the 2nd line, each contains C integers separated by a space representing the matrix M1.
The next R lines from the R+2nd line, each contains C integers separated by a space representing the matrix M2.

Output Format:
The first R lines contain the integer values representing the combined matrix.

Example Input/Output 1:
Input:
6 4
7 6 5 9
1 2 1 1
2 3 5 8
1 1 7 5
7 3 7 9
5 3 8 9
8 2 4 6
6 3 2 2
9 6 5 3
5 1 2 1
7 7 4 3
7 5 6 3

Output:
8 2 11 12 5 9
6 3 3 4 1 1
9 6 7 6 5 8
5 1 3 2 7 5
7 7 11 6 7 9
7 5 11 6 8 9

Explanation:
The last column of M2 occurs in the 2nd column of M1.
The given matrices are combined based on the 2nd column of M1.

Example Input/Output 2:
Input:
3 4
92 75 40 18
19 53 20 64
90 74 10 32
40 38 49 73
20 49 43 55
10 38 26 74

Output:
92 75 80 56 49 73
19 53 40 113 43 55
90 74 20 70 26 74
"""
r,c=map(int,input().split())
m1=[list(map(int,input().split())) for _ in range(r)]
m2=[list(map(int,input().split())) for _ in range(r)]
for j in range(c):
    last=first=True
    for i in range(r):
        if m2[i][c-1]!=m1[i][j]:
            last=False
        if m2[i][0]!=m1[i][j]:
            first=False
        if not first and not last:
            break
    if first or last:
        col=j
        break
if first:
    j=col
    for m2_col in range(c):
        for i in range(r):
            if j<c:
                m1[i][j]+=m2[i][m2_col]
            else:
                m1[i].append(m2[i][m2_col])
        j+=1
    for i in m1:
        print(*i)
if last:
    m2_col=c-col-1
    for j in range(c):
        for i in range(r):
            if m2_col<c:
                m2[i][m2_col]+=m1[i][j]
            else:
                m2[i].append(m1[i][j])
        m2_col+=1
    for i in m2:
        print(*i)
