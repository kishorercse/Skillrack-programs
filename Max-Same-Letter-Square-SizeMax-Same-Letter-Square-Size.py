""
Certain kids were playing a game in which they would draw a N*N matrix and would fill in a letter from A to Z in a given cell based on certain rules. Without getting into the 
details of those rules, the final values present in the N*N matrix is passed as the input to the program. The program must print the size of the largest square sub-matrix which 
has all the letters equal in it.

Input Format:
The first line will contain N.
The next N lines will each contain N letters separated by a space.

Output Format:
The first line will contain the size of the largest square sub-matrix with all the letters equal in it.

Boundary Conditions:
3 <= N <= 50

Example Input/Output 1:
Input:
5
A H K L O
J H H B U
Q H H H Z
I E H H W
F H H W Z

Output:
2

Explanation:
The two 2*2 sub-matrices filled with H are the largest.

Example Input/Output 1:
Input:
7
B C C C C J K
O P Q R S T C
H S S S S S S
J K S S S S S
K I S S S S U
G H S S S S V
Y Y Y X D Q T

Output:
4

Explanation:
The 4*4 sub-matrix filled with S is the largest.
"""
n=int(input())
m=[input().split() for _ in range(n)]
for k in range(n,0,-1):
    for i in range(n-k+1):
        for j in range(n-k+1):
            t=m[i][j]
            f=True
            for ii in range(i,i+k):
                for jj in range(j,j+k):
                    if t!=m[ii][jj]:
                        f=False
                        break
                if not f:
                    break
            if f:
                print(k)
                exit()
