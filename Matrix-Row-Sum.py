"""
Given a R*C matrix (R - rows and C- Columns), print the sum of the values in each row as the output.

Input Format:
First line will contain R and C separated by a space.
Next R lines will contain C values, each separated by a space.

Output Format:
R lines representing the sum of elements of rows 1 to R.

Boundary Conditions:
2 <= R, C <= 50

Example Input/Output 1:
Input:
4 4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

Output:
10
26
42
58
"""
r,c=map(int,input().split())
for _ in range(r):
    print(sum(map(int,input().split())))
