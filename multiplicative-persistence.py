"""
The program must accept an integer N and print its multiplicative persistence, which is the number of times we must
multiply the digits in N unitil we reach a single digit.

Boundary Condition(s):
1 <= N <= 10^16

Input Format:
The first line contains N.

Output Format:
The first line contains an integer value representing the multiplicative persistence. 

Example Input/Output 1: 
Input:
49

Output: 
3

Explanation:
1st time - 4*9 = 36.
2nd time - 3*6 = 18. 
3rd time - 1*8 = 8. 
So 3 is printed as the output. 

Example Input/Output 2: 
Input:
41

Output: 
1
"""
def product(n):
    n=str(n)
    m=1
    for i in n:
        m*=int(i)
    return m
n=int(input())
count=0
while n>9:
    n=product(n)
    count+=1
print(count)
