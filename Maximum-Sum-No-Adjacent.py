"""
The program must accept an integer matrix of size 2*N as the input. The program must print the maximum sum such that no two chosen integers are adjacent vertically,
diagonally or horizontally in the matrix.

Boundary Condition(s):
2 <= N <= 100
1 <= Matrix element value <= 10^5

Input Format:
The first line contains N.
The next two lines, each contains N integer values separated by a space.

Output Format:
The first line contains the maximum sum.

Example Input/Output 1:
Input:
3
2 5 6
3 1 1

Output:
9

Explanation:
The 4 possible ways are given below.
(1, 1) and (1, 3) => 2 + 6 = 8.
(1, 1) and (2, 3) => 2 + 1 = 3.
(2, 1) and (1, 3) => 3 + 6 = 9.
(2, 1) and (2, 3) => 3 + 1 = 4.
Here the maximum sum is 9, which is printed as the output.

Example Input/Output 2:
Input:
5
1 3 5 7 8
2 4 6 8 10

Output:
18

Explanation:
The maximum sum is obtained as given below.
(2, 1), (2, 3) and (2, 5) => 2 + 6 + 10 = 18.

Example Input/Output 3:
Input:
4
9 8 7 3
7 6 4 9

Output:
18
"""
n=int(input())
m=[list(map(int,input().split())) for _ in range(2)]
inc=exc=0
for j in range(n):
    new_exc=max(exc,inc)
    inc=exc+max(m[0][j],m[1][j])
    exc=new_exc
print(max(inc,exc))
