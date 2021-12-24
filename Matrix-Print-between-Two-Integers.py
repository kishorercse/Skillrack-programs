"""
The program must accept an integer matrix of size R*C containing unique integers and two integers X, Y as the input. The integers X and Y are always present in the given matrix.
The program must print all the integers starting from X to Y in the matrix. Consider the elements of the matrix in a circular fashion when printing the integers
(i.e., once it reaches the bottom-right element, then starts from the top-left element of the matrix).

Boundary Condition(s):
2 <= R, C <= 50
1 <= Matrix element value, X, Y <= 10^4

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C integers separated by a space.
The R+2nd line contains X and Y separated by a space.

Output Format:
The first line contains all the integers starting from X to Y in the matrix separated by a space.

Example Input/Output 1:
Input:
6 5
67 54 32 74 90
93 52 39 38 82
48 50 79 56 47
26 72 20 86 58
95 10 21 77 49
17 37 66 14 87
38 66

Output:
38 82 48 50 79 56 47 26 72 20 86 58 95 10 21 77 49 17 37 66

Explanation:
Here X=38 and Y=66.
All the integers starting from 38 to 66 in the given 6*5 matrix are highlighted below.
67 54 32 74 90
93 52 39 38 82
48 50 79 56 47
26 72 20 86 58
95 10 21 77 49
17 37 66 14 87

Example Input/Output 2:
Input:
6 5
67 54 32 74 90
93 52 39 38 82
48 50 79 56 47
26 72 20 86 58
95 10 21 77 49
17 37 66 14 87
66 38

Output:
66 14 87 67 54 32 74 90 93 52 39 38

Example Input/Output 3:
Input:
4 4
89 90 78 77
73 93 92 26
79 64 43 88
99 61 29 24
26 73

Output:
26 79 64 43 88 99 61 29 24 89 90 78 77 73
"""
r,c=map(int,input().split())
m=[list(map(int,input().split())) for _ in range(r)]
x,y=map(int,input().split())
start=end=f=False
ans=[]
ans1=[]
for i in range(r):
    for j in range(c):
        if m[i][j]==x:
            start=True
            if end==False:
                ans.clear()
            else:
                f=True
        elif m[i][j]==y:
            end=True
            ans.append(m[i][j])
            if start and end:
                break
        if end and start:
            if f:
                ans1.append(m[i][j])
            else:
                break
        elif end==False or start==True:
            ans.append(m[i][j])
    if start and end and f==False:
        break
print(*ans1,*ans)
