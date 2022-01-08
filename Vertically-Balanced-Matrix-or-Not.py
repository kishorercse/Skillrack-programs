"""
The program must accept an integer matrix of size R*C as the input. The program must print YES if the given matrix is balanced vertically. Else the program must print NO as
the output. The vertically balanced matrix is a matrix where the sum of the integers on the left part and right part are equal when the matrix is divided vertically.

Boundary Condition(s):
2 <= R, C <= 50
1 <= Matrix element value <= 10^5

Input Format:
The first line contains R and C separated by a space.
The next R lines each contains C integers separated by a space.

Output Format:
The first line contains YES or NO.

Example Input/Output 1:
Input:
4 4
10 4 4 5
10 5 3 4
20 3 5 3
10 6 2 6

Output:
YES

Explanation:
If the matrix is divided vertically as given below, then the sum of integers on the left part and right part are equal.
10 | 4 4 5
10 | 5 3 4
20 | 3 5 3
10 | 6 2 6
The sum of integers on the left part is 50.
The sum of integers on the right part is 50.
Hence the matrix is a vertically balanced matrix.

Example Input/Output 2:
Input:
3 5
7 1 8 9 8
5 3 5 7 7
2 8 3 3 8

Output:
YES

Explanation:
If the matrix is divided vertically as given below, then the sum of integers on the left part and right part are equal.
7 1 8 | 9 8
5 3 5 | 7 7
2 8 3 | 3 8
The sum of integers on the left part is 42.
The sum of integers on the right part is 42.
Hence the matrix is a vertically balanced matrix.

Example Input/Output 3:
Input:
3 3
1 2 3
6 5 4
7 8 9

Output:
NO
"""
r,c=map(int,input().split())
m=[list(map(int,input().split())) for _ in range(r)]
total=0
for i in m:
    total+=sum(i)
left=0
for j in range(c-1):
    for i in range(r):
        left+=m[i][j]
    if left==total-left:
        print("YES")
        break
else:
    print("NO")
