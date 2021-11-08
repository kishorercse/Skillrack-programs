"""
The program must accept an integer matrix of size NxN and an integer X as the input. The program must print all the integers along the main diagonal of X in the matrix as the 
output. 
Note: The integer X has occurred only once in the NxN matrix. 

Boundary Condition(s): 
2 <= N <= 50 
1 <= Each integer value <= 10000 

Input Format: 
The first line contains N. 
The next N lines each contain N integers separated by a space. 
The (N+2)nd line contains X.

Output Format: 
The first line contains all the integers along the main diagonal of X in the matrix separated by a space. 

Example Input/Output 1: 
Input: 
4
77 48 51 82
13 53 76 68
64 71 45 52
87 87 64 24 
53 

Output:
77 53 45 24 

Explanation: 
The main diagonal of 53 is highlighted below. 
77 48 51 82
13 53 76 68
64 71 45 53 
87 87 64 24 

Example Input/Output 2:
Input: 
5
41 70 37 49 92 
84 54 46 58 81 
36 89 53 63 70 
22 13 20 13 59 
35 43 32 28 83 
20 

Output:
84 89 20 28
"""
n=int(input())
m=[list(map(int,input().split())) for _ in range(n)]
x=int(input())
t=False
for i in range(n):
    for j in range(n):
        if m[i][j]==x:
            t=min(i,j)
            r=i-t
            c=j-t
            break
    if t:
        break
while r<n and c<n:
    print(m[r][c],end=' ')
    r+=1
    c+=1
