"""
The program must accept values for two positive integer arrays of size N. The program must print the minimum sum S possible when a value in the first array is multiplied with
a value in the second array. If a value is already used for multiplication then the value cannot be used again.

Boundary Condition(s):
1 <= N <= 100
1 <= Each integer value in array <= 100

Input Format:
The first line contains N.
The second line contains N positive integer values separated by a space.
The third line contains N positive integer values separated by a space.

Output Format:
The first line contains S.

Example Input/Output 1:
Input:
3
5 6 10
8 15 9

Output:
209

Explanation:
The minimum sum is obtained for 10*8+6*9+5*15

Example Input/Output 2:
Input:
5
2 55 10 8 20
5 40 60 2 15

Output:
800
"""
n=int(input())
a=sorted(map(int,input().split()))
b=sorted(map(int,input().split()),reverse=True)
s=0
for i in range(n):
    s+=a[i]*b[i]
print(s)
