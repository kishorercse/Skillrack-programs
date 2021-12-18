"""
A M*N matrix having M rows and N columns contains + or - as it's cell values. A set of semi-colon separated words is also passed as input. The cells with + are not to be touched. 
The words must be filled in the cells with - values. Input Format: The first line will contain the value of M and N, each separated by a space. The next M lines will contain N 
characters (each of these characters will be + or -). The last (M+2)th line will contain the words to be filled separated by a semi-colon. Output Format: M lines with the words 
filled in the matrix.

Constraints:
10 <= M, N <= 20 

Example Input/Output 1:
Input:
10 10 
+-++++++++ 
+-++++++++ 
+-------++ 
+-++++++++ 
+-++++++++ 
+------+++ 
+-+++-++++ 
+++++-++++ 
+++++-++++ 
++++++++++ 
AGRA;NORWAY;ENGLAND;GWALIOR

Output: 
+E++++++++ 
+N++++++++ 
+GWALIOR++ 
+L++++++++ 
+A++++++++ 
+NORWAY+++ 
+D+++G++++ 
+++++R++++ 
+++++A++++ 
++++++++++
"""
def horizontal(t,i,j,s,l):
    for ind in range(l):
        if t[i][j+ind]=='-' or t[i][j+ind]==s[ind]:
            t[i][j+ind]=s[ind]
        else:
            return False
    return t
def vertical(t,i,j,s,l):
    for ind in range(l):
        if t[i+ind][j]=='-' or t[i+ind][j]==s[ind]:
            t[i+ind][j]=s[ind]
        else:
            return False
    return t
def solve(mat, ind):
    if ind<length:
        s=l[ind]
        sl=len(s)
        mx=m-sl+1
        for i in range(mx):
            for j in range(n):
                temp=vertical([i[:] for i in mat],i,j,s,sl)
                if temp:
                    solve(temp,ind+1)
        mx=n-sl+1
        for i in range(m):
            for j in range(mx):
                temp=horizontal([i[:] for i in mat],i,j,s,sl)
                if temp:
                    solve(temp,ind+1)
    else:
        for i in mat:
            print(*i,sep='')
        exit()
m,n=map(int,input().split())
mat=[list(input().strip()) for _ in range(m)]
l=input().split(';')
length=len(l)
solve(mat,0)
