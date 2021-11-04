"""
The program must accept an integer matrix of size R*C as the input. The program must reverse every second column in the matrix. Then the program must print the modified matrix as
the output. 

Boundary Condition(s):
2 <= R, C <= 50 

Input Format:
The first line contains R and C separated by a space. 
The next R lines, each contains C integers separated by a space.

Output Format: 
The first R lines, each contains C integers separated by a space. 

Example Input/Output 1: 
Input: 
4 5
51 74 71 32 14 
31 78 51 45 67 
87 96 77 10 26
70 72 93 39 31 

Output: 
51 72 71 39 14
31 96 51 10 67 
87 78 77 45 26 
70 74 93 32 31 

Explanation:
Here R = 4 and C = 5. 
After reversing the columns 2 and 4, the matrix becomes 
51 72 71 39
14 31 96 51
10 67 87 78
77 45 26 70
74 93 32 31

Example Input/Output 2:
Input: 
5 8
64 47 33 18 33 80 92 50
17 99 56 45 31 92 61 80
70 82 45 27 93 26 46 72
45 40 67 59 55 57 73 56
74 62 71 16 36 51 35 21

Output:
64 62 33 16 33 51 92 21
17 40 56 59 31 57 61 56
70 82 45 27 93 26 46 72
45 99 67 45 55 92 73 80
74 47 71 18 36 80 35 50
"""
r,c=map(int,input().split())
m=[input().split() for _ in range(r)]
for j in range(1,c,2):
    a,b=0,r-1
    while a<b:
        m[a][j],m[b][j]=m[b][j],m[a][j]
        a+=1
        b-=1
for i in m:
    print(*i)
