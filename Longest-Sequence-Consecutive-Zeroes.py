"""
The program must accept N integers and print the integers having the longest sequence of consecutive zeroes in their reverse order of occurrence. 

Boundary Condition(s): 
1 <= N <= 10^4
1 <= Each integer value <= 10^18 

Input Format:
The first line contains N.
The second line contains N integer values separated by a space.

Output Format: 
The first line contains the integer values separated by a space.

Example Input/Output 1: 
Input: 
5
9 10 32 65 7 

Output: 
65 32 

Explanation: 
32 binary representation is 100000 having 5 consecutive zeroes. 
65 binary representation is 1000001 having 5 consecutive zeroes. 
They are printed in the reverse order of occurrence. 

Example Input/Output 2: 
Input: 
4
9 2 5 10

Output:
9
"""
n=int(input())
l=list(map(int,input().split()))
mx=0
for i in range(n):
    b=bin(l[i])[2:]
    m=count=0
    for ch in b:
        if ch=='0':
            count+=1
        else:
            m=max(count,m)
            count=0
    m=max(m,count)
    l[i]=[l[i],m]
    mx=max(m,mx)
for i in range(n-1,-1,-1):
    if l[i][1]==mx:
        print(l[i][0],end=' ')
