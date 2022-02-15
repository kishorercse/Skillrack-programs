"""
The program must accept the coordinates (x, y) of N points as the input. The program must print the lengths of all possible horizontal lines that can be formed using 
the given N points as the output. The lengths of the horizontal lines must be printed in sorted order. If it is not possible to form horizontal lines, then the program
must print -1 as the output.

Note: All N points are always distinct.

Boundary Condition(s):
2 <= N <= 500
-10 <= x, y <= 10

Input Format:
The first line contains N.
The next N lines, each contains two integers separated by a space representing the coordinates(x, y) of a point.

Output Format:
The first line contains the integer values separated by a space representing the lengths of all possible horizontal lines that can be formed using the given N points.

Example Input/Output 1:
Input:
9
1 1
-2 -1
-2 3
-1 1
2 -1
0 3
2 2
4 -1
2 1

Output:
1 2 2 2 3 4 6

Explanation:
The start and end coordinates of the 7 possible horizontal lines are given below.
Length 1: (1, 1) to (2, 1)
Length 2: (-2, 3) to (0, 3)
Length 2: (-1, 1) to (1, 1)
Length 2: (2, -1) to (4, -1)
Length 3: (-1, 1) to (2, 1)
Length 4: (-2, -1) to (2, -1)
Length 6: (-2, -1) to (4, -1)

Example Input/Output 2:
Input:
5
-2 2
0 1
1 3
-1 -1
-1 0

Output:
-1
"""
n=int(input())
d={}
for _ in range(n):
    x,y=map(int,input().split())
    try:
        d[y].append(x)
    except KeyError:
        d[y]=[x]
res=[]
for y in d:
    l=len(d[y])
    for i in range(l):
        for j in range(i+1,l):
            res.append(abs(d[y][i]-d[y][j]))
if res:
    print(*sorted(res))
else:
    print(-1)
