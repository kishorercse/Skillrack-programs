"""
The program must accept a character matrix of size N*N representing the floor of a room as the input. Each hash symbol indicates that the area is clean. Each asterisk indicates
that the area is dirty. A floor sweeper of length L is available to clean the room. The program must print the maximum number of dirty areas that can be cleaned in one sweep
vertically or horizontally as the output.

Boundary Condition(s):
2 <= N <= 50
1 <= L <= N

Input Format:
The first line contains N.
The next N lines, each contains N characters separated by a space.
The N+2nd line contains L.

Output Format:
The first line contains an integer representing the maximum number of dirty areas that can be cleaned in one sweep vertically or horizontally.

Example Input/Output 1:
Input:
5
# * # * *
* * * * #
* # # * #
* * # # *
# # * # #
2

Output:
7

Explanation:
Here N = 5 and L = 2.
The maximum number of dirty areas that can be cleaned is 7 (by sweeping the first 2 rows horizontally).
Hence 7 is printed as the output.

Example Input/Output 2:
Input:
6
# # * # # #
# * # * # *
# # * # # #
* * # # # #
# * # # # #
# # * * # *
3

Output:
8
"""
n=int(input())
m=[input().split() for _ in range(n)]
l=int(input())
rows=[]
cols=[]
for i in range(n):
    row=col=0
    for j in range(n):
        if m[i][j]=='*':
            row+=1
        if m[j][i]=='*':
            col+=1
    rows.append(row)
    cols.append(col)
rowsum=colsum=0
res=-1
for i in range(n):
    rowsum+=rows[i]
    colsum+=cols[i]
    if i-l>=0:
        rowsum-=rows[i-l]
        colsum-=cols[i-l]
    res=max(rowsum,colsum,res)
print(res)
