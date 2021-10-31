"""
The program must accept N integers and an integer X as the input. The program must print the sum of the first X integers among the N integers. Then the program must print the sum 
of the last X integers among the N integers as the output.

Boundary Condition(s):
2 <= X <= N <= 100 
1 <= Each integer value <= 10^6 

Input Format:
The first line contains N. 
The second line contains N integers separated by a space. 
The third line contains X. 

Output Format: 
The first line contains two integers representing the sum values as per the given conditions. 

Example Input/Output 1: 
Input: 
5 
10 20 30 50 40 
2 

Output: 
30 90 

Explanation:
Here X = 2. 
The sum of the first 2 integers in the given 5 integers is 30 (10 + 20). 
The sum of the last 2 integers in the given 5 integers is 90 (50 + 40). 
Hence the output is 30 90 

Example Input/Output 2: 
Input:
6 
5 8 1 6 2 3 
4 

Output: 
20 12
"""
n=int(input())
l=list(map(int,input().split()))
x=int(input())
for i in range(1,n):
    l[i]+=l[i-1]
if x==n:
    last=l[-1]
else:
    last=l[-1]-l[-x-1]
print(l[x-1],last)
