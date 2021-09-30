"""
The program must accept a character matrix of size RxC containing only # and * as the input. The program must print the count
of the longest consecutive asterisks both vertically and horizontally present in the matrix as the output. 

Boundary Condition(s):
1 <= R, C <= 100 

Input Format: 
The first line contains R and C separated by a space.
The next R lines contain C characters each.

Output Format:
The first line contains the count of the longest consecutive asterisks. 

Example Input/Output 1: 
Input: 
4 5 
##### 
#***# 
###*# 
#**## 

Output:
3

Explanation: 
The longest consecutive asterisks are present in the 2nd row. 

Example Input/Output 2:
Input:
7 8 
#*#****# 
####*### 
##****##
####*### 
##*#*### 
##***###
###*#### 

Output: 
6
"""
r,c=map(int,input().split())
mat=[]
max_count=0
for _ in range(r):
    t=input().strip()
    mat.append(t)
    count=0
    for j in range(1,c):
        count+=1
        if not(t[j]=='*' and t[j-1]=='*'):
            if count > max_count:
                max_count=count
            count=0
    if c>1 and t[-1]=='*' and t[-1]==t[-2]:
        count+=1
    if count>max_count:
        max_count=count
for j in range(c):
    count=0
    for i in range(1,r):
        count+=1
        if not(mat[i-1][j]=='*' and mat[i][j]=='*'):
            if count > max_count:
                max_count=count
            count=0
    if r>1 and mat[-1][j]=='*' and mat[-1][j]==mat[-2][j]:
        count+=1
    if count>max_count:
        max_count=count
print(max_count)
