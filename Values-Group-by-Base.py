"""
The program must accept N integers as the input. For each integer X among the N integers, the program must find the least possible base of X. Then the program must group the
integers based on the base value. Finally, the program must print the sum of decimal equivalents of the integers in each group as the output. The sum values must be printed
in sorted order.

Boundary Condition(s):
1 <= N <= 1000
1 <= Each integer value <= 10^8

Input Format:
The first line contains N.
The second line contains N integer values separated by a space.

Output Format:
The first line contains the sum of decimal equivalents of the integers in each group.

Example Input/Output 1:
Input:
6
10111 267 101 215 700 1050

Output:
28 329 631

Explanation:
10111 -> base 2 -> 23
267 -> base 8 -> 183
101 -> base 2 -> 5
215 -> base 6 -> 83
700 -> base 8 -> 448
1050 -> base 6 -> 246
base 2: 23 + 5 = 28.
base 6: 83 + 246 = 329.
base 8: 183 + 448 = 631.
So the sum values are printed in sorted order.

Example Input/Output 2:
Input:
7
22 10000 10 111 19 12 1010

Output:
13 19 35

Explanation:
22 -> base 3 -> 8
10000 -> base 2 -> 16
10 -> base 2 -> 2
111 -> base 2 -> 7
19 -> base 10 -> 19
12 -> base 3 -> 5
1010 -> base 2 -> 10
base 2: 16 + 2 + 7 + 10 = 35
base 3: 8 + 5 = 13
base 10: 19
So the sum values are printed in sorted order.
""
n=int(input())
l=input().split()
ans=[0]*11
for i in l:
    base=int(max(i))+1
    ans[base]+=int(i,base)
ans.sort()
for i in ans:
    if i!=0:
        print(i,end=' ')
