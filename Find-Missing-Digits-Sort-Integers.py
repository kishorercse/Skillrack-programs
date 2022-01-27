"""
The program must accept N integers as the input. Each integer is formed using consecutive digits (increasing or decreasing order) but some digits are missing. The program must
find the missing digits in each integer and find the original integer by inserting the missing digits. If there is no missing digit in an integer, then the program must keep the
integer as it is. Finally, the program must print the N revised integers in sorted order as the output.

Boundary Condition(s):
1 <= N <= 100

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains N integers separated by a space representing the N sorted integers.

Example Input/Output 1:
Input:
6
468 13 25 97 5410 975

Output:
123 987 2345 45678 98765 543210

Explanation:
468 -> 45678
13 -> 123
25 -> 2345
97 -> 987
5410 -> 543210
975 -> 98765
So the 6 revised integers are printed in sorted order.

Example Input/Output 2:
Input:
4
90 9876 567 3210

Output:
567 3210 9876 9876543210
"""
n=int(input())
l=input().split()
for i in range(n):
    a,b=int(l[i][0]),int(l[i][-1])
    d=1 if a<b else -1
    for num in range(a+d,b+d,d):
        a=a*10+num
    l[i]=a
print(*sorted(l))
