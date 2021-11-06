"""
The program must accept an array of N integers as the input. The program must find the binary representation of each integer in the array. Then the program must concatenate the 
binary representations of the N integers. Then the program must split the entire binary representation into bytes(8 bits) from LSB(Least Significant Bit). Finally, the program 
must print the decimal equivalent of each byte as the output. 

Boundary Condition(s): 
1 <= N <= 10^4 
1 <= Each integer value <= 10^8 

Input Format: 
The first line contains N. 
The second line contains N integer values separated by a space. 

Output Format: 
The first line contains the decimal equivalent of each byte separated by a space. 

Example Input/Output 1: 
Input: 
5 
110 40 85 63 33 

Output:
221 69 95 225

Explanation: 
110 -> 1101110 
40 -> 101000 
85 -> 1010101 
63 -> 111111 
33 -> 100001 
The concatenated binary representation is given below.
11011101010001010101111111100001
After dividing the binary representation into bytes(8 bits) from LSB, the bytes and their corresponding decimal values are given below. 
11011101 -> 221 
01000101 -> 69 
01011111 -> 95 
11100001 -> 225 

Example Input/Output 2: 
Input: 
4
8 10 5 1 

Output: 
8 171 
"""
n=int(input())
l=list(map(int,input().split()))
s=''
for i in l:
    s+=bin(i)[2:]
t=len(s)
c=t%8
if c>0:
    s='0'*(8-c)+s
    t+=8-c
i=0
while i<t:
    print(int(s[i:i+8],2),end=' ')
    i+=8
