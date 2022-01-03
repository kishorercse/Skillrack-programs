"""
The program must accept a grid of size N*N containing asterisks and exactly one hash symbol as the input. The hash symbol indicates the bottom-right corner of another N*N grid 
of asterisks. The program must print the combined grid of asterisks as shown in the Example Input/Output section. The empty spaces must be printed as hyphens.

Boundary Condition(s):
2 <= N <= 50

Input Format:
The first line contains N.
The next N lines, each contains N characters separated by a space.

Output Format:
The lines contain the combined grid of asterisks separated by a space.

Example Input/Output 1:
Input:
4
* * * *
* * * *
* # * *
* * * *

Output:
* * * * - -
* * * * * *
* * * * * *
* * * * * *
- - * * * *

Explanation:
Here N=4, so the size of grid is 4*4.
The combined 4*4 grids of asterisks is given below.
* * * * - -
* * * * * *
* * * * * *
* * * * * *
- - * * * *

Example Input/Output 2:
Input:
3
* # *
* * *
* * *

Output:
* * * -
* * * -
* * * *
- * * *
- * * *

Example Input/Output 3:
Input:
6
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * # *
* * * * * *

Output:
* * * * * * -
* * * * * * *
* * * * * * *
* * * * * * *
* * * * * * *
* * * * * * *
- * * * * * *
"""
n=int(input())
m=[input().split() for _ in range(n)]
r=c=-1
for i in range(n):
    for j in range(n):
        if m[i][j]=='#':
            r,c=i,j
            break
    if r!=-1:
        break
dr=n-r
dc=n-c
rows=n+dr-1
cols=n+dc-1
for i in range(dr-1):
    for j in range(cols-dc+1):
        print('*',end=' ')
    for j in range(dc-1):
        print('-',end=' ')
    print()
for i in range(rows-(2*dr-2)):
    for j in range(cols):
        print('*',end=' ')
    print()
for i in range(dr-1):
    for j in range(dc-1):
        print('-',end=' ')
    for j in range(cols-dc+1):
        print('*',end=' ')
    print()
