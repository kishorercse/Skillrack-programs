"""
The program must accept an integer N as the input. The program must print YES if it is possible to split the integer N into two parts (left part L and right part R) based on
the following condition.
- The sum of the integers from L to R or R to L must be equal to N.
If it is not possible to split the integer N with the given condition, the program must print NO as the output.
Note: The leading zeroes in the right part of N are not considered.

Boundary Condition(s):
10 <= N <= 10^7

Input Format:
The first line contains N.

Output Format:
The first line contains YES or NO.

Example Input/Output 1:
Input:
27

Output:
YES

Explanation:
There is only one possible partition.
2 and 7
2 + 3 + 4 + 5 + 6 + 7 = 27
So YES is printed as the output.

Example Input/Output 2:
Input:
20328

Output:
YES

Explanation:
There are 4 possible partitions.
2 and 0328 -> sum = (2 + 3 + ... + 327 + 328) = 53955
20 and 328 -> sum = (20 + 21 + ... + 327 + 328) = 53766
203 and 28 -> sum = (28 + 29 + ... + 202 + 203) = 20328
2032 and 8 -> sum = (8 + 9 + ... + 2031 + 2032) = 2065500
The partition 203 and 28 gives the sum as 20328.
So YES is printed as the output.

Example Input/Output 3:
Input:
1020

Output:
NO

Explanation:
There are 3 possible partitions.
1 and 020 -> sum = (1 + 2 + ... + 19 + 20) = 210
10 and 20 -> sum = (10 + 11 + ... + 19 + 20) = 165
102 and 0 -> sum = (0 + 1 + ... + 101 + 102) = 5253
All possible partitions are invalid.
So NO is printed as the output.
"""
num=input().strip()
temp=int(num)
l=len(num)
for i in range(1,l):
    x=int(num[:i])
    y=int(num[i:])
    a=min(x,y)
    b=max(x,y)
    n=b-a+1
    s=n*(2*a+(n-1))//2
    if s==temp:
        print("YES")
        break
else:
    print("NO")
