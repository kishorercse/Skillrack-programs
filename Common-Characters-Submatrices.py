"""
The program must accept a character matrix of size R*C and an integer K as the input. The values of R and C are always divisible by K. The program must print the count of 
common characters in all the K*K submatrices of the given matrix.

Boundary Condition(s):
2 <= R, C <= 50

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C characters separated by a space.
The (R+2)nd line contains K.

Output Format:
The first line contains an integer representing the count of common characters in all the K*K submatrices of the given matrix.

Example Input/Output 1:
Input:
6 9
s b k g s y w g f
r g y e q j j a s
s m s a s z s l e
u s q u e h s s s
g s f h s s e s g
x d r h g y s s s
3

Output:
2

Explanation:
The 2 common characters in all the six 3*3 submatrices are given below.
s and g

Example Input/Output 2:
Input:
4 4
a A A a
9 * * 9
* 9 9 *
A a a A
2

Output:
4
"""
r,c=map(int,input().split())
m=[input().split() for _ in range(r)]
k=int(input())
count={}
n=1
for i in range(0,r,k):
    for j in range(0,c,k):
        for ii in range(i,i+k):
            for jj in range(j,j+k):
                if count.get(m[ii][jj],0)==n-1:
                    count[m[ii][jj]]=n
        n+=1
n-=1
res=0
for i in count:
    if count[i]==n:
        res+=1
print(res)
