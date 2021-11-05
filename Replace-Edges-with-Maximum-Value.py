"""
The program must accept an integer matrix of size RxC as the input. The program must replace each integer in all four edges(except the corners) with the maximum value present in 
the corresponding edges. Finally, the program must print the modified matrix as the output.

Boundary Condition(s):
4 <= R, C <= 50
1 <= Each integer value <= 10^4 

Input Format: 
The first line contains R and C separated by a space. 
The next R lines, each contains C integers separated by a space. 

Output Format: 
The first R lines, each contains C integers separated by a space.

Example Input/Output 1: 
Input:
5 6 
25 98 32 68 87 80
81 25 57 53 37 89
53 23 11 68 43 36
98 61 69 43 64 24
39 59 39 26 28 83

Output: 
25 98 98 98 98 80
98 25 57 53 37 89
98 23 11 68 43 89
98 61 69 43 64 89
39 59 59 59 59 83

Explanation: 
The maximum value in the top edge of the matrix is 98.
The maximum value in the right edge of the matrix is 89. 
The maximum value in the bottom edge of the matrix is 59. 
The maximum value in the left edge of the matrix is 98.
After replacing the edges, the matrix becomes 
25 98 98 98 98 80
98 25 57 53 37 89
98 23 11 68 43 89
98 61 69 43 64 89
39 59 59 59 59 83

Example Input/Output 2:
Input: 
7 7 
12 60 23 17 45 25 51
93 67 54 41 40 79 81
85 38 50 44 95 78 97
14 65 49 78 21 50 36
56 19 79 78 55 55 49
57 56 77 84 92 93 48
55 11 12 13 14 15 61

Output: 
12 60 60 60 60 60 51
93 67 54 41 40 79 97
93 38 50 44 95 78 97
93 65 49 78 21 50 97
93 19 79 78 55 55 97
93 56 77 84 92 93 97
55 15 15 15 15 15 61
"""
r,c=map(int,input().split())
m=[list(map(int,input().split())) for _ in range(r)]
a=max(m[0][1:-1])
b=max(m[r-1][1:-1])
for j in range(1,c-1):
    m[0][j]=a
    m[r-1][j]=b
a=b=0
for i in range(1,r-1):
    a=max(a,m[i][0])
    b=max(b,m[i][-1])
for i in range(1,r-1):
    m[i][0]=a
    m[i][-1]=b
for i in m:
    print(*i)
