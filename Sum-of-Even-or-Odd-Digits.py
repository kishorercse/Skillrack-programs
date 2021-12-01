"""
The program must accept N integers as the input. For each integer X among the N integers, the program must print the output based on the following conditions.
- If X is even, the program must print the value of X + (Sum of all the even digits in the remaining integers).
- If X is odd, the program must print the value of X + (Sum of all the odd digits in the remaining integers).

Boundary Condition(s):
2 <= N <= 1000
1 <= Each integer value <= 10^4

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains the N integer values separated by a space.

Example Input/Output 1:
Input:
4
32 25 16 71

Output:
40 37 20 80

Explanation:
The first integer 32 is an even integer, so the sum is 40 (32 + 2+6).
The second integer 25 is an odd integer, so the sum is 37 (25 + 3+1+7+1).
The third integer 16 is an even integer, so the sum is 20 (16 + 2+2).
The fourth integer 71 is an odd integer, so the sum is 80 (71 + 3+5+1).
Hence the output is 40 37 20 80

Example Input/Output 2:
Input:
3
234 46 1897

Output:
252 60 1900
"""
n=int(input())
l=input().split()
evenSum=[0]*n
oddSum=[0]*n
totalOddSum=totalEvenSum=0
for i in range(n):
    for ch in l[i]:
        if ch in "24680":
            evenSum[i]+=int(ch)
        else:
            oddSum[i]+=int(ch)
    totalEvenSum+=evenSum[i]
    totalOddSum+=oddSum[i]
for i in range(n):
    l[i]=int(l[i])
    if l[i]%2==0:
        print(l[i]+totalEvenSum-evenSum[i],end=' ')
    else:
        print(l[i]+totalOddSum-oddSum[i],end=' ')
