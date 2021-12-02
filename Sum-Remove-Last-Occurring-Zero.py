"""
The program must accept N integers as the input. For each integer X among the N integers, the program must remove the last occurring 0 in X. Then the program must print the
sum of those N modified integers as the output.

Boundary Condition(s):
1 <= N <= 100
1 <= Each integer value <= 10^8

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains the sum of those N modified integers.

Example Input/Output 1:
Input:
4
160 875 5000 20111

Output:
3502

Explanation:
After removing the last occurring 0 in 160, the integer becomes 16.
The integer 875 has no zeros. So it remains same.
After removing the last occurring 0 in 5000, the integer becomes 500.
After removing the last occurring 0 in 20111, the integer becomes 2111.
So the sum of those modified values is 3502 (16 + 875 + 500 + 2111).
Hence the output is 3502

Example Input/Output 2:
Input:
8
609 7070 21 308 800 2800 5007 690

Output:
1771
"""
n=int(input())
l=input().split()
s=0
for i in range(n):
    for j in range(len(l[i])-1,-1,-1):
        if l[i][j]=='0':
            l[i]=l[i][:j]+l[i][j+1:]
            break
    s+=int(l[i])
print(s)
