"""
A positive integer N is passed as the input. The program must print the number of 1s in the binary representation of N.

Input Format:
First line contains N.

Output Format:
First line contains the count of 1s in the binary representation of N.

Boundary Conditions:
1 <= N <= 9000000000000000000   

Example Input/Output 1:
Input:
22

Output:
3

Explanation:
The binary representation of 22 is 10110. There are three 1s in it.
"""
n=int(input())
count=0
while n>0:
    count+=n&1
    n>>=1
print(count)
