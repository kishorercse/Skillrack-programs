"""
The program must accept a list of integer-alphabet pairs and two integers R, C as the input. The sum of the integers present in all the integer-alphabet pairs is always equal
to the product of R and C. The program must form a matrix of size R*C based on the following conditions.
- The program must expand each integer-alphabet pair by repeating the specified alphabet X times, where X represents the integer value present in the pair.
- Then the program must fill the matrix with the expanded alphabets from the 1st row to the Rth row, where left to right in each row.
Finally, the program must print the R*C matrix as the output.

Boundary Condition(s):
2 <= R, C <= 50

Input Format:
The first line contains a list of integer-alphabet pairs separated by a space.
The second line contains R and C separated by a space.

Output Format:
The first R lines, each contains C alphabets separated by a space.

Example Input/Output 1:
Input:
3a 5b 2c 6d
4 4

Output:
a a a b
b b b b
c c d d
d d d d

Explanation:
Here R = 4 and C = 4.
There are 4 integer-alphabet pairs which are expanded as given below.
3a -> a a a
5b -> b b b b b
2c -> c c c
6d -> d d d d d d
So the 4*4 matrix is formed as given below.
a a a b
b b b b
c c d d
d d d d

Example Input/Output 2:
Input:
10R 5o 7c 4k 4s
5 6

Output:
R R R R R R
R R R R o o
o o o c c c
c c c c k k
k k s s s s
"""
def separate(s):
    l=len(s)
    for i in range(l):
        if s[i].isalpha():
            return [int(s[:i]),s[i:]]
l=[separate(i) for i in input().split()]
ind=0
r,c=map(int,input().split())
for i in range(r):
    for j in range(c):
        print(l[ind][1],end=' ')
        l[ind][0]-=1
        if l[ind][0]==0:
            ind+=1
    print()
