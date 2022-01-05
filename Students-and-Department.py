"""
Given N students name and department, print the X students belonging to a specific department D.

Boundary Condition(s):
1 <= N <= 100
Length of student name is from 3 to 100
Length of department name is from 3 to 20

Input Format:
The first line contains the values of N.
N lines contain the name and department of N students separated by a space.
The next line (N+2)th line, will contain the department name D for which the students list is to be printed.

Output Format:
X lines containing students name where X is the number of students belonging to department D.

Example Input/Output 1:
Input:
5
Arun CSE
Bhuvana ECE
Ganesh MECH
Pavithra ECE
Rohit CSE
ECE

Output:
Bhuvana
Pavithra
"""
n=int(input())
dt={}
for _ in range(n):
    s,d=input().split()
    dt[d]=dt.get(d,[])+[s]
print(*dt[input().strip()],sep='\n')
