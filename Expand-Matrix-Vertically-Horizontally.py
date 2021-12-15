"""
The program must accept a character matrix of size R*C and an integer K as the input. The program must expand the matrix horizontally so that each character in the rows repeated K times if K is positive. Else the program must expand the matrix vertically so that each character in the columns repeated K times. Finally, the program must print the expanded matrix as the output.

Note: The value of K is always a nonzero value.

Boundary Condition(s):
1 <= R, C <= 50
-50 <= K <= 50

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C characters separated by a space.
The R+2nd line contains K.

Output Format:
The lines contain the expanded matrix based on the given conditions.

Example Input/Output 1:
Input:
3 3
a b c
d e f
g h i
4

Output:
a a a a b b b b c c c c
d d d d e e e e f f f f
g g g g h h h h i i i i

Explanation:
Here K = 4, which is a positive value.
So the matrix is expanded horizontally as given below.
a a a a b b b b c c c c
d d d d e e e e f f f f
g g g g h h h h i i i i

Example Input/Output 2:
Input:
3 3
A B C
P Q R
X Y Z
-4

Output:
A B C
A B C
A B C
A B C
P Q R
P Q R
P Q R
P Q R
X Y Z
X Y Z
X Y Z
X Y Z
"""
r,c=map(int,input().split())
m=[input().split() for _ in range(r)]
k=int(input())
if k>0:
    for i in range(r):
        for j in range(c):
            for ctr in range(k):
                print(m[i][j],end=' ')
        print()
else:
    k=-k
    for i in range(r):
        for ctr in range(k):
            print(*m[i])
