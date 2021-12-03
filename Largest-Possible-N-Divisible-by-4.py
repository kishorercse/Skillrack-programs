"""
The program must accept an integer N as the input. The program must print the largest possible integer divisible by 4 from the digits of N. If it is not possible to form such
an integer, the program must print -1 as the output.
Note: The largest possible integer divisible by 4 has no leading zeros.

Boundary Condition(s):
2 <= N <= 10^8

Input Format:
The first line contains N.

Output Format:
The first line contains the largest possible integer divisible by 4 from the digits of N or -1.

Example Input/Output 1:
Input:
102

Output:
120

Explanation:
Here the largest possible integer divisible by 4 from the digits of 102 is 120.
Hence the output is 120

Example Input/Output 2:
Input:
1345

Output:
-1
"""
from itertools import permutations
n=permutations(input().strip())
mx=-1
for i in n:
    t=int(''.join(i))
    if t%4==0 and t>mx:
        mx=t
print(mx)
