"""
The program must accept an integer matrix of size RxC as the input. The program must print all possible non-overlapping square submatrices in the given matrix as the output. The
non-overlapping square submatrices must be printed in increasing order of size. 

Boundary Condition(s):
2 <= R, C <= 30

Input Format:
The first line contains R and C separated by a space. 
The next R lines, each contains C integers separated by a space. 

Output Format: 
The lines containing the non-overlapping square submatrices.

Example Input/Output 1: 
Input:
4 5
48 89 68 28 30
93 89 98 37 68
29 67 70 21 12
32 19 72 89 53

Output:
48 89 
93 89
68 28
98 37
29 67
32 19
70 21
72 89
48 89 68
93 89 98
29 67 70
48 89 68 28
93 89 98 37
29 67 70 21
32 19 72 89

Explanation:
In the given 4x5 matrix, the non-overlapping square submatrices are given below.
48 89
93 89
68 28
98 37
29 67
32 19
70 21
72 89
48 89 68
93 89 98
29 67 70
48 89 68 28 
93 89 98 37 
29 67 70 21 
32 19 72 89 

Example Input/Output 2:
Input:
5 6
61 65 85 18 56 19 
17 81 21 40 23 35 
16 79 12 62 59 51 
33 49 25 24 93 47 
71 50 63 86 29 66 

Output: 
61 65
17 81
85 18
21 40
56 19
23 35
16 79
33 49
12 62
25 24
59 51
93 47
61 65 85
17 81 21
16 79 12
18 56 19
40 23 35
62 59 51
61 65 85 18
17 81 21 40
16 79 12 62
33 49 25 24
61 65 85 18 56
17 81 21 40 23
16 79 12 62 59
33 49 25 24 93
71 50 63 86 29
"""
r,c=map(int,input().split())
m=[input().split() for _ in range(r)]
n=2
minimum=min(r,c)
while n<=minimum:
    for i in range(0,r-n+1,n):
        for j in range(0,c-n+1,n):
            for ii in range(i,i+n):
                print(*m[ii][j:j+n])
    n+=1
