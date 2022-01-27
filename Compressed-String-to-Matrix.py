"""
The program must accept a matrix of size R*C containing compressed string values as the input. A compressed string contains alphabet-integer pairs which represent the alphabets 
and their frequencies. For each compressed string in the matrix, the program must expand the compressed string as a string of length 9 and print the characters in 3*3 matrix 
format as shown in the Example Input/Output section.

Boundary Condition(s):
1 <= R, C <= 15

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C compressed string values separated by a space.

Output Format:
The first R*3 lines, each contains C*3 characters separated by a space.

Example Input/Output 1:
Input:
2 2
b4c1a4 b1a1c5a2
a3b3c3 c9

Output:
b b b b a c
b c a c c c
a a a c a a
a a a c c c
b b b c c c
c c c c c c

Explanation:
Here R = 2, C = 2 and the four compressed string values are expanded as below.
b4c1a4 -> bbbbcaaaa
b b b
b c a
a a a

b1a1c5a2 -> bacccccaa
b a c
c c c
c a a

a3b3c3 -> aaabbbccc
a a a
b b b
c c c

c9 -> ccccccccc
c c c
c c c
c c c

Example Input/Output 2:
Input:
2 3
a3b3c3 b1c1a7 x4y1z4
p9 a8c1 z2y2x5

Output:
a a a b c a x x x
b b b a a a x y z
c c c a a a z z z
p p p a a a z z y
p p p a a a y x x
p p p a a c x x x
"""
from re import findall
r,c=map(int,input().split())
for _ in range(r):
    a=input().split()
    for j in range(c):
        a[j]=list(map(list,findall(r'(\w+?)(\d+)',a[j])))
    for _ in range(3):
        for j in range(c):
            for _ in range(3):
                print(a[j][0][0],end=' ')
                a[j][0][1]=int(a[j][0][1])-1
                if a[j][0][1]==0:
                    a[j].pop(0)
        print()
