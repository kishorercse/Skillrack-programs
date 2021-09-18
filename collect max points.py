"""A kids game has a board with an M*N matrix having M rows and N columns containing non-negative integer values as cell values. The kid can start from the first column of any row and can perform the following three navigations after collecting the points in that cell.
– He can move to the right cell.
– He can move to the top right cell.
– He can move to the bottom right cell.

The kid cannot come back to a previous column. He navigates until he reaches the last column of the matrix and collects the points in each cell. The program must print the maximum points a kid can collect for the given matrix while navigating.

Input Format:
The first line will contain the value of M and N separated by a space.
The next M lines will contain the values for N columns with the non-negative integer values separated by a space.

Output Format:
The integer value of the maximum points that can be collected.

Constraints:
2 <= M,N <= 30

Example Input/Output 1:
Input:
3 3
5 3 3
2 1 4
0 9 4
Output:
15
Explanation: The maximum points can be collected by navigating 2->9->4 and hence the sum is 2+9+4 = 15.

Example Input/Output 2:
Input:
4 4
1 3 1 5
2 2 4 1
5 0 2 3
0 6 1 2
Output:
16
Explanation: The maximum points 16 can be collected by navigating 5->6->2->3 or 5->2->4->5.
"""
m,n=map(int,input().split())
mat=[list(map(int,input().split())) for _ in range(m)]
for j in range(1,n):
    mat[0][j]+=max(mat[0][j-1],mat[1][j-1])
    mat[m-1][j]+=max(mat[m-2][j-1],mat[m-1][j-1])
    for i in range(1,m-1):
        mat[i][j]+=max(mat[i-1][j-1],mat[i][j-1],mat[i+1][j-1])
mx=mat[0][n-1]
for i in range(1,m):
    if mat[i][n-1]>mx:
        mx=mat[i][n-1]
print(mx)
