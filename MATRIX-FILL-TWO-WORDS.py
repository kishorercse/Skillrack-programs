"""
A N*N matrix having N rows and N columns containing + or * for it's cell values is passed as the input. Two strings S1 and S2 are also passed as input. The program must search 
for * in a straight line (either left to right or top to bottom) and replace them with strings S1 and S2.

Input Format:
The first line will contain the value of N.
The next N lines will contain the values for N rows having +  and  * representing the cell values of the matrix.
The last two lines will contain the value of the two strings S1 and S2 respectively.

Output Format:
N lines with the matrix cell values containing * replaced by the characters in the string values S1 and S2.

Constraints:
4 <= N <= 100
Length of S1 and S2 is from 2 to N.

Example Input/Output 1:
Input:
10
++++++++++
++++++++++
+++*++++++
+++*++++++
+++***++++
+++*++++++
+++*++++++
+++*++++++
++++++++++
++++++++++
MANAGE
NEW

Output:
++++++++++
++++++++++
+++M++++++
+++A++++++
+++NEW++++
+++A++++++
+++G++++++
+++E++++++
++++++++++
++++++++++

Example Input/Output 2:
Input:
6
++++++
++*+++
++****
++*+++
++*+++
++++++
LION
IRON

Output:
++++++
++L+++
++IRON
++O+++
++N+++
++++++ 
"""
def vertical(mat,s,l,x,y):
    for i in range(l):
        if mat[x+i][y]=='*' or mat[x+i][y]==s[i]:
            mat[x+i][y]=s[i]
        else:
            return False
    return mat
def horizontal(mat,s,l,x,y):
    for i in range(l):
        if mat[x][y+i]=='*' or mat[x][y+i]==s[i]:
            mat[x][y+i]=s[i]
        else:
            return False
    return mat
def solve(mat, ind):
    if ind<2:
        s=l[ind]
        length=len(s)
        mx=n-length+1
        for i in range(mx):
            for j in range(n):
                t=vertical([i[:] for i in mat],s,length,i,j)
                if t:
                    solve(t,ind+1)
                t=horizontal([i[:] for i in mat],s,length,j,i)
                if t:
                    solve(t,ind+1)
    else:
        for i in mat:
            print(*i,sep='')
        exit()
n=int(input())
m=[list(input().strip()) for _ in range(n)]
l=[input().strip() for _ in range(2)]
solve(m,0)
