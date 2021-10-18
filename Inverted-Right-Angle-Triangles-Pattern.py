"""
The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section. 

Boundary Condition(s): 
2 <= N <= 50 

Input Format: 
The first line contains N. 

Output Format: 
The first N lines contain the desired pattern as shown in the Example Input/Output section. 

Example Input/Output 1: 
Input: 
3 

Output: 
*-*-*-*-* 
--*-*-* 
----* 

Explanation: 
Here N=3, so the pattern contains 3 lines of output. 
Two inverted right-angle triangles are printed using asterisks. 
The hyphens in the pattern represent the empty spaces. 

Example Input/Output 2: 
Input: 
5 

Output: 
*-*-*-*-*-*-*-*-* 
--*-----*-----* 
----*---*---* 
------*-*-* 
--------* 

Example Input/Output 3: 
Input: 
6 

Output: 
*-*-*-*-*-*-*-*-*-*-* 
--*-------*-------*
----*-----*-----*
------*---*---* 
--------*-*-*
----------*
"""
n=int(input())
print('*-'*(n*2-2),end='*\n')
hyphen=1+(n-3)*2
for i in range(1,n-1):
    print('-'*(i*2),end='*')
    print('-'*hyphen,end='*')
    print('-'*hyphen,end='*\n')
    hyphen-=2
print('-'*(2*(n-1)),end='*')
