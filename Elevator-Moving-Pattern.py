"""
There is an elevator in a building. Initially, the elevator is on the ground floor. The operator moves the elevator (up / down) based on the requests of the persons using the 
elevator. The program must accept N integers representing the N requests as the input. A positive integer X indicates that the elevator moves X floors above the current floor. 
A negative integer -X indicates that the elevator moves X floors down the current floor. The program must print the way the elevator moves as the output. The elevator must be
indicated by an asterisk and the empty spaces must be indicated by hyphens. 

Boundary Condition(s):
2 <= N <= 100 
-100 <= Each integer value <= 100

Input Format:
The first line contains N.
The second line contains N integer values separated by a space. 

Output Format: 
The lines contain the way the elevator moves. 

Example Input/Output 1: 
Input: 
6
2 4 -5 7 3 -4

Output:
----*- 
----** 
----** 
---*-* 
---*-* 
-*-*-- 
-***-- 
-***-- 
-***-- 
*-**-- 
*-*--- 

Explanation: 
1st column: 2 floors up 
2nd column: 4 floors up 
3rd column: 5 floors down
4th column: 7 floors up 
5th column: 3 floors up 
6th column: 4 floors down

Example Input/Output 2:
Input:
4 
10 -5 -3 9 

Output: 
---* 
*--* 
**-* 
**-* 
**-* 
**-* 
**-* 
*-** 
*-** 
*-*- 
*--- 
"""
n=int(input())
l=list(map(int,input().split()))
a=[]
s=0
mn=999
mx=-999
for i in range(n):
    s+=l[i]
    a.append(s)
    mx=max(s,mx)
    mn=min(s,mn)
mx=max(abs(mx),abs(mn))
for i in range(mx-1,-1,-1):
    prev=0
    for j in range(n):
        t=l[j]<0
        if prev-t<=i<a[j]-t or a[j]-t<=i<prev-t:
            print('*',end='')
        else:
            print('-',end='')
        prev=a[j]
    print()
