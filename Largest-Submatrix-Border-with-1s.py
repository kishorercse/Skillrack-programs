"""
The program must accept an integer matrix of size R*C containing only 0s and 1s as the input. The program must print the size of the largest square submatrix of the minimum 
size 2 where all the elements in the border are 1s. If there is no such submatrix, then the program must print -1 as the output.

Boundary Condition(s):
2 <= R, C <= 50

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C integer values separated by a space.

Output Format:
The first line contains an integer value representing the size of the largest square submatrix or -1 based on the given conditions.

Example Input/Output 1:
Input:
6 8
0 0 0 0 0 1 1 0
1 1 1 0 0 0 0 0
0 0 1 1 1 1 1 1
1 1 1 1 0 1 1 0
1 1 0 1 0 1 1 0
0 0 0 1 1 1 1 1

Output:
4

Explanation:
The largest square submatrix of size 4*4 with 1s in the border is highlighted below.
0 0 0 0 0 1 1 0
1 1 1 0 0 0 0 0
0 0 1 1 1 1 1 1
1 1 1 1 0 1 1 0
1 1 0 1 0 1 1 0
0 0 0 1 1 1 1 1

Example Input/Output 2:
Input:
4 3
1 1 0
1 0 1
0 1 1
1 1 0

Output:
-1
"""
r,c=map(int,input().split())
m=[list(map(int,input().split())) for _ in range(r)]
mn=min(r,c)
for k in range(mn,1,-1):
    for i in range(r-k+1):
        for j in range(c-k+1):
            if all((m[i][jj]==1 and m[i+k-1][jj]==1) for jj in range(j,j+k)) and all((m[ii][j]==1 and m[ii][j+k-1]==1) for ii in range(i+1,i+k-1)):
                print(k)
                exit()
print(-1)
