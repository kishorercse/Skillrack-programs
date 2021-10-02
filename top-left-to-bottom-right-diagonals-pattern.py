"""
The program must accept an integer N as the input. The program must form a grid of hyphens of size (N^2)*(N^2).
Then the program must replace the top-left to bttom-right diagonal in each N*N subgrid with asterisks. Finally,
the program must print the (N^2)*(N^2) grid as the output.

Boundary Condition(s):
1 <= N <= 15

Input Format:
The first line contains N

Output Format:
The first N*N lines contain the pattern as shown in the Example Input/Output section.

Example Input/Output 1:
Input:
2

Output:
* - * -
- * - *
* - * -
- * - *

Explanation:
Here N=2, so the pattern contains 4 lines(2*2) of output and each line contains 4 character(2*2) separated by a space.
In the 4*4 grid of hyphens, the top-left to bottom-right diagonal of each 2*2 subgrid is replaced with asterisks.

Example Input/Output 2:
Input:
3

Output: 
* - - * - - * - -
- * - - * - - * - 
- - * - - * - - * 
* - - * - - * - - 
- * - - * - - * - 
- - * - - * - - * 
* - - * - - * - - 
- * - - * - - * - 
- - * - - * - - *
"""
n=int(input())
t=n*n
for i in range(t):
    for j in range(t):
        if i%n==j%n:
            print('* ',end='')
        else:
            print('- ',end='')
    print()
