"""
The program must accept an integer matrix of size RxC as the input. The program must print the number of submatrix of size 2x2 that contains only one integer (i.e., all the four 
integers in the 2x2 submatrix are equal) as the output. 

Boundary Condition(s): 
2 <= R, C <= 50 

Input Format:
The first line contains R and C separated by a space. 
The next R lines each contain C integers separated by a space. 

Output Format:
The first line contains the number of submatrix as per the given condition. 

Example Input/Output 1: 
Input:
2 5
5 1 1 2 2
4 1 1 2 2 

Output: 
2

Explanation: 
The integers in the first 2x2 submatrix are 5, 1, 4 and 1.
The integers in the second 2x2 submatrix are 1, 1, 1 and 1.
The integers in the third 2x2 submatrix are 1, 2, 1 and 2. 
The integers in the fourth 2x2 submatrix are 2, 2, 2 and 2.
In the 2x5 integer matrix, there are 2 submatrices where all the integers are equal in it. Hence the output is 2 

Example Input/Output 2:
Input:
4 4
90 56 15 20
62 62 48 15
62 62 10 10
62 62 10 10

Output: 
3
"""
r,c=map(int,input().split())
m=[list(map(int,input().split())) for _ in range(r)]
count=0
for i in range(r-1):
    for j in range(c-1):
        if m[i][j]==m[i][j+1] and m[i][j+1]==m[i+1][j] and m[i+1][j]==m[i+1][j+1]:
            count+=1
print(count)
