"""
A matrix of size R*C is given as the input to the program. The program must add the elements in the first row in each column to the elements in the below rows by equally dividing them. Then the program must print the modified matrix as the output.
Note: If the integer cannot be evenly divided then do not consider the decimal point values.

Boundary Condition(s):
1 <= R, C <= 100

Input Format:
The first line contains R and C separated by space.
The next R lines contain C integers each separated by space(s).

Output Format:
The first R lines contain the modified matrix as per the given condition.

Example Input/Output 1:
Input:
3 4
24 4 2 19
8 10 5 1
7 13 12 14

Output:
24 4 2 19
20 12 6 10
19 15 13 23

Example Input/Output 2:
Input:
4 4
21 24 13 14
22 12 23 11
11 22 16 16
20 16 11 20

Output:
21 24 13 14
29 20 27 15
18 30 20 20
27 24 15 24
"""
r,c=map(int,input().split())
m=[list(map(int,input().split())) for _ in range(r)]
print(*m[0])
m[0]=[m[0][j]//(r-1) for j in range(c)]
for i in range(1,r):
    for j in range(c):
        print(m[i][j]+m[0][j],end=' ')
    print()
