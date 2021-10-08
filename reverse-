"""
The program must accept a string S and repeat the alphabets from the end till a new string S2 of length N is formed. Then the program must print the value of S2. 

Boundary Condition(s):
1 <= Length of S <= 1000 
1 <= N <= 10000 

Input Format:
The first line contains S. 
The second line contains N. 

Output Format: 
The first line contains S2.

Example Input/Output 1: 
Input: 
abc 
5

Output: 
cbacb 

Explanation:
The alphabets are repeated from the end till the new string's length is 5. 

Example Input/Output 2: 
Input:
work 
10

Output:
krowkrowkr
"""
s=input().strip()
n=int(input())
l=len(s)
j=l-1
while n>0:
    print(s[j],end='')
    j=(j-1)%l
    n-=1
