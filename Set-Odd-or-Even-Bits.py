"""
The program must accept an integer N as the input. If N is odd, then the program must modify N by setting all the bits at the odd positions from LSB. Else the program must
modify N by setting all the bits at the even positions from LSB. Then the program must print the revised value of N as the output.

Boundary Condition(s):
1 <= N <= 10^8

Input Format:
The first line contains N.

Output Format:
The first line contains the revised value of N.

Example Input/Output 1:
Input:
45

Output:
61

Explanation:
Here N = 45 which is an odd integer.
45 -> 101101 -> 111101 -> 61

Example Input/Output 2:
Input:
326

Output:
494

Explanation:
Here N = 326 which is an even integer.
326 -> 101000110 -> 111101110 -> 494
"""
from math import log2,floor
n=int(input())
bits=floor(log2(n))+1
s=['0']*bits
if n&1:
    for i in range(bits-1,-1,-2):
        s[i]='1'
else:
    for i in range(bits-2,-1,-2):
        s[i]='1'
print(n|int(''.join(s),2))
