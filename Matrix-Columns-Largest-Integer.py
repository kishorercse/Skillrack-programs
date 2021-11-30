"""
The program must accept a matrix of size R*C containing distinct values and must print the columns which are having a value which is the largest in a given row.

Boundary Condition(s):
2 <= R, C <= 50
1 <= Matrix element value <= 10^5

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C integers separated by a space.

Output Format:
The first R lines contain the integer values based on the given conditions.

Example Input/Output 1:
Input:
4 5
60 100 59 46 70
90 64 11 91 88
86 51 7 37 89
23 34 32 20 2

Output:
100 46 70 
64 91 88
51 37 89
34 20 2

Explanation:
Max value in Row 1 is 100 which is in column 2.
Max value in Row 2 is 91 which is in column 4.
Max value in Row 3 is 89 which is in column 5.
Max value in Row 4 is 34 which is in column 2.
Hence the columns 2, 4 and 5 are printed.

Example Input/Output 2:
Input:
5 8
73 68 16 10 80 44 22 89
81 84 15 64 99 75 46 56
87 11 40 24 97 58 17 71
48 37 26 65 50 18 59 25
19 57 36 83 13 92 31 39

Output:
10 80 44 89
64 99 75 56
24 97 58 71
65 50 18 25
83 13 92 39
"""
r,c=map(int,input().split())
m=[list(map(int,input().split())) for _ in range(r)]
cols=[False]*c
for i in range(r):
    mx=-1
    maxCol=-1
    for j in range(c):
        if m[i][j]>mx:
            mx=m[i][j]
            maxCol=j
    cols[maxCol]=True
for i in range(r):
    for j in range(c):
        if cols[j]:
            print(m[i][j],end=' ')
    print()
