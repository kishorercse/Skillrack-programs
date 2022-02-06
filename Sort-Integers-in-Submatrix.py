"""
The program must accept an integer matrix of size R*C and two integers X, Y as the input. The integers X and Y represent the bottom-left position of a submatrix of size
X*(C-Y+1). The program must sort the integers in the specified submatrix. Then the program must print the revised matrix as the output.

Boundary Condition(s):
2 <= R, C <= 50
1 <= Matrix element value <= 10^5
1 <= X <= R
1 <= Y <= C

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C integers separated by a space.
The R+2nd line contains X and Y separated by a space.

Output Format:
The first R lines contain the revised matrix.

Example Input/Output 1:
Input:
5 6
90 49 77 41 32 21
67 71 69 14 94 28
60 87 92 42 88 26
34 75 33 66 51 86
38 99 15 81 97 55
3 4

Output:
90 49 77 14 21 26
67 71 69 28 32 41
60 87 92 42 88 94
34 75 33 66 51 86
38 99 15 81 97 55

Explanation:
Here R=5, C=6, X=3 and Y=4.
The submatrix of size 3*3(i.e., 3*(6-4+1)) with the bottom-left position as (3, 4) is highlighted below.
90 49 77 41 32 21
67 71 69 14 94 28
60 87 92 42 88 26
34 75 33 66 51 86
38 99 15 81 97 55
After sorting the integers in the specified submatrix, the matrix becomes
90 49 77 14 21 26
67 71 69 28 32 41
60 87 92 42 88 94
34 75 33 66 51 86
38 99 15 81 97 55

Example Input/Output 2:
Input:
7 7
88 24 23 61 45 81 29
32 31 90 91 82 92 89
82 10 32 21 21 75 59
87 71 73 59 91 58 70
54 74 57 23 24 83 26
56 24 48 47 51 29 23
48 80 83 54 97 88 25
4 3

Output:
88 24 21 21 23 29 32
32 31 45 58 59 59 61
82 10 70 73 75 81 82
87 71 89 90 91 91 92
54 74 57 23 24 83 26
56 24 48 47 51 29 23
48 80 83 54 97 88 25
"""
r,c=map(int,input().split())
m=[list(map(int,input().split())) for _ in range(r)]
x,y=map(int,input().split())
col=y-1
size=x*col
l=[]
for i in range(x):
    for j in range(col,c):
        l.append(m[i][j])
l.sort()
for i in range(x):
    for j in range(col,c):
        m[i][j]=l.pop(0)
for i in m:
    print(*i)
