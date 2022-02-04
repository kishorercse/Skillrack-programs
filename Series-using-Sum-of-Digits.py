"""
The program must accept two integers N and K as the input. The program must generate a series of integers based on the following conditions.
- The first integer of the series must be N.
- Then each integer from the second integer of the series must be formed by adding the previous integer and the sum of digits in the previous integer.
The program must print the first K integers of the generated series as the output.

Boundary Condition(s):
1 <= N <= 10^5
1 <= K <= 100

Input Format:
The first line contains N and K separated by a space.

Output Format:
The first line contains K integers separated by a space representing the first K integers of the series.

Example Input/Output 1:
Input:
532 5

Output:
532 542 553 566 583

Explanation:
Here N = 532 and K = 5.
1st integer: 532
2nd integer: 542 (532 + (5+3+2))
3rd integer: 553 (542 + (5+4+2))
4th integer: 566 (553 + (5+5+3))
5th integer: 583 (566 + (5+6+6))

Example Input/Output 2:
Input:
80 10

Output:
80 88 104 109 119 130 134 142 149 163
"""
n,k=map(int,input().split())
while k>0:  
    print(n,end=' ')
    for i in str(n):
        n+=int(i)
    k-=1
