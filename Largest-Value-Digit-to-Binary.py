"""
The program must accept an integer N as the input. The program must print the largest integer that can be formed by replacing a digit with its binary representation in the 
integer N. 

Boundary Condition(s): 
1 <= N <= 10^8 

Input Format: 
The first line contains N.

Output Format: 
The first line contains an integer value representing the largest integer that can be formed by replacing a digit with its binary representation in the integer N. 

Example Input/Output 1: 
Input: 
392 

Output: 
310012 

Explanation: 
Here N = 392. 
The three possible integer values are given below. 
1192 (3 -> 11) 
310012 (9 -> 1001) 
3910 (2 -> 10) 
Hence the largest integer 310012 is printed as the output. 

Example Input/Output 2: 
Input: 
4765 

Output: 
476101
"""
s=input().strip()
l=len(s)
mx=int(s)
for i in range(l):
    t=int(s[:i]+bin(int(s[i]))[2:]+s[i+1:])
    if t>mx:
        mx=t
print(mx)
