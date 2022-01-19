"""
Given N, print the pattern as described in the Example Input/Output.

Input Format:
The first line will contain N.

Output Format:
N lines will contain the required pattern.

Boundary Conditions:
1 <= N <= 50

Example Input/Output 1:
Input:
5

Output:
1 2 3 4 5
2 4 6 8 4
4 8 12 10 8
8 16 18 20 10
16 26 36 28 20

Example Input/Output 2:
Input:
4

Output:
1 2 3 4
2 4 6 3
4 8 7 6
8 11 14 7

"""
n=int(input())
l=[]
for i in range(1,n+1):
    l.append(i)
    print(i,end=' ')
print()
for i in range(1,n):
    t=[l[1]]
    print(l[1],end=' ')
    for j in range(1,n-1):
        print(l[j-1]+l[j+1],end=' ')
        t.append(l[j-1]+l[j+1])
    t.append(l[-2])
    print(l[-2])
    l=t[:]
