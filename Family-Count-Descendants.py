"""
The program must accept the first and last names of N persons in a family. The last name of each person indicates the name of his/her father. The program must print the number 
of persons(descendants) belonging to the given person's family.

Boundary Condition(s):
1 <= N <= 50
2 <= Length of each name <= 20

Input Format:
The first line contains N.
The next N lines contain the first and last names of N persons in a family.
The N+2nd line contains a person name.

Output Format:
The first line contains the number of persons(descendants) belonging to the given person's family.

Example Input/Output 1:
Input:
6
Arun Babloo
Gavin Babloo
Rajesh Arun
Hector Arun
Oliver Hector
Kavin Gavin
Arun

Output:
4

Explanation:
Arun is the father of both Rajesh and Hector.
Hector is the father of Oliver.
So there are 4 persons in the Arun's family.

Example Input/Output 2:
Input:
12
Catherine John
Rajesh Babloo
Pravin Babloo
Kavin Pravin
Deepa Rajesh
Hector John
Bhuvana Pravin
Arun Kavin
Anu Deepa
Anita Kavin
Jhanvi Bhuvana
Mambo Hector
Pravin

Output:
6
"""
count=1
def family(l):
    for i in l:
        if i in d:
            global count
            count+=len(d[i])
            family(d[i])
            del d[i]
n=int(input())
d={}
for _ in range(n):
    a,b=input().split()
    try:
        d[b].append(a)
    except KeyError:
        d[b]=[a]
family([input().strip()])
print(count)
