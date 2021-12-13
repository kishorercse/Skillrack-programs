"""
Given a value of N, where N is the number of rows, the program must print the character '*' from left or right depending on whether the row is an odd row or an even row.
- If it is an odd row, the '*' must start from left.
- If it is an even row, the '*' must start from right.

After the asterisk '*' the numbers from 1 to the row count must be printed.

Input Format:
The first line will contain the value of N

Output Format:
N lines will contain '*' forming the pattern as described.

Constraints:
2 <= N <= 25

Example Input/Output 1:
Input:
3

Output:
*1
21*
*123

Example Input/Output 2:
Input:
5

Output:
*1
21*
*123
4321*
*12345
"""
n=int(input())
s=[i for i in range(1,n+1)]
for i in range(1,n+1):
    if i%2!=0:
        print('*',*s[:i],sep='')
    else:
        print(*s[i-1::-1],'*',sep='')
