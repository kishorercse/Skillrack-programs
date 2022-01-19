"""
The program must accept N string values as the input. The given N string values are aligned vertically or horizontally as shown in the Example Input/Output section. The empty
spaces at the end of each string are denoted as asterisks. The program must change the alignment (vertical to horizontal or horizontal to vertical) of the given N string values
and print them as the output.

Note: At least one string value is always longer than N.

Boundary Condition(s):
3 <= N <= 50
1 <= Length of each string <= 100

Input Format:
The first line contains N.
The next lines contain the N string values vertically or horizontally.

Output Format:
The lines contain the N string values vertically or horizontally.

Example Input/Output 1:
Input:
4
book**
pencil
car***
cycle*

Output:
bpcc
oeay
onrc
kc*l
*i*e
*l**

Explanation:
Here N = 4 and the string values are aligned horizontally.
So they are printed vertically.

Example Input/Output 2:
Input:
4
bpcc
oeay
onrc
kc*l
*i*e
*l**

Output:
book**
pencil
car***
cycle*

Explanation:
Here N = 4 and the string values are aligned vertically.
So they are printed horizontally.
"""
n=int(input())
l=[]
while True:
    try:
        l.append(input().strip())
    except EOFError:
        break
for j in range(len(l[0])):
    for i in range(len(l)):
        print(l[i][j],end='')
    print()
