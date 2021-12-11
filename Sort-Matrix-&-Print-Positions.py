"""
The program must accept an integer matrix of size R*C containing only unique integers as the input. The program must sort the integers in the given matrix. Then the program 
must print the original positions of the integers in the matrix as shown in the Example Input/Output section.

Boundary Condition(s):
2 <= R, C <= 50
1 <= Matrix element value <= 10^5

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C integers separated by a space.

Output Format:
The first R lines contain the original positions(row-col) of the integers in the sorted matrix.

Example Input/Output 1:
Input:
3 3
50 40 80
20 30 90
10 60 70

Output:
3-1 2-1 2-2
1-2 1-1 3-2
3-3 1-3 2-3

Explanation:
After sorting the integers in the given 3*3 matrix, the matrix becomes
10 20 30
40 50 60
70 80 90
So their original positions are printed as the output.

Example Input/Output 2:
Input:
4 2
42 14
62 73
25 64
74 92

Output:
1-2 3-1
1-1 2-1
3-2 2-2
4-1 4-2
"""
r,c=map(int,input().split())
m=[]
for i in range(r):
    t=input().split()
    m+=[[int(t[j]),i+1,j+1] for j in range(c)]
m.sort()
ind=0
for i in range(r):
    for j in range(c):
        print(*m[ind][1:],sep='-',end=' ')
        ind+=1
    print()
