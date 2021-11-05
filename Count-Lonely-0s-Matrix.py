"""
The program must accept an integer matrix of size RxC containing only 0s and 1s as the input. The program must print the count of lonely 0s in the matrix as the output. 
If matrix[i][j] is a lonely 0, then all other elements in the row i and the column j are 1. 

Boundary Condition(s): 
2 <= R, C <= 50 

Input Format: 
The first line contains R and C separated by a space.
The next R lines, each contains C integers separated by a space.

Output Format: 
The first line contains an integer representing the count of lonely 0s in the given matrix. 

Example Input/Output 1: 
Input:
3 4
0 1 1 1
1 0 1 0
1 1 0 1

Output: 
2 

Explanation: 
The lonely 0s in the given matrix are highlighted below. 
0 1 1 1 
1 0 1 0 
1 1 0 1

Example Input/Output 2:
Input: 
5 5
1 1 1 1 1
1 0 1 1 1
1 1 1 0 1
0 1 1 1 0
1 0 0 1 1

Output:
1
"""
r,c=map(int,input().split())
m=[input().split() for _ in range(r)]
lonely_zero=0
for i in range(r):
    for j in range(c):
        if m[i][j]=='0':
            flag=1
            for ii in range(r):
                if ii!=i and m[ii][j]=='0':
                    flag=0
                    break
            if flag==1:
                for jj in range(c):
                    if jj!=j and m[i][jj]=='0':
                        flag=0
                        break
                lonely_zero+=flag
print(lonely_zero)
