"""
The program must accept an integer matrix of size RxC as the input. The program must print the desired pattern as shown in the Example Input/Output section. 

Note: The value of C is always odd. 

Boundary Condition(s): 
3 <= R, C <= 49 

Input Format:
The first line contains R and C separated by a space.
The next R lines each contain C integers separated by a space. 

Output Format:
The first R lines contain the desired pattern as shown in the Example Input/Output section. 

Example Input/Output 1: 
Input:
3 5
79 93 40 30 42
24 17 93 91 60
21 92 27 96 75

Output:
79 * * * 42
* 17 * 91 *
* * 27 * * 

Example Input/Output 2:
Input: 
4 5
4 5 3 9 3
3 1 5 5 3
3 5 5 2 6
5 8 2 8 5

Output:
* * * * *
3 * * * 3
* 5 * 2 *
* * 2 * * 

Example Input/Output 3:
Input: 
5 15
79 19 79 57 76 27 77 37 95 56 10 14 70 65 25
87 50 19 67 99 45 37 32 26 39 43 84 82 96 58
11 91 35 46 55 44 15 34 87 99 85 68 15 37 84
59 65 30 29 47 54 82 93 58 82 68 13 37 38 45
14 64 40 39 47 33 76 81 14 51 82 13 51 76 24

Output:
* * * 57 * * * * * * * 14 * * *
* * * * 99 * * * * * 43 * * * * 
* * * * * 44 * * * 99 * * * * * 
* * * * * * 82 * 58 * * * * * * 
* * * * * * * 81 * * * * * * *
"""
r,c=map(int,input().split())
m=[input().split() for _ in range(r)]
t=c//2
for i in range(r):
    for j in range(c):
        if j==t-(r-i)+1 or j==t+(r-i)-1:
            print(m[i][j],end=' ')
        else:
            print('*',end=' ')
    print()
