"""
The program must accept N integers as the input. For each integer X among the N integers, the program must find the last occurrence of 1 in the binary representation of X. Then 
the program must find the corresponding power of 2 value for that last occurrence of 1. Finally, the program must print the sum S of those powers of 2 as the output. 

Boundary Condition(s):
1 <= N <= 100 
1 <= Each integer value <= 10^8

Input Format: 
The first line contains N. 
The second line contains N integers separated by a space. 

Output Format:
The first line contains S. 

Example Input/Output 1: 
Input:
5
12 10 8 15 22 

Output: 
17 

Explanation: 
12 -> 1100 -> 4 
10 -> 1010 -> 2 
8 -> 1000 -> 8 
15 -> 1111 -> 1 
22 -> 10110 -> 2 
4 + 2 + 8 + 1 + 2 = 17 

Example Input/Output 2: 
Input:
4 
100 64 55 72 

Output:
77 

Explanation: 
100 -> 1100100 -> 4 
64 -> 1000000 -> 64 
55 -> 110111 -> 1 
72 -> 1001000 -> 8
4 + 64 + 1 + 8 = 77
"""
n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    power=1
    while i>0:
        if i&1:
            s+=power
            break
        power=power<<1
        i=i>>1
print(s)
