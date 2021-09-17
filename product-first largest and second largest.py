"""
The program must accept an integer N as the input. The program must print the product of the first largest digit and the second largest digit in N as the output. 

Boundary Condition(s): 
10 <= N <= 10^15 

Input Format: 
The first line contains the integer N. 

Output Format: 
The first line contains the product of the first largest digit and the second largest digit. 

Example Input/Output 1: 
Input: 
73483 

Output: 
56 

Explanation: 
The first largest digit in 73483 is 8. 
The second largest digit in 73483 is 7. 
The product of 8 and 7 is 56. 
Hence the output is 56 

Example Input/Output 2: 
Input: 
37457 

Output: 
49
"""
n=list(map(int,input()))
mx=-1
l=len(n)
for i in range(l):
    if n[i]>mx:
        mx=n[i]
        ind=i
n[ind]=-1
smx=-1
for i in n:
    if i>=smx:
        smx=i
print(mx*smx)
