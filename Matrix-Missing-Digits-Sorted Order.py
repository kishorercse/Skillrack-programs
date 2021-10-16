"""
The program must accept a matrix of size RxC containing only digits as the input. Each 3x3 submatrix in the given matrix contains 9 unique digits(1 - 9), but some digits are 
missing. The missing digits are denoted by hyphens. The program must find those missing digits in each 3x3 submatrix and replace the hyphens with the missing digits in sorted 
order. Finally, the program must print the revised matrix as the output. Note: The values of R and C are always divisible by 3. 

Boundary Condition(s): 
3 <= R, C <= 48 

Input Format: 
The first line contains R and C separated by a space. 
The next R lines contain the matrix. 

Output Format: 
The first R lines contain the revised matrix. 

Example Input/Output 1:
Input: 
9 6 
5 7 1 8 4 - 
- 9 - - 6 2 
4 3 6 - 3 -
8 - 5 8 - 9 
2 4 3 - - 1 
6 - - 5 6 7 
6 3 2 1 4 - 
- 5 - 3 5 9 
7 4 8 6 - - 

Output: 
5 7 1 8 4 1 
2 9 8 5 6 2 
4 3 6 7 3 9 
8 1 5 8 2 9 
2 4 3 3 4 1 
6 7 9 5 6 7 
6 3 2 1 4 2 
1 5 9 3 5 9 
7 4 8 6 7 8 

Explanation: 
Here R = 9 and C = 6 After replacing the hyphens in each 3x3 submatrix with the missing digits in sorted order, the matrix becomes 
5 7 1 8 4 1 
2 9 8 5 6 2 
4 3 6 7 3 9 
8 1 5 8 2 9 
2 4 3 3 4 1 
6 7 9 5 6 7 
6 3 2 1 4 2 
1 5 9 3 5 9 
7 4 8 6 7 8 

Example Input/Output 2: 
Input: 
6 6 
6 4 - - 5 2 
- 5 3 - - 9 
- 9 8 4 3 7 
6 9 5 3 - 4 
4 1 8 2 - 6 
3 2 7 8 9 1 

Output: 
6 4 1 1 5 2 
2 5 3 6 8 9 
7 9 8 4 3 7 
6 9 5 3 5 4 
4 1 8 2 7 6 
3 2 7 8 9 1 
"""
r,c=map(int,input().split())
m=[input().split() for _ in range(r)]
for i in range(0,r,3):
    for j in range(0,c,3):
        t=[0]*10
        for ii in range(i,i+3):
            for jj in range(j,j+3):
                if m[ii][jj]!='-':
                    t[int(m[ii][jj])]=1
        t=[i for i in range(1,10) if t[i]==0]
        for ii in range(i,i+3):
            for jj in range(j,j+3):
                if m[ii][jj]=='-':
                    m[ii][jj]=t.pop(0)
for i in m:
    print(*i)
