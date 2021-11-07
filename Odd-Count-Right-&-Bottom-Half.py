"""
The program must accept an integer matrix of size RxC as the input. The program must print the count of odd integers which are present at the right half of the matrix and bottom 
half of the matrix as the output. Note: R and C values will be always even. 

Boundary Condition(s): 
2 <= R, C <= 50 
1 <= Each integer value <= 10^4 

Input Format: 
The first line contains R and C separated by a space. 
The next R lines each contain C integers separated by a space. 

Output Format: 
The first line contains the count of odd integers which are present at the right half of the matrix and bottom half of the matrix. 

Example Input/Output 1: 
Input:
4 6
32 13 30 14 25 11
22 38 44 35 42 43
36 12 46 48 40 41
50 74 10 34 68 16

Output: 
5 

Explanation: 
In the 4x6 matrix, the right half of the matrix and bottom half of the matrix are highlighted below, 
32 13 30 14 25 11 
22 38 44 35 42 43 
36 12 46 48 40 41
50 74 10 34 68 16
So the odd integers in the right half of the matrix and bottom half of the matrix are 25, 11, 35, 43 and 41.
Hence the output is 5 

Example Input/Output 2:
Input:
8 4
97 13 15 47
54 67 57 95
44 92 61 55
31 34 62 96
46 10 51 84
53 91 16 72
98 89 58 33
22 48 66 77

Output:
12
"""
r,c=map(int,input().split())
m=[list(map(int,input().split())) for _ in range(r)]
h=c//2
odd=0
for i in range(r):
    for j in range(h,c):
        if m[i][j]%2!=0:
            odd+=1
for i in range(r//2,r):
    for j in range(h):
        if m[i][j]%2!=0:
            odd+=1
print(odd)
