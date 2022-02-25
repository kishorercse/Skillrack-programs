"""
The program must accept an integer matrix of size R*C and four integers X, Y, P, Q as the input. The program must divide the matrix into nine submatrices based on the following
condition.
- The program must divide the matrix horizontally after the Xth row and Yth row. Then the program must divide the matrix vertically after the Pth column and Qth column.
Finally, the program must print the sum of integers in each submatrix as the output.

Boundary Condition(s):
3 <= R, C <= 50
1 <= Matrix element value <= 1000
1 <= X < Y < R
1 <= P < Q < C

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C integer values separated by a space.
The R+2nd line contains X, Y, P and Q separated by a space.

Output Format:
The first line contains nine integer values separated by a space representing the sum of integers in the nine submatrices.

Example Input/Output 1:
Input:
6 5
6 9 2 9 2
7 1 9 3 2
9 9 1 2 6
6 5 7 1 9
6 6 6 2 3
1 6 7 9 7
3 5 2 4

Output:
41 26 10 23 16 12 7 16 7

Explanation:
Here X = 3, Y = 5, P = 2 and Q = 4.
The nine submatrices and their sums are given below.
1st submatrix sum = 6 + 9 + 7 + 1 + 9 + 9 = 41.
6 9
7 1
9 9

2nd submatrix sum = 2 + 9 + 9 + 3 + 1 + 2 = 26.
2 9
9 3
1 2

3rd submatrix sum = 2 + 2 + 6 = 10.
2
2
6

4th submatrix sum = 6 + 5 + 6 + 6 = 23.
6 5
6 6

5th submatrix sum = 7 + 1 + 6 + 2 = 16.
7 1
6 2

6th submatrix sum = 9 + 3 = 12.
9
3

7th submatrix sum = 1 + 6 = 7.
1 6

8th submatrix sum = 7 + 9 = 16.
7 9

9th submatrix sum = 7.
7

Example Input/Output 2:
Input:
9 9
1 2 3 1 2 3 1 2 3
4 5 6 4 5 6 4 5 6
7 8 9 7 8 9 7 8 9
1 2 3 1 2 3 1 2 3
4 5 6 4 5 6 4 5 6
7 8 9 7 8 9 7 8 9
1 2 3 1 2 3 1 2 3
4 5 6 4 5 6 4 5 6
7 8 9 7 8 9 7 8 9
3 6 3 6

Output:
45 45 45 45 45 45 45 45 45
"""
def print_sum(cols,m,r1,r2,c1,c2):
    a=b=c=0
    for i in range(r1,r2):
        for j in range(cols):
            if j<c1:
                a+=m[i][j]
            elif j<c2:
                b+=m[i][j]
            else:
                c+=m[i][j]
    print(a,b,c,end=' ')
r,c=map(int,input().split())
m=[list(map(int,input().split())) for _ in range(r)]
x,y,p,q=map(int,input().split())
print_sum(c,m,0,x,p,q)
print_sum(c,m,x,y,p,q)
print_sum(c,m,y,r,p,q)
