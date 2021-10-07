"""
Several bricks whose weight may be varying are stacked in multiple columns. A brick along with the other bricks that are above it can be removed in one go 
if the weight of the bricks is strictly increasing from top to bottom. The number of rows R and the columns C in which the bricks are arranged is passed 
as the input. The weight of each brick is also passed as the input. The program must print the minimum number of removals M to remove all the bricks. 

Boundary Condition(s): 
1 <= R, C <= 10^4
1 <= weight of each brick <= 1000 

Input Format: 
The first line contains R and C separated by space(s). 
The next R lines each contain C values denoting the weight of the bricks.

Output Format: 
The first line contains M.
Example Input/Output 1:
Input:
4 3
11 84 63 
57 85 5
30 67 97 
85 87 58

Output: 
7

Explanation:
In the first column, 11 57 can be removed in one removal. 30 85 can be removed in one removal. 
In the second column, 84,85 and 67,87 can be removed requiring two removals. 
In the third column, 63 and 5 97 and 58 can be removed in three removals. So overall 7 minimum removals required.
"""
r,c=map(int,input().split())
mat=[list(map(int,input().split())) for _ in range(r)]
count=c
for j in range(c):
    i=1
    t=mat[0][j]
    while i<r:
        if mat[i][j]<=t:
            count+=1
        t=mat[i][j]
        i+=1
print(count)
