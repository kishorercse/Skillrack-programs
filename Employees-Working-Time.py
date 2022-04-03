"""
The program must accept the name, in-time and out-time (in 24-hr format HH:MM) of N employees as the input. The program must print the names of the employees in 
descending order based on their working time. If two or more employees have the same working time then those employees must be printed in chronological order based 
on their in-time. If two or more employees have the same working time and the same in-time then those employees must be printed in sorted order based on their names.

Boundary Condition(s):
1 <= N <= 50
1 <= Length of each employee's name <= 10

Input Format:
The first line contains N.
The next N lines, each contains the name, in-time and out-time of an employee separated by a space.

Output Format:
The first N lines contain the names of the N employees based on the given conditions.

Example Input/Output 1:
Input:
7
Rajesh 08:45 16:45
Catherine 09:15 17:45
Deepa 08:00 18:00
Pravin 09:00 17:30
Jhanvi 08:45 16:45
Hector 09:00 18:00
Mambo 09:00 17:00

Output:
Deepa
Hector
Pravin
Catherine
Jhanvi
Rajesh
Mambo

Explanation:
Here N=7, the name, in-time and out-time of 7 employees are given below.
Rajesh 08:45 16:45
Catherine 09:15 17:45
Deepa 08:00 18:00
Pravin 09:00 17:30
Jhanvi 08:45 16:45
Hector 09:00 18:00
Mambo 09:00 17:00
After sorting the names of the employees based on the given conditions, the names of the employees become
Deepa
Hector
Pravin
Catherine
Jhanvi
Rajesh
Mambo

Example Input/Output 2:
Input:
6
Bhuvana 16:00 23:00
Anu 11:00 23:00
Hector 09:30 16:30
John 10:15 20:15
Ramesh 09:30 16:29
Anita 09:30 16:30

Output:
Anu
John
Anita
Hector
Bhuvana
Ramesh
"""
n=int(input())
l=[]
for _ in range(n):
    name,s,e=input().split()
    h,m=map(int,s.split(':'))
    s=h*60+m
    h,m=map(int,e.split(':'))
    e=h*60+m
    l.append([name,s,e-s])
l.sort(key=lambda x:(-x[-1],x[-2],x[-3]))
for i in l:
    print(i[0])
