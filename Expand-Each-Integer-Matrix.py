"""
The program must accept an integer matrix of size R*C containing four-digit integers as the input. The program must expand each integer into a 2*2 matrix and print the
resulting matrix as the output.

Boundary Condition(s):
2 <= R, C <= 50

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C integers separated by a space.

Output Format:
The first R*2 lines, each contains C*2 integers separated by a space.

Example Input/Output 1:
Input:
4 3
3676 4456 8509
6922 4111 4576
9724 6332 1380
1400 7858 6076

Output:
3 6 4 4 8 5
7 6 5 6 0 9
6 9 4 1 4 5
2 2 1 1 7 6
9 7 6 3 1 3
2 4 3 2 8 0
1 4 7 8 6 0
0 0 5 8 7 6

Explanation:
The 4*3 integer matrix is given below.
3676 4456 8509
6922 4111 4576
9724 6332 1380
1400 7858 6076
After expanding each integer into a 2*2 matrix, the matrix becomes
3 6 4 4 8 5
7 6 5 6 0 9
6 9 4 1 4 5
2 2 1 1 7 6
9 7 6 3 1 3
2 4 3 2 8 0
1 4 7 8 6 0
0 0 5 8 7 6

Example Input/Output 2:
Input:
2 2
1234 4567
6547 2345

Output:
1 2 4 5
3 4 6 7
6 5 2 3
4 7 4 5
"""
r,c=map(int,input().split())
m=[input().split() for _ in range(r)]
for i in range(2*r):
    x=2*(i%2)
    for j in range(2*c):
        print(m[i//2][j//2][x],end=' ')
        x+=1
        if x==4:
            x=2
        elif x==2:
            x=0
    print()
