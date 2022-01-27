"""
The program must accept N pairs of integers as the input. For each pair (X, Y), the program must print the integers from 1 to X*Y within a pair of square brackets, where every
Y integers must be enclosed within a pair of square brackets.

Boundary Condition(s):
1 <= N, X, Y <= 100

Input Format:
The first line contains N.
The next N lines, each contains two integers X and Y separated by a space.

Output Format:
The first N lines contain the pattern as shown in the Example Input/Output section.

Example Input/Output 1:
Input:
3
2 2
4 2
2 4

Output:
[[1 2] [3 4]]
[[1 2] [3 4] [5 6] [7 8]]
[[1 2 3 4] [5 6 7 8]]

Explanation:
1st pair (2, 2): The first line contains the integers from 1 to 4 (2*2).
[[1 2] [3 4]] -> Every 2 integers are enclosed within a pair of square brackets.

2nd pair (4, 2): The second line contains the integers from 1 to 8 (4*2).
[[1 2] [3 4] [5 6] [7 8]] -> Every 2 integers are enclosed within a pair of square brackets.

3rd pair (2, 4): The third line contains the integers from 1 to 8 (2*4).
[[1 2 3 4] [5 6 7 8]] -> Every 4 integers are enclosed within a pair of square brackets.

Example Input/Output 2:
Input:
6
2 1
3 3
3 2
4 1
1 4
5 2

Output:
[[1] [2]]
[[1 2 3] [4 5 6] [7 8 9]]
[[1 2] [3 4] [5 6]]
[[1] [2] [3] [4]]
[[1 2 3 4]]
[[1 2] [3 4] [5 6] [7 8] [9 10]]
"""
n=int(input())
while n>0:
    x,y=map(int,input().split())
    t=x*y
    print('[[',end='')
    for i in range(1,t):
        if i%y==0:
            print(i,'] [',sep='',end='')
        else:
            print(i,end=' ')
    print(t,']]',sep='')
    n-=1
