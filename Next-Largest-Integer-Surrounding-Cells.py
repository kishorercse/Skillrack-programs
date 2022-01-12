"""
The program must accept an integer matrix of size R*C containing only unique integers as the input. The program must print the output based on the following conditions.
- The program must print the smallest integer in the given matrix.
- Then the program must print the next largest integer of the previously printed integer in its surrounding cells(i.e., 8 possible surrounding cells).
- Then the program must repeat the above process till there is no next largest integer to print from the surrounding cells.

Boundary Condition(s):
2 <= R, C <= 50
1 <= Matrix element value <= 10^4

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C integers separated by a space.

Output Format:
The first line contains the integer values separated by a space.

Example Input/Output 1:
Input:
4 4
18 26 25 24
19 17 10 16
22 27 21 14
13 11 20 29

Output:
10 14 16 21 27

Explanation:
Here R = 4 and C = 4.
The smallest integer in the matrix is 10.
The next largest integer of 10 in its surrounding cells is 14.
The next largest integer of 14 in its surrounding cells is 16.
The next largest integer of 16 in its surrounding cells is 21.
The next largest integer of 21 in its surrounding cells is 27.
There is no next largest integer of 27 in its surrounding cells.
Hence the output is
10 14 16 21 27

Example Input/Output 2:
Input:
3 5
20 26 19 50 27
17 25 34 18 32
15 40 47 36 33

Output:
15 17 20 25 26 34 36 47
"""
r,c=map(int,input().split())
m=[]
x=99999999
a=b=-1
for i in range(r):
    t=list(map(int,input().split()))
    m.append(t)
    for j in range(c):
        if t[j]<x:
            x=t[j]
            a,b=i,j
print(x,end=' ')
p=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
while True:
    lar=99999999
    aa=bb=-1
    for i,j in p:
        if 0<=a+i<r and 0<=b+j<c and m[a+i][b+j]>x and m[a+i][b+j]<lar:
            lar=m[a+i][b+j]
            aa,bb=a+i,b+j
    if aa==-1:
        break
    x=lar
    a,b=aa,bb
    print(x,end=' ')
