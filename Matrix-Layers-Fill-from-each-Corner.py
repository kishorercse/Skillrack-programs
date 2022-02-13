"""
Matrix Layers - Fill from each Corner
The program must accept five integers A, B, C, D and N as the input. The value of N is always even. The program must form an integer matrix of size N*N. Then the program must 
fill the matrix layer by layer based on the following conditions.
- In each layer of the matrix, the program must fill the integers A, B, C and D at top-left, top-right, bottom-right and bottom-left corners respectively.
- In the top edge of each layer, the program must fill the remaining integers starting from A+1 (left to right).
- In the right edge of each layer, the program must fill the remaining integers starting from B+1 (top to bottom).
- In the bottom edge of each layer, the program must fill the remaining integers starting from C+1 (right to left).
- In the left edge of each layer, the program must fill the remaining integers starting from D+1 (bottom to top).
Finally, the program must print the N*N integer matrix as the output.

Boundary Condition(s):
1 <= A, B, C, D <= 10^3
2 <= N <= 50

Input Format:
The first line contains A, B, C and D separated by a space.
The second line contains N.

Output Format:
The first N lines contain the integer matrix.

Example Input/Output 1:
Input:
10 20 40 50
6

Output:
10 11 12 13 14 20
54 10 11 12 20 21
53 52 10 20 21 22
52 51 50 40 22 23
51 50 42 41 40 24
50 44 43 42 41 40

Explanation:
Here A = 10, B = 20, C = 40, D = 50 and N = 6.
So the 6*6 integer matrix is formed and filled with the integers based on the given conditions.
10 11 12 13 14 20
54 10 11 12 20 21
53 52 10 20 21 22
52 51 50 40 22 23
51 50 42 41 40 24
50 44 43 42 41 40

Example Input/Output 2:
Input:
11 51 61 31
8

Output:
11 12 13 14 15 16 17 51
37 11 12 13 14 15 51 52
36 35 11 12 13 51 52 53
35 34 33 11 51 52 53 54
34 33 32 31 61 53 54 55
33 32 31 63 62 61 55 56
32 31 65 64 63 62 61 57
31 67 66 65 64 63 62 61
"""
a,b,c,d=map(int,input().split())
n=int(input())
m=[[0]*n for _ in range(n)]
t=n-1
for ctr in range(n//2):
    i=j=ctr
    x=a
    for jj in range(j,t):
        m[i][jj]=x
        x+=1
    x=b
    for ii in range(i,t):
        m[ii][t]=x
        x+=1
    x=c
    for jj in range(t,j,-1):
        m[t][jj]=x
        x+=1
    x=d
    for ii in range(t,i,-1):
        m[ii][j]=x
        x+=1
    t-=1
for i in m:
    print(*i)
