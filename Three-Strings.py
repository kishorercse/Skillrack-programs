"""
Given N string values, the program must print 3 string values as the output as described in the Example Input/Output section.

Input format:
The first line will contain N denoting the number of string values.
Next N lines will contain the N string values.

Output format:
Three lines containing string values as described in the Example Input/Output section.

Example Input/Output 1:
Input:
3
JOHN
JOHNY
JANARDHAN

Output:
JJOJAN
OHHARD
NNYHAN

Example Input/Output 2:
Input:
4
JOHN
JOHNY
JANARDHAN
MIKESPENCER

Output:
JJOJANMIKE
OHHARDSPE
NNYHANNCER
"""
n=int(input())
l=[input().strip() for _ in range(n)]
a=b=c=""
for i in range(n):
    a+=l[i][:i+1]
    c+=l[i][-(i+1):]
    b+=l[i][i+1:-(i+1)]
print(a,b,c,sep='\n')
