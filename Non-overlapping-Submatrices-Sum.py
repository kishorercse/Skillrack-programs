"""
The program must accept an integer matrix of size R*C and two integer X, Y as the input. The program must print the sum of integers in all X*Y non-overlapping submatrices
as the output.

Boundary Condition(s):
2 <= X <= R <= 50
2 <= Y <= C <= 50
1 <= Matrix element value <= 1000

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C integers separated by a space.
The (R+2)th line contains X and Y separated by a space.

Output Format:
The first line contains the integer values representing the sum of integers in all the X*Y non-overlapping submatrices.

Example Input/Output 1:
Input:
10 9
5 7 5 3 2 9 5 1 6
3 7 6 2 5 9 6 9 2
3 7 8 9 7 3 9 6 6
6 2 3 9 1 4 5 2 9
9 4 3 7 8 5 2 2 5
9 1 8 9 6 3 2 9 2
8 2 3 8 9 7 3 9 1
1 8 6 9 4 6 5 3 1
3 7 8 9 7 9 2 6 9
8 9 2 5 9 5 3 1 8
4 4

Output:
85 83 95 83

Explanation:
Here R = 10, C = 9, X = 4 and Y = 4.
The sum of integers in the first 4*4 non-overlapping submatrix is 85 and the submatrix is highlighted below.
5 7 5 3 2 9 5 1 6
3 7 6 2 5 9 6 9 2
3 7 8 9 7 3 9 6 6
6 2 3 9 1 4 5 2 9
9 4 3 7 8 5 2 2 5
9 1 8 9 6 3 2 9 2
8 2 3 8 9 7 3 9 1
1 8 6 9 4 6 5 3 1
3 7 8 9 7 9 2 6 9
8 9 2 5 9 5 3 1 8
The sum of integers in the second 4*4 non-overlapping submatrix is 83 and the submatrix is highlighted below.
5 7 5 3 2 9 5 1 6
3 7 6 2 5 9 6 9 2
3 7 8 9 7 3 9 6 6
6 2 3 9 1 4 5 2 9
9 4 3 7 8 5 2 2 5
9 1 8 9 6 3 2 9 2
8 2 3 8 9 7 3 9 1
1 8 6 9 4 6 5 3 1
3 7 8 9 7 9 2 6 9
8 9 2 5 9 5 3 1 8
The sum of integers in the third 4*4 non-overlapping submatrix is 95 and the submatrix is highlighted below.
5 7 5 3 2 9 5 1 6
3 7 6 2 5 9 6 9 2
3 7 8 9 7 3 9 6 6
6 2 3 9 1 4 5 2 9
9 4 3 7 8 5 2 2 5
9 1 8 9 6 3 2 9 2
8 2 3 8 9 7 3 9 1
1 8 6 9 4 6 5 3 1
3 7 8 9 7 9 2 6 9
8 9 2 5 9 5 3 1 8
The sum of integers in the fourth 4*4 non-overlapping submatrix is 83 and the submatrix is highlighted below.
5 7 5 3 2 9 5 1 6
3 7 6 2 5 9 6 9 2
3 7 8 9 7 3 9 6 6
6 2 3 9 1 4 5 2 9
9 4 3 7 8 5 2 2 5
9 1 8 9 6 3 2 9 2
8 2 3 8 9 7 3 9 1
1 8 6 9 4 6 5 3 1
3 7 8 9 7 9 2 6 9
8 9 2 5 9 5 3 1 8
Hence the output is
85 83 95 83

Example Input/Output 2:
Input:
7 7
9 4 7 9 4 2 8
1 3 3 9 7 2 1
9 2 8 6 4 5 2
2 8 3 2 3 3 5
1 1 4 1 9 6 8
7 6 2 7 3 7 9
8 2 9 7 7 7 6
3 2

Output:
28 42 24 25 19 31
"""
r,c=map(int,input().split())
m=[list(map(int,input().split())) for _ in range(r)]
x,y=map(int,input().split())
for i in range(0,r-x+1,x):
    for j in range(0,c-y+1,y):
        s=0
        for ii in range(i,i+x):
            s+=sum(m[ii][j:j+y])
        print(s,end=' ')
