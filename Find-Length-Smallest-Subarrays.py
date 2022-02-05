"""
The program must accept two arrays A and B of equal size N as the input. For every index i in the array A, the program must print the length of the smallest subarray starting
from the index i such that the subarray contains at least B[i] integers greater than or equal to A[i]. If there is no such subarray starting from the index i, the program must
print -1.

Boundary Condition(s):
2 <= N <= 100
1 <= Each integer value <= 10^5

Input Format:
The first line contains N.
The second line contains N integers separated by a space representing the array A.
The third line contains N integers separated by a space representing the array B.

Output Format:
The first line contains N integer values separated by a space.

Example Input/Output 1:
Input:
5
9 2 5 2 10
2 3 6 1 1

Output:
5 3 -1 1 1

Explanation:
For i = 0, the smallest subarray is [9, 2, 5, 2, 10] -> Length = 5.
For i = 1, the smallest subarray is [2, 5, 2] -> Length = 3.
For i = 2, there is no such smallest subarray -> So -1 is printed.
For i = 3, the smallest subarray is [2] -> Length = 1.
For i = 4, the smallest subarray is [10] -> Length = 1.

Example Input/Output 2:
Input:
6
39 53 13 11 11 84
2 1 3 3 2 2

Output:
2 1 -1 3 2 -1
"""
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(n):
    for j in range(i,n):
        if a[j]>=a[i]:
            b[i]-=1
            if b[i]==0:
                print(j-i+1,end=' ')
                break
    else:
        print(-1,end=' ')
