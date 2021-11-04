"""
The program must accept an integer n as the input. the program must find the binary representation of n. Then the program must print the powers of two indicated by the set bits in
the binary representation of n as shown in the example input/output section. 

Boundary condition(s): 
1 <= n <= 10^18 

Input format:
The first line contains n. 

Output format: 
The first line contains the powers of two indicated by the set bits in the binary representation of n. 

Example input/output 1: I
nput: 
10 

Output: 
8+2 

Explanation: 
Here n = 10 whose binary representation is 1010. 
1 -> 1*2^3 = 8
0 -> 0*2^2 = 0 
1 -> 1*2^1 = 2 
0 -> 0*2^0 = 0
Hence the output is 8+2. 

Example input/output 2:
Input: 
15 

Output: 
8+4+2+1 

Example input/output 3: 
Input: 
83 

Output: 
64+16+2+1 
"""
def binary(n,p):
    if n==0:
        return
    binary(n>>1,p<<1)
    if n&1:
        global flag
        if flag:
            print('+',end='')
        print(p,end='')
        flag=True
n=int(input())
flag=False
binary(n,1)
