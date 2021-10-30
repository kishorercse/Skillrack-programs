"""
The program must accept N integers and X number of pairs. Each pair contains two integers representing positions P1 and P2. For each pair, the program must find the sum of integers
from the position P1 to the position P2 and then print 1 if the sum is 0 else print 0 as the output.
Note: The N integers containing 1 and -1. 

Boundary Condition(s):
1 <= N, X <= 10^4 
1 <= P1 <= P2 <= N 

Input Format: 
The first line contains N and X separated by a space. 
The second line contains the N integers separated by space(s). 
The next X lines contain the pair of integers ( P1 and P2) separated by a space. 

Output Format: 
The first line contains the integers separated by a space as per the given conditions. 

Example Input/Output 1:
Input: 
7 2 
-1 1 1 -1 1 -1 -1 
1 7 
4 5 

Output:
0 1

Explanation: 
For the 1st pair (1, 7), the sum of integers from the position 1 to the position 7 (-1 + 1 + 1 + -1 + 1 + -1 + -1) is -1. So 0 is printed. 
For the 2nd pair (4, 5), the sum of integers from the position 4 to the position 5 (-1 + 1) is 0. So 1 is printed.
Hence the output is 0 1 

Example Input/Output 2:
Input:
5 4 
-1 1 -1 1 1 
3 4 
5 4 
1 2 
2 3 

Output: 
1 0 1 1
"""
n,x=map(int,input().split())
l=list(map(int,input().split()))
for i in range(1,n):
    l[i]+=l[i-1]
while x>0:
    p1,p2=map(int,input().split())
    p1-=1
    t=l[p2-1]
    if p1>0:
        t-=l[p1-1]
    print(1 if t==0 else 0,end=' ')
    x-=1
