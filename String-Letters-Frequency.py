"""
A string value S containing N unique letters is passed as the input. The program must print the letters in the string based on the count of their occurrence. The letters of higher frequency of occurrence must appear first. If two letters have same frequency of occurrence then they are arranged as per alphabetical order.

Input Format:
The first line contains S.

Output Format:
N lines containing letters based on their frequency of occurrence.

Boundary Conditions:
2 <= LENGTH(S) <= 10000

Example Input/Output 1:
Input:
MANAGEMENT

Output:
A2
E2
M2
N2
G1
T1

Example Input/Output 2:
Input:
ArrangemENt

Output:
r2
A1
E1
N1
a1
e1
g1
m1
n1
t1
"""
s=input().strip()
count={}
for i in s:
    count[i]=count.get(i,0)+1
count=sorted(count.items(),key=lambda x:(-x[1],x[0]))
for i in count:
    print(*i,sep='')
