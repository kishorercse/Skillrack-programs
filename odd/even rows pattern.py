"""
The program must accept an integer N as the input. The program must print the integer values in N lines
based on the following conditions.
- If the row number X is odd, then the Xth row contains X consecutive odd integers sorted in ascending order.
- If the row number x is even, then the Xth row contains X consecutive even integers sorted in ascending order.
- The last integer in each row must be equal to the square of the row number X.

Boundary Condition(s):
1 <= N <= 100

Input Format:
The first line contains N. 

Output Format: 
The first N lines contain the integer values based on the given conditions. 

Example Input/Output 1: 
Input: 
5 

Output: 
1 
2 4 
5 7 9 
10 12 14 16 
17 19 21 23 25 
Explanation: 
X = 1: 1 (only 1 odd integer) 
X = 2: 2 4 (2 consecutive even integers ending with 2*2) 
X = 3: 5 7 9 (3 consecutive odd integers ending with 3*3) 
X = 4: 10 12 14 16 (4 consecutive even integers ending with 4*4) 
X = 5: 17 19 21 23 25 (5 consecutive odd integers ending with 5*5) 

Example Input/Output 2: 
Input: 
8 

Output: 
1 
2 4 
5 7 9 
10 12 14 16 
17 19 21 23 25 
26 28 30 32 34 36 
37 39 41 43 45 47 49 
50 52 54 56 58 60 62 64
"""
n=int(input())
t=1
for i in range(1,n+1):
  for _ in range(i):
    print(t,end=' ')
    t+=2
  t-=1
  print()
