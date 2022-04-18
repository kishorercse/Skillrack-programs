"""
The program must accept a matrix of size R*C representing R*C cities. A person visits the cities from the top-left position and he marks the visited cities with the
integers starting from 1. The integers in the matrix represent the cities he visited. The asterisks in the matrix represent the cities he has not visited. The program
must print the directions (N-North, S-South, E-East and W-West) in which he visited the cities as the output.

Boundary Condition(s):
2 <= R, C <= 25

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C values separated by a space.

Output Format:
The first line contains a list of characters separated by a space representing the directions in which the person visited the cities.

Example Input/Output 1:
Input:
5 5
1 2 * 8 9
* 3 6 7 10
* 4 5 * 11
* * 16 * 12
* * 15 14 13

Output:
E S S E N E N E S S S S W W N

Explanation:
Here R = 5 and C = 5.
The person visits 16 cities(1 - 16) starting from the top-left position.
The directions in which he visited the 16 cities are given below.
E S S E N E N E S S S S W W N

Example Input/Output 2:
Input:
7 5
1 * 5 6 7
2 3 4 * 8
* * * * 9
20 * * 11 10
19 * 13 12 *
18 15 14 * *
17 16 * * *

Output:
S E E N E E S S S W S W S W S W N N N
"""
r,c=map(int,input().split())
m=[input().split() for _ in range(r)]
a,b=0,0
while True:
    m[a][b]=int(m[a][b])
    if a-1>=0 and m[a-1][b].isdigit() and int(m[a-1][b])==m[a][b]+1:
        print('N',end=' ')
        m[a][b]='*'
        a-=1
    elif a+1<r and m[a+1][b].isdigit() and int(m[a+1][b])==m[a][b]+1:
        print('S',end=' ')
        m[a][b]='*'
        a+=1
    elif b-1>=0 and m[a][b-1].isdigit() and int(m[a][b-1])==m[a][b]+1:
        print('W',end=' ')
        m[a][b]='*'
        b-=1
    elif b+1<c and m[a][b+1].isdigit() and int(m[a][b+1])==m[a][b]+1:
        print('E',end=' ')
        m[a][b]='*'
        b+=1
    else:
        break
