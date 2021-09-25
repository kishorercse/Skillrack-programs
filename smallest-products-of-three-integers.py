"""
The program must accept N integers as the input. The program must print the smallest value obtained by the multiplying three integers among the N integers as the output.

Boundary Condition(s):
3 <= N <= 1000
-1000 <= Each integer value <= 1000

Input Format:
The first line contains N.
The second line contains N integers separated by space.

Output Format:
The first line contains the smallest product value of three integers.

Example Input/Output 1:
Input:
5
-5 3 12 5 7

Output:
-420

Explanation:
The smallest integer obtained by multiplying 3 integers -5, 12 and 7 is -420.

Example Input/Output 2:
Input:
8
12 45 78 22 16 2 14 23

Output:
336
"""
n=int(input())
l=sorted(map(int,input().split()))
print(min(l[0]*l[1]*l[2],l[-1]*l[-2]*l[-3],l[0]*l[-1]*l[-2],l[-1]*l[0]*l[1]))
