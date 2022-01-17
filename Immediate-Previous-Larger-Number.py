"""
N numbers are passed as input to the program. The program must print the immediate previous larger number. If there is no such larger number print 0 for that specific number.

Note: As N can be as high as 100000, optimize your algorithm to avoid timeout.

Input Format:
The first line contains N.
The second line contains N numbers separated by a space.

Output Format:
The first line contains N numbers which denote the immediate previous larger number.

Boundary Conditions:
2 <= N <= 100000

Example Input/Output 1:
Input:
11
455 346 76 304 488 374 385 433 350 9 1000

Output:
0 455 346 346 0 488 488 488 433 350 0
"""
n=int(input())
l=list(map(int,input().split()))
stack=[]
for i in range(n):
    while stack and stack[-1]<=l[i]:
        stack.pop()
    if stack:
        print(stack[-1],end=' ')
    else:
        print(0,end=' ')
    stack.append(l[i])
