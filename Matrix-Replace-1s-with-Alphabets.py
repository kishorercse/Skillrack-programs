"""
The program must accept an integer matrix of size R*C and an alphabet CH as the input. The program must replace all the 1s with the alphabets starting from CH. Consider the 
English alphabet set in circular fashion when replacing the 1s. Finally, the program must print the revised matrix as the output.

Boundary Condition(s):
2 <= R, C <= 50

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C integer values separated by a space.
The R+2nd line contains CH.

Output Format:
The first R lines contain the revised matrix.

Example Input/Output 1:
Input:
3 4
0 1 0 1
0 0 0 0
1 0 0 1
x

Output:
0 x 0 y
0 0 0 0
z 0 0 a

Explanation:
Here R=3, C=4 and the given 3*4 matrix is
0 1 0 1
0 0 0 0
1 0 0 1
The given alphabet CH is 'x'.
After replacing the 1s with the alphabets starting from 'x', the matrix becomes
0 x 0 y
0 0 0 0
z 0 0 a

Example Input/Output 2:
Input:
4 4
0 0 0 1
0 0 0 0
0 0 0 1
1 1 1 1
C

Output:
0 0 0 C
0 0 0 0
0 0 0 D
E F G H
"""
r,c=map(int,input().split())
m=[input().split() for _ in range(r)]
s="abcdefghijklmnopqrstuvwxyz"
ch=input().strip()
if ch.isupper():
    s=s.upper()
ind=s.index(ch)
for i in range(r):
    for j in range(c):
        if m[i][j]=='1':
            print(s[ind],end=' ')
            ind=(ind+1)%26
        else:
            print(0,end=' ')
    print()
