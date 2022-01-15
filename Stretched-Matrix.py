"""
The program must accept two matrices M1 and M2 as the input. The size of the matrix M1 is N*N. The size of the matrix M2 is X*X. The program must print Yes if M2 is a diagonally
stretched matrix of M1 (i.e., if each element in M1 is repeated as a submatrix of size (X/N)*(X/N) in M2 in the order of their occurrence). Else the program must print No as the
output.

Note: The value of X is always divisible by N.

Boundary Condition(s):
2 <= N <= 10
2 <= X <= 50
1 <= Matrix element value <= 1000

Input Format:
The first line contains N.
The next N lines (from the 2nd line) contain the matrix M1.
The N+2nd line contains X.
The next X lines (from the N+3rd line) contain the matrix M2.

Output Format:
The first line contains Yes or No.

Example Input/Output 1:
Input:
3
1 2 3
4 5 6
7 8 9
9
1 1 1 2 2 2 3 3 3
1 1 1 2 2 2 3 3 3
1 1 1 2 2 2 3 3 3
4 4 4 5 5 5 6 6 6
4 4 4 5 5 5 6 6 6
4 4 4 5 5 5 6 6 6
7 7 7 8 8 8 9 9 9
7 7 7 8 8 8 9 9 9
7 7 7 8 8 8 9 9 9

Output:
Yes

Explanation:
Here N = 3 and X = 9.
Each integer in the matrix M1 is repeated as a submatrix of size 3*3 in M2.
Hence Yes is printed as the output.

Example Input/Output 2:
Input:
2
10 20
33 44
8
10 10 10 10 20 20 20 20
10 10 10 10 20 20 20 20
10 10 10 10 20 20 20 20
10 10 10 10 20 20 20 20
33 33 33 33 44 44 44 44
33 33 33 33 44 44 44 44
33 33 33 33 44 44 44 44
33 33 33 33 44 44 44 44

Output:
Yes

Example Input/Output 3:
Input:
2
6 7
8 9
4
6 6 7 7
6 6 7 7
8 8 5 9
8 8 9 9

Output:
No
"""
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
x=int(input())
b=[list(map(int,input().split())) for _ in range(x)]
t=x//n
for i in range(x):
    for j in range(x):
        if b[i][j]!=a[i//t][j//t]:
            print("No")
            exit()
print("Yes")
