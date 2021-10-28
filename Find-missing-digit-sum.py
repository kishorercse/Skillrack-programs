"""
The program must accept N integers and their sum S, but eactly one digit is missing in an integer. The missing digit in the integer is denoted by an asterisk. The program must 
find the missing digit and print the N integers without missing any digits. 

Boundary Condition(s): 
1 <= N <= 100 
0 <= Each integer value <= 10^6 

Input Format: 
The first line contains N. 
The second line contains N integers separated by a space. 
The third line contains S. 

Output Format: 
The first line contains N integers separated by a space. 

Example Input/Output 1: 
Input: 
3 
468 120 9*5 
1573 

Output: 
468 120 985 

Explanation: 
Here N = 3 and a digit is missing in the 3rd integer. 
If the missing digit is 8, then 468 + 120 + 985 = 1573. 

Example Input/Output 2: 
Input: 
4 
15 *8652 987 52364 
152018 

Output: 
15 98652 987 52364
"""
n=int(input())
l=input().split()
s=int(input())
for i in range(n):
    try:
        t=int(l[i])
        s-=t
    except ValueError:
        x=i
l[x]=s
print(*l)
