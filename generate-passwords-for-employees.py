"""
There are N employees working in a company. The N employees are numbered from 1 to N. Every day, each employee
must use a password to enter into the office. The passwords of the employees are generated based on the fallowing
conditions.
- The password of Kth employee on the 1st day = C+K, where C is a numeric value representin the company's code.
- The password of Kth employee on the 2nd day = Password[day1] of Kth employee + C + 1.
- The password of Kth employee on the 3rd day = Password[day2] of Kth employee + C + 2.
- The password of Kth employee on the 4th day = Password[day3] of Kth employee + C + 3.
- Similarly, the passwords are generated for the remaining days.
The program must accept the values of N and C as the input. The program must print the passwords of the N employees
on each day from 1 to D as the output. The value of D is also passed as the input.

Boundary Condition(s):
1 <= N <= 1000 
1 <= C <= 10^5 
1 <= D <= 100

Input Format: 
The first line contains N. 
The second line contains C. 
The third line contains D. 

Output Format: 
The first D lines, each contains N integers separated by a space representing the passwords of the N employees. 
Example Input/Output 1: 
Input:
10 
500 
3
 
Output: 
501 502 503 504 505 506 507 508 509 510 
1002 1003 1004 1005 1006 1007 1008 1009 1010 1011 
1504 1505 1506 1507 1508 1509 1510 1511 1512 1513 

Explanation: 
Here N = 10, C = 500 and D = 3.
Passwords of the 10 employees on day 1: 501 502 503 504 505 506 507 508 509 510 
Passwords of the 10 employees on day 2: 1002 1003 1004 1005 1006 1007 1008 1009 1010 1011 
Passwords of the 10 employees on day 3: 1504 1505 1506 1507 1508 1509 1510 1511 1512 1513 

Example Input/Output 2: 
Input: 
7
120
6 

Output: 
121 122 123 124 125 126 127 
242 243 244 245 246 247 248 
364 365 366 367 368 369 370 
487 488 489 490 491 492 493 
611 612 613 614 615 616 617 
736 737 738 739 740 741 742
"""
n=int(input())
c=int(input())
d=int(input())
l=[]
for k in range(1,n+1):
    t=c+k
    print(t,end=' ')
    l.append(t)
print()
for i in range(1,d):
    for k in range(1,n+1):
        l[k-1]=l[k-1]+c+i
        print(l[k-1],end=' ')
    print()
