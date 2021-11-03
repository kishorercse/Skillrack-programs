"""
The program must accept an array of N integers as the input. The program must transfer the LSB of each integer to the MSB of its next integer in the given array. For the last 
integer in the array, consider the first integer as the next integer. Then the program must print the revised values of the N integers as the output. 

Boundary Condition(s):
2 <= N <= 100 
1 <= Each integer value <= 10^8 

Input Format: 
The first line contains N. 
The second line contains N integer values separated by a space.

Output Format: 
The first line contains the revised N integers separated by a space.

Example Input/Output 1:
Input: 
4 
174 27 120 79 

Output:
215 13 124 39 

Explanation: 
The binary representations of the 4 integers are given below. 
10101110 11011 1111000 1001111 
After transferring the LSB of each integer to the MSB of its next integer, the binary representations become 
11010111 01101 1111100 0100111 

Example Input/Output 2:
Input:
6 
10 9 15 12 14 5 

Output:
13 4 15 14 7 2 

Explanation: 
The binary representations of the 6 integers are given below.
1010 1001 1111 1100 1110 101 
After transferring the LSB of each integer to the MSB of its next integer, the binary representations become 
1101 0100 1111 1110 0111 010
"""
n=int(input())
l=[bin(i)[2:] for i in list(map(int,input().split()))]
for i in range(n):
    l[i]=l[i-1][-1]+l[i]
    l[i-1]=l[i-1][:-1]
print(*[int(i,2) for i in l])
