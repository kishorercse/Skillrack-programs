"""
The program must accept two integer arrays A1 and A2 as the input. The size of the array A1 is M and the size of the array A2 is N. The program must print the longest common subarray between the given two arrays as the output. If two or more subarrays have the same maximum size, then the program must print the first occurring subarray in A1 as the output.

Boundary Condition(s):
2 <= M, N <= 100
1 <= Each integer value <= 10^5

Input Format:
The first line contains M.
The second line contains M integers separated by a space.
The third line contains N.
The fourth line contains N integers separated by a space.

Output Format:
The first line contains the longest common subarray between the given two arrays.

Example Input/Output 1:
Input:
5
1 2 3 4 5
6
2 3 4 7 1 2

Output:
2 3 4

Explanation:
All possible common subarrays are {1}, {2}, {3}, {4}, {1, 2}, {2, 3}, {3, 4}, {2, 3 4}.
Here the longest possible subarray is {2 3 4}.
Hence the output is
2 3 4

Example Input/Output 2:
Input:
6
5 10 15 20 25 30
6
35 10 15 40 15 20

Output:
10 15

Example Input/Output 3:
Input:
7
8 4 7 3 2 1 7
8
8 7 3 2 4 7 3 5

Output:
4 7 3
"""
m=int(input())
l1=[0]+list(map(int,input().split()))
n=int(input())
l2=[0]+list(map(int,input().split()))
dp=[[0]*(n+1) for _ in range(m+1)]
max_size=0
max_row=-1
for i in range(1,m+1):
    for j in range(1,n+1):
        if l1[i]==l2[j]:
            dp[i][j]=dp[i-1][j-1]+1
            if dp[i][j]>max_size:
                max_size=dp[i][j]
                max_row=i
for i in range(max_row-max_size+1,max_row+1):
    print(l1[i],end=' ')
