"""
Given an integer N as the input, print the pattern as given in the Example Input/Output section.

Input Format:
The first line contains N.

Output Format:
2N-1 lines containing the desired pattern.

Boundary Conditions:
2 <= N <= 50

Example Input/Output 1:
Input:
3

Output:
0 0 1 0 0
0 2 0 8 0
3 0 0 0 7
0 4 0 6 0
0 0 5 0 0

Example Input/Output 2:
Input:
5

Output:
0 0 0 0 1 0 0 0 0
0 0 0 2 0 16 0 0 0
0 0 3 0 0 0 15 0 0
0 4 0 0 0 0 0 14 0
5 0 0 0 0 0 0 0 13
0 6 0 0 0 0 0 12 0
0 0 7 0 0 0 11 0 0
0 0 0 8 0 10 0 0 0
0 0 0 0 9 0 0 0 0
"""
n=int(input())
t=n
x=n-1
y=n-1
n=2*n-1
a=1
b=2*n-2
for i in range(n):
    for j in range(n):
        if j==x:
            print(a,end=' ')
            a+=1
        elif j==y:
            print(b,end=' ')
            b-=1
        else:
            print('0',end=' ')
    if i<t-1:
        x-=1
        y+=1
    else:
        x+=1
        y-=1
    print()
