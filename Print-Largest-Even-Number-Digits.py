"""
Given a number N as the input, print the largest even number E that can be formed using the digits present in the number. (There will be at least one even digit).

Input Format:
The first line contains N.

Output Format:
The first line contains E.

Example Input/Output 1:
Input:
1902

Output:
9210
"""
n=list(input().strip())
mn=9
for i in n:
    t=int(i)
    if t%2==0:
        mn=min(t,mn)
        if mn==0:
            break
mn=str(mn)
n.remove(mn)
print(''.join(sorted(n,reverse=True)+[mn]))
