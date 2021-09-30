"""
The program must accept an integer matrix of size RxC as the input. The program must print the sum of integers in the longest increasing 
series of integers in the matrix both horizontally and vertically (in all direction that is top to bottom, bottom to top, left to right 
or right to left). If more than one longest series having the same number of integers exist, then print the maximum sum. 

Boundary Condition(s):
1 <= R, C <= 100 

Input Format: 
The first line contains R and C separated by a space. 
The next R lines contain C integers each separated by a space. 

Output Format: 
The first line contains the sum of integers in the longest series as per the condition. 

Example Input/Output 1: 
Input: 
6 4 
11 15 11 34 
14 28 30 30
11 22 21 22 
26 22 13 21 
20 23 21 16 
25 14 29 16

Output: 
123

Explanation: 
The longest increasing series of integers are at the last column in the rows 5, 4, 3, 2 and 1.
These 5 integers are added as 16+21+22+30+34 = 123. 
Hence 123 is printed.

Example Input/Output 2:
Input: 
6 5 
16 36 21 28 14 
21 31 32 16 21 
47 31 26 12 20 
33 28 20 35 33 
39 13 22 16 34 
33 16 16 29 14 

Output: 
116 

Explanation: 
The longest increasing series of integers are at the 3rd row and in the columns 4, 3, 2 and 1.
These integers are added as 12 + 26 + 31 + 47 = 116.
Hence 116 is printed as the output.
"""
r,c=map(int,input().split())
mat=[list(map(int,input().split())) for _ in range(r)]
max_count=0
max_sum=0
for i in range(r):
    for j in range(1,c):
        prev = s = mat[i][j]
        k=j-1
        count=1
        while(k>=0 and prev<mat[i][k]):
            s+=mat[i][k]
            prev=mat[i][k]
            k-=1
            count+=1
        if count>max_count:
            max_count=count
            max_sum=s
        elif count==max_count:
            max_sum=max(max_sum,s)
        k=j+1
        s=prev=mat[i][j]
        count=1
        while k<c and prev<mat[i][k]:
            s+=mat[i][k]
            prev=mat[i][k]
            k+=1
            count+=1
        if count>max_count:
            max_count=count
            max_sum=s
        elif count==max_count:
            max_sum=max(max_sum,s)
        s=prev=mat[i][j]
        k=i-1
        count=1
        while k>=0 and prev<mat[k][j]:
            s+=mat[k][j]
            prev=mat[k][j]
            k-=1
            count+=1
        if count>max_count:
            max_count=max_count
            max_sum=s
        elif max_count==count:
            max_sum=max(max_sum,s)
        k=i+1
        s=prev=mat[i][j]
        count=1
        while k<r and prev<mat[k][j]:
            s+=mat[k][j]
            prev=mat[k][j]
            k+=1
            count+=1
        if count>max_count:
            max_count=count
            max_sum=s
        elif max_count==count:
            max_sum=max(max_sum,s)
print(max_sum)
