"""
The program must accept N hexadecimal values as the input. For each hexadecimal value H, the program must replace each alphabet with the corresponding decimal value in H. Then 
the program must print the sum of the N revised values by considering them as decimal values.

Boundary Condition(s):
1 <= N <= 100
1 <= Decimal equivalent of H <= 10^6

Input Format:
The first line contains N.
The second line contains N hexadecimal values separated by a space.

Output Format:
The first line contains an integer representing the sum of the N revised values based on the given conditions.

Example Input/Output 1:
Input:
4
5FA 34B C10 529

Output:
56660

Explanation:
5FA -> 51510
34B -> 3411
C10 -> 1210
529 -> 529
51510 + 3411 + 1210 + 529 = 56660.

Example Input/Output 2:
Input:
3
ABCD 1234 EF

Output:
10113862

Explanation:
ABCD -> 10111213
1234 -> 1234
EF -> 1415
10111213 + 1234 + 1415 = 10113862.
"""
n=int(input())
res=0
l=input().split()
for s in l:
    num=0
    for ch in s:
        if ch.isdigit():
            num=num*10+int(ch)
        else:
            num=num*100+(ord(ch)-55)
    res+=num
print(res)
