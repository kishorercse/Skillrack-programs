"""
The program must accept N integers as the input. The program must print the number of set bits that occur in the same positions from LSB(Least Significant Bit) of the given N 
integers as the output. 

Boundary Condition(s): 
1 <= N <= 100 
1 <= Each integer value <= 10^8 

Input Format: 
The first line contains N. 
The second line contains N integer values separated by a space. 

Output Format: 
The first line contains an integer representing the number of set bits that occur in the same positions from LSB.

Example Input/Output 1: 
Input: 
4
11 75 57 59 

Output:
2 

Explanation: 
11 -> 0001011 
75 -> 1001011 
57 -> 0111001 
59 -> 0111011 
1st bit from LSB of all 4 integers are equal to 1. 
4th bit from LSB of all 4 integers are equal to 1. 
So 2 printed as the output. 

Example Input/Output 2: 
Input: 
5 
486 495 299 431 511

Output:
3
"""
n=int(input())
l=list(map(int,input().split()))
count=0
t=min(l)
while t!=0:
    a=0
    for i in range(n):
        if l[i]&1:
           a+=1
        l[i]=l[i]>>1
    if a==n:
        count+=1
    t=t>>1
print(count)
