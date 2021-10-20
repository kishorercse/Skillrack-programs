"""
SHARE
Given a sequence of distinct numbers a1, a2, …. an, an inversion occurs if there are indices i < j such that ai > aj.

For example, in the sequence 2 1 4 3 there are 2 inversions (2 1) and (4 3).

The input will be a main sequence of N positive integers. From this sequence, a Derived sequence will be obtained using the following rule. The output is the number of inversions in the derived sequence.

Rule for forming the derived sequence:

The derived sequence is formed by the sum of digits in the base 6 representation of the corresponding number in the input sequence.

Thus for the number 1409, the base 6 representation is 10305, and the sum of digits is 1+0+3+0+5 = 9. The sum of digits may be done in the decimal system, and does not need to be in base 6.

Boundary Condition(s):
2 <= N <= 100
1 <= Each integer value <= 10^7

Input Format:
The first line contains N.
The second line contains N integers separated by a comma.

Output Format:
The first line contains the number of inversions in the derived sequence formed from the main sequence.

Example Input/Output 1:
Input:
5
62,85,44,21,36

Output:
8

Explanation:
The given sequence is 62,85,44,21,36.
The base 6 representations of the integers in the above sequence are 142, 221, 112, 33 and 100.
The derived sequence is 7, 5, 4, 6 and 1 (corresponding to the sum of digits in the base 6 representation).
The number of inversions in the above derived sequence is 8 and they are given below.
(7, 5), (7, 4), (7, 6), (7, 1), (5, 4), (5, 1), (4, 1) and (6, 1).

Example Input/Output 2:
Input:
8
39,46,999,22,19,136,91,81

Output:
11

Explanation:
The given sequence is 39,46,999,22,19,136,91,81.
The base 6 representations of the integers in the above sequence are 103, 114, 4343, 34, 31, 344, 231 and 213.
The derived sequence is 4, 6, 14, 7, 4, 11, 6 and 6 (corresponding to the sum of digits in the base 6 representation).
The number of inversions in the above derived sequence is 11 and they are given below.
(6, 4), (14, 7), (14, 4), (14, 11), (14, 6), (14, 6), (7, 4), (7, 6), (7, 6), (11, 6) and (11, 6).
"""
def base6sum(n):
    s=0
    while n>0:
        s+=n%6
        n//=6
    return s
n=int(input())
l=[base6sum(int(i)) for i in input().split(',')]
count=0
for i in range(n):
    for j in range(i+1,n):
        if l[i]>l[j]:
            count+=1
print(count)
