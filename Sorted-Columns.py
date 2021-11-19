"""
The program must accept an integer matrix of size RxC as the input. The program must print the columns of the matrix having the integers in ascending order. If there is no such 
column, the program must print -1 as the output. 

Boundary Condition(s):
2 <= R, C <= 50

Input Format:
The first line contains R and C separated by a space.
The next R lines, each containing C integers separated by a space. 

Output Format:
The lines containing the columns of the matrix having the integers in ascending order. 

Example Input/Output 1: 
Input:
5 6
15 27 38 79 31 99
18 13 84 31 46 98
31 89 81 70 77 97
45 86 14 81 77 97
88 86 37 64 82 96

Output:
15 31
18 46
31 77
45 77
88 82

Explanation: 
The integers in the first column and the fifth column of the matrix are in ascending order. 
Hence the first column and the fifth column of the matrix are printed as the output. 

Example Input/Output 2:
Input:
6 6
84 44 48 10 27 61
34 52 33 60 86 47
98 20 47 66 41 33
80 28 38 59 44 37
62 14 71 81 13 66
74 27 54 73 61 12 

Output: 
-1
"""
r,c=map(int,input().split())
m=[list(map(int,input().split())) for _ in range(r)]
col=[False]*c
flag=False
for j in range(c):
    if all(m[i-1][j]<=m[i][j] for i in range(1,r)):
        col[j]=True
        flag=True
if flag:
    for i in range(r):
        for j in range(c):
            if col[j]:
                print(m[i][j],end=' ')
        print()
else:
    print(-1)
