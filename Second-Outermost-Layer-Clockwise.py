"""
The program must accept an integer matrix of size NxN as the input. The program must print all the integers in the second outermost layer (in clockwise direction) of the given 
matrix as shown in the Example Input/Output section. 

Boundary Condition(s): 
3 <= N <= 50 

Input Format:
The first line contains N. 
The next N lines each contain N integers separated by a space. 

Output Format:
The first line contains all the integers in the second outermost layer (in clockwise direction) of the given matrix separated by a space. 

Example Input/Output 1:
Input: 
5
11 76 24 19 44
38 98 37 26 19
47 90 73 21 97
44 86 39 84 70
44 47 98 45 31

Output:
98 37 26 21 84 39 86 90 

Explanation: 
In the given 5x5 matrix, the second outermost layer is highlighted below. 
11 76 24 19 44
38 98 37 26 19
47 90 73 21 97
44 86 39 84 70
44 47 98 45 31
So the integers in the second outermost layer are printed in the clockwise direction. 

Example Input/Output 2:
Input: 
8
24 88 10 77 36 10 99 55
80 20 48 99 50 65 90 21
84 33 96 53 61 36 66 18
58 63 74 47 40 72 68 69
59 27 68 28 24 23 30 29
14 49 64 40 32 46 48 73
50 51 18 92 49 45 86 50
78 13 28 53 98 91 95 21

Output:
20 48 99 50 65 90 66 68 30 48 86 45 49 92 18 51 49 27 63 33
"""
n=int(input())
m=[input().split() for _ in range(n)]
for i in range(1,n-1):
    print(m[1][i],end=' ')
for i in range(2,n-1):
    print(m[i][n-2],end=' ')
for i in range(n-3,0,-1):
    print(m[n-2][i],end=' ')
for i in range(n-3,1,-1):
    print(m[i][1],end=' ')
