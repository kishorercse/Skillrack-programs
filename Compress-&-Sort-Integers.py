"""
The program must accept N integers as the input. For each integer X among the N integers, the program must compress the integer to a smaller value by removing a digit in X. 
Then the program print the N revised integers in sorted order.

Boundary Condition(s):
1 <= N <= 100
10 <= Each integer value <= 10^6

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains N integers separated by a space representing the N sorted integers.

Example Input/Output 1:
Input:
5
623 234 59296 894 50

Output:
0 23 23 84 5296

Explanation:
After compressing the 5 integers based on the given conditions, the integers become
623 -> 23
234 -> 23
59296 -> 5296
894 -> 84
50 -> 0
After sorting the 5 revised integers, the integers become
0 23 23 84 5296

Example Input/Output 2:
Input:
4
303 45 636 61

Output:
1 3 4 36

Explanation:
After compressing the 4 integers based on the given conditions, the integers become
303 -> 03 -> 3 (as the leading zeroes do not have value)
45 -> 4
636 -> 36
61 -> 1
After sorting the 4 revised integers, the integers become
1 3 4 36
"""
n=int(input())
l=[list(i) for i in input().split()]
for i in range(n):
    mn=1000000000
    for j in range(len(l[i])):
        t=l[i][:]
        t[j]=''
        mn=min(mn,int(''.join(t)))
    l[i]=mn
print(*sorted(l))
