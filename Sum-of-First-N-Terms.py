"""
The program must accept an integer N as the input. The program must print the sum of the first N terms in the following series.
1 1 2 1 2 3 1 2 3 4 1 2 3 4 5 1 2 3 4 5 6 1 2 3 4 5 6 7 ... and so on.
The above series contains the integers 1, 1 to 2, 1 to 3, 1 to 4, 1 to 5, 1 to 6, ... and so on.

Boundary Condition(s):
1 <= N <= 10^6

Input Format:
The first line contains N.

Output Format:
The first line contains an integer representing the sum of the first N terms in the above-mentioned series.

Example Input/Output 1:
Input:
7

Output:
11

Explanation:
The first 7 terms are 1 1 2 1 2 3 1.
So their sum is 11 (1+1+2+1+2+3+1).

Example Input/Output 2:
Input:
10

Output:
20
"""
n=int(input())
Sum=0
k=1
i=1
while i<=n:
    if (n-i+1<k):
        t=n-i+1
        Sum+=t*(t+1)//2
    else:
        Sum+=k*(k+1)//2
    i+=k
    k+=1
print(Sum)
