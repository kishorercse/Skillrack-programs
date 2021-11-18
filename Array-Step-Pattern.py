"""
The program must accept an integer array of size N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s): 
1 <= N <= 100 
1 <= Each integer value <= 10^7 

Input Format: 
The first line contains N. 
The second line contains N integers separated by a space.

Output Format: 
The first N lines containing the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
Input:
4
24 6 9800 454 

Output: 
24
**6
***9800 
*******454 

Example Input/Output 2:
Input: 
7
1 12 456 9877 12005 464 5 

Output: 
1
*12
***456
******9877
**********12005
***************464
******************5
"""
n=int(input())
l=input().split()
print(l[0])
t=len(l[0])
for i in range(1,n):
    print('*'*t,l[i],sep='')
    t+=len(l[i])
