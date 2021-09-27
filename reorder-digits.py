"""
The program must accept two integer values N, A and rearrange the digits in N so that it forms the smallest possible
value T which is greater than or equal to A. Assume such a re-arrangement is always possible.

Boundary Condition(s):
1 <= N, A <=10^9

Input Format:
The first line contains N and A separated by a space. 

Output Format: 
The first line contains an integer value T representing the smallest possible value which is greater than or equal to A. 
  
Example Input/Output 1: 
Input: 
145 430 

Output: 
451 

Explanation: 
Here N=145 and A=430 
All the possible values that can be formed by rearranging the digits of 145 are 145, 154, 415, 451, 514 and 541. 
The smallest possible value which is greater than or equal to 430 is 451. So 451 is printed as the output. 

Example Input/Output 2: 
Input: 
1000 987 

Output: 
1000
"""
from itertools import permutations
n,a=input().split()
a=int(a)
mx=int(''.join(sorted(n,reverse=True)))
p=permutations(n)
for i in p:
  t=int(''.join(i))
  if t>=a and t<=mx:
    mx=t
print(mx)
