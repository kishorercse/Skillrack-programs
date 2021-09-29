"""
The program must accept an integer matrix of size RxC as the input. The program must print the count of the longest consecutive odd 
or consecutive even integers both vertically and horizontally present in the matrix as the output. 

Boundary Condition(s): 
1 <= R, C <= 1000 

Input Format: 
The first line contains R and C separated by a space. 
The next R lines contain C integers each separated by a space.

Output Format: 
The first line contains the count of the longest consecutive odd or even integers.
Example Input/Output 1: 
Input: 
4 5 
2 1 4 5 7 
5 4 3 2 1 
6 1 4 8 7 
2 1 4 7 2 

Output: 
3 

Explanation: 
The longest consecutive odd integers are present at the last column in the first three rows.

Example Input/Output 2:
Input: 
6 6 
49 50 45 12 33 19 
11 27 44 17 14 47
38 12 12 50 13 19 
46 21 10 46 39 48 
28 43 43 20 43 20 
29 45 39 36 10 38 

Output: 
4 

Explanation: 
The longest consecutive even integers are present at the 3rd row and in the columns 1, 2, 3 and 4.
"""
r,c=map(int,input().split())
mat=[]
max_count=0
for _ in range(r):
    count=0
    t=list(map(int,input().split()))
    mat.append(t)
    for j in range(1,c):
        count+=1
        if t[j-1]%2!=t[j]%2:
            if count>max_count:
                max_count=count
            count=0
    if c>1 and t[-1]%2==t[-2]%2:
        count+=1
    if count>max_count:
        max_count=count
for j in range(c):
    count=0
    for i in range(1,r):
        count+=1
        if mat[i-1][j]%2!=mat[i][j]%2:
            if count>max_count:
                max_count=count
            count=0
    if r>1 and mat[-1][j]%2==mat[-2][j]%2:
        count+=1
    if count>max_count:
        max_count=count
print(max_count)
