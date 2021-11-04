"""
The program must accept an integer N as the input. The program must print the reducing triangular wave pattern as shown in the Example Input/Output section. 

Boundary Condition(s): 
3 <= N <= 50 

Input Format: 
The first line contains N. 

Output Format: 
The first N lines contain the reducing triangular wave pattern as shown in the Example Input/Output section. 

Example Input/Output 1: 
Input: 
5 

Output: 
# 
* # * * * * * #
* * # * * * # * # * # 
* * * # * # * * * # 
* * * * # 

Explanation: 
Here N=5, so the pattern contains 5 lines of reducing triangular wave pattern. 

Example Input/Output 2: 
Input: 
8 

Output: 
#
* # * * * * * * * * * * * # 
* * # * * * * * * * * * # * # * * * * * * * # 
* * * # * * * * * * * # * * * # * * * * * # * # * * * # 
* * * * # * * * * * # * * * * * # * * * # * * * # * # * # 
* * * * * # * * * # * * * * * * * # * # * * * * * # 
* * * * * * # * # * * * * * * * * * # 
* * * * * * * #
"""
n=int(input())
m=['*'*i+'#' for i in range(n)]
a,b=1,n-1
for c in range(1,n-1):
    t=1
    if c%2==0:
        for i in range(a,b):
            m[i]+='*'*t+'#'
            t+=2
        b-=1
    else:
        for i in range(b-1,a-1,-1):
            m[i]+='*'*t+'#'
            t+=2
        a+=1
for i in m:
    print(*i)
