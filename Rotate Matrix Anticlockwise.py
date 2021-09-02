"""
The program must accept an integer matrix of size NxN as the input. The program must rotate the given matrix by 90 degree in anticlockwise direction. Finally, the program must print modified matrix as the output.

Boundary Condition(s):
1 <= N <= 100
1 <= Matrix Element Value <= 9999999

Input Format:
The first line contains the value of N.
The next N lines contain N integers separated by space(s).

Output Format:
The first N lines contain N integers of the modified matrix separated by space(s).

Example Input/Output 1:
Input:
3
45 10 98
75 58 85
94 44 91

Output:
98 85 91
10 58 44
45 75 94

Example Input/Output 2:
Input:
6
91 92 59 10 40 87
73 31 44 64 24 57
12 67 61 93 25 46
53 28 37 11 98 35
84 51 99 41 54 89
96 43 18 23 33 16

Output:
87 57 46 35 89 16
40 24 25 98 54 33
10 64 93 11 41 23
59 44 61 37 99 18
92 31 67 28 51 43
91 73 12 53 84 96
"""
n=int(input())
m=[input().split() for _ in range(n)]
for j in range(n-1,-1,-1):
    for i in range(n):
        print(m[i][j],end=' ')
    print()
