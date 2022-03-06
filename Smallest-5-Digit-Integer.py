"""
The program must accept an integer S as the input. The program must print the smallest 5-digit integer whose sum of digits is equal to S. If it is not possible to form such an
integer, then the program must print -1 as the output.

Boundary Condition(s):
1 <= S <= 50

Input Format:
The first line contains S.

Output Format:
The first line contains the smallest 5-digit integer whose sum of digits is equal to S.

Example Input/Output 1:
Input:
10

Output:
10009

Explanation:
Here S = 10.
The smallest possible 5-digit integer that can be formed is 10009 (1 + 0 + 0 + 0 + 9 = 10).

Example Input/Output 2:
Input:
46

Output:
-1

Example Input/Output 3:
Input:
25

Output:
10699
"""
s=int(input())
if (s>45):
    print(-1)
    exit()
n=[]
d=9
while s>0:
    while s>=d:
        s-=d
        n.append(d)
    d=s
l=len(n)
n.sort()
if l<5:
    n.insert(0,1)
    n[1]-=1
    l+=1
print(n[0],'0'*(5-l),*n[1:],sep='')
