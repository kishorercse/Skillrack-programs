"""
The program must accept a matrix of size R*C and an integer K as the input. The matrix contains K*K alphabets and the rest are integers. The program must rearrange the matrix 
so that all K*K alphabets must be present at the bottom-right K*K submatrix. The integers and alphabets must be arranged in the order of their occurrence. Then the program must
print the revised matrix as the output.
Note: The value of K is always less than or equal to both R and C.

Boundary Condition(s):
2 <= R, C <= 50
1 <= Value of each integer in the matrix <= 10^5

Input Format:
The first line contains R, C and K separated by a space.
The next R lines contain the matrix.

Output Format:
The first R lines contain the revised matrix.

Example Input/Output 1:
Input:
5 5 3
90 b 86 76 i
a 14 c 99 12
91 d 64 54 e
82 78 51 f 67
h 43 g 56 65

Output:
90 86 76 14 99
12 91 64 54 82
78 51 b i a
67 43 c d e
56 65 f h g

Explanation:
Here K = 3, so there are 9 alphabets in the matrix.
b i a c d e f h g

The remaining integers are given below.
90 86 76 14 99 12 91 64 54 82 78 51 67 43 56 65

After rearranging the alphabets and integers based on the given conditions, the matrix becomes
90 86 76 14 99
12 91 64 54 82
78 51 b i a
67 43 c d e
56 65 f h g

Example Input/Output 2:
Input:
6 4 2
A B 49 42
97 59 95 17
D C 44 25
24 37 26 19
76 78 91 86
54 60 81 61

Output:
49 42 97 59
95 17 44 25
24 37 26 19
76 78 91 86
54 60 A B
81 61 D C
"""
r,c,k=map(int,input().split())
m=[]
al=[]
ind=0
for _ in range(r):
    m+=input().split()
for i in range(r):
    for j in range(c):
        if m[ind].isalpha():
            al.append(m[ind])
            m[ind]=''
        ind+=1
ind=0
try:
    while m[ind]=='':
        ind+=1
except IndexError:
    pass
for i in range(r-k):
    for j in range(c):
        print(m[ind],end=' ')
        ind+=1
        try:
            while m[ind]=='':
                ind+=1
        except IndexError:
            pass
    print()
x=0
for i in range(k):
    for j in range(c-k):
        print(m[ind],end=' ')
        ind+=1
        try:
            while m[ind]=='':
                ind+=1
        except IndexError:
            pass
    for j in range(k):
        print(al[x],end=' ')
        x+=1
    print()
