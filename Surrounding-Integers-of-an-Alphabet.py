"""
The program must accept a matrix of size NxN as the input. The matrix always contains exactly one alphabet CH and the remaining are integers. The program must print the
surrounding integers of the alphabet CH in clockwise direction as the output.

Boundary Condition(s):
2 <= N <= 100

Input Format:
The first line contains N.
The next N lines contain the matrix.

Output Format:
The first line contains the surrounding integers of the alphabet CH.

Example Input/Output 1:
Input:
5
66 32 22 31 90
34 16 12 56 77
64 18 72 40 44
14 y 58 58 11
31 30 79 11 18

Output:
64 18 72 58 79 30 31 14

Explanation:
The surrounding integers of the alphabet y are highlighted below.
66 32 22 31 90
34 16 12 56 77
64 18 72 40 44
14 y 58 58 11
31 30 79 11 18
Now, the surrounding integers of y are printed in the clockwise direction.

Example Input/Output 2:
Input:
6
5 1 9 8 9 8
2 4 6 2 2 3
3 2 5 3 8 19
6 8 9 2 1 3
9 8 7 6 5 3
16 3 4 7 20 b

Output:
5 3 20
"""
n=int(input())
m=[input().split() for _ in range(n)]
f=False
for i in range(n):
    for j in range(n):
        if m[i][j].isalpha():
            if (i>=1):
                if j>=1:
                    print(m[i-1][j-1],end=' ')
                print(m[i-1][j],end=' ')
                if j+1<n:
                    print(m[i-1][j+1],end=' ')
            if j+1<n:
                print(m[i][j+1],end=' ')
            if i+1<n:
                if j+1<n:
                    print(m[i+1][j+1],end=' ')
                print(m[i+1][j],end=' ')
                if j-1>=0:
                    print(m[i+1][j-1],end=' ')
            if j-1>=0:
                print(m[i][j-1],end=' ')
            f=True
            break
    if f:
        break
