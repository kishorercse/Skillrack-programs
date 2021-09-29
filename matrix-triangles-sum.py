"""
The program must accept an integer matrix of size N*N as the input. The program must print the sum of integers in the
upper triangular part of the matrix. Then the program must print the sum of integers in the lower triangular part of
the matrix. The integers in the bottom-left to top-right diagonal are common to both triangles.

Boundary Condition(s):
2 <= N <= 50
1 <= Matrix element value <= 10^4

Input Format:
The first line contains N.
The next N lines, each contains N integer values separated by a space.

Output Format: 
The first line contains the sum of integers in the upper triangular part of the matrix. 
The second line contains the sum of integers in the lower triangular part of the matrix. 

Example Input/Output 1: 
Input: 
4 
10 20 30 40 
50 60 70 80 
11 22 33 44 
55 66 77 88 

Output: 
368 
575 

Explanation: 
The integers in the upper triangular part of the matrix are highlighted below.
10 20 30 40 
50 60 70 80 
11 22 33 44 
55 66 77 88 
So their sum is 368. 
The integers in the lower triangular part of the matrix are highlighted below. 
10 20 30 40 
50 60 70 80 
11 22 33 44 
55 66 77 88 
So their sum is 575. 

Example Input/Output 2:
Input: 
5
32 93 88 17 21 
59 9 51 44 81 
59 61 53 31 61 
88 14 71 39 5 
46 90 81 43 4 

Output: 
735 
684
"""
n=int(input())
mat=[list(map(int,input().split())) for _ in range(n)]
up=low=0
for i in range(n):
    for j in range(n):
        if j<=n-i-1:
            up+=mat[i][j]
        if j>=n-i-1:
            low+=mat[i][j]
print(up,low,sep='\n')
