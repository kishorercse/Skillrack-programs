"""
The program must accept an integer matrix of size R*C and an integer K as the input. The matrix contains only 0s and 1s. The values of R and C are always divisible by K. For
each K*K submatrix, the program must print an integer whose binary representation is formed using the bits in the submatrix.

Boundary Condition(s):
2 <= R, C <= 50
1 <= K <= 5

Input Format:
The first line contains R and C separated by a space.
The next R lines each contains C integer values separated by a space.
The R+2nd line contains K.

Output Format:
The first R/K lines, each contains C/K integer values separated by a space.

Example Input/Output 1:
Input:
4 4
1 0 0 1
1 1 0 1
1 1 0 1
1 0 1 0
2

Output:
11 5
14 6

Explanation:
1st submatrix -> 1011 -> 11.
2nd submatrix -> 0101 -> 5.
3rd submatrix -> 1110 -> 14.
4th submatrix -> 0110 -> 6.
Hence the output is
11 5
14 6

Example Input/Output 2:
Input:
6 9
0 0 1 1 1 1 0 0 1
0 0 1 0 1 1 1 0 0
0 0 0 0 1 1 1 1 1
0 1 0 0 1 1 1 0 0
0 0 1 0 1 1 1 1 0
1 1 0 0 0 1 1 1 1
3

Output:
72 475 103
142 217 311
"""
r,c=map(int,input().split())
m=[input().split() for _ in range(r)]
k=int(input())
for i in range(0,r,k):
    for j in range(0,c,k):
        s=''
        for ii in range(i,i+k):
            for jj in range(j,j+k):
                s+=m[ii][jj]
        print(int(s,2),end=' ')
    print()
