"""
The program must accept the coordinates (x, y) of N distinct points and an integer L as the input. The program must print the number of vertical lines of length L that can be 
formed using the given N points as the output.

Boundary Condition(s):
2 <= N <= 500
-10 <= x, y <= 10
1 <= L <= 20

Input Format:
The first line contains N.
The next N lines, each contains the coordinates(x, y) of a point.
The N+2nd line contains L.

Output Format:
The first line contains an integer value representing the number of vertical lines of length L that can be formed using the given N points.

Example Input/Output 1:
Input:
9
1 3
-1 1
2 4
1 -3
-1 3
1 0
-1 -2
1 2
2 1
3

Output:
4

Explanation:
Here L = 3.
The four vertical lines of length 3 that can be formed using the 9 points are given below.
Line 1: (-1, 1) to (-1, -2)
Line 2: (1, 3) to (1, 0)
Line 3: (1, 0) to (1, -3)
Line 4: (2, 4) to (2, 1)

Example Input/Output 2:
Input:
12
0 0
2 0
4 0
-2 0
-4 0
4 2
4 4
2 2
0 2
2 4
0 4
-4 2
2

Output:
7
"""
n=int(input())
d={}
for _ in range(n):
    x,y=map(int,input().split())
    d[x]=d.get(x,[])+[y]
l=int(input())
count=0
for x in d:
    a=len(d[x])
    for i in range(a):
        for j in range(i+1,a):
            if abs(d[x][i]-d[x][j])==l:
                count+=1
print(count)
