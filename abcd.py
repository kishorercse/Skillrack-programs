"""
The program must accept an integer matrix of size MxM and an integer N representing the size of NxN submatrix as input. The program must print the count of NxN submatrices in the 
MxM matrix whose border elements are same.

Boundary Condition(s): 
2 <= M <= 100 
2 <= N <= M 
1 <= Each integer value <= 1000 

Input Format: 
The first line contains M and N separated by a space. 
The next M lines contain M integers separated by space(s).

Output Format: 
The first line contains the count of NxN submatrices in the MxM matrix whose border elements are same. 

Example Input/Output 1: 
Input: 
6 3 
8 8 8 9 8 3 
8 3 8 3 3 3 
8 8 8 3 4 3 
7 3 3 3 3 3 
7 3 7 3 3 3 
2 3 3 3 3 3 

Output:
4 

Explanation: 
There are four 3x3 submatrices having the same border elements which are highlighted below.
8 8 8 9 8 3 
8 3 8 3 3 3 
8 8 8 3 4 3 
7 3 3 3 3 3 
7 3 7 3 3 3 
2 3 3 3 3 3 

Example Input/Output 2: 
Input: 
4 2
1 1 1 1
1 2 1 1
1 2 1 1
1 1 1 1

Output:
3
"""
m,n=map(int,input().split())
a=[list(map(int,input().split())) for i in range(m)]
count=0
for i in range(m-n+1):
    for j in range(m-n+1):
        t=a[i][j]
        f=True
        for k in range(j,j+n):
            if a[i][k]!=t or a[i+n-1][k]!=t:
                f=False
                break
        if f:
            for k in range(i,i+n):
                if a[k][j]!=t or a[k][j+n-1]!=t:
                    f=False
                    break
            if f:
                count+=1
print(count)
