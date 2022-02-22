"""
The program must accept N integers as the input. For each integer X among the N integers, the program must form two integers by dividing the binary representation of X into two
equal halves. If the number of bits in the binary representation of X is odd, then consider the middle bit for both halves. Finally, the program must print the resulting N*2 
integers in sorted order.

Boundary Condition(s):
1 <= N <= 100
1 <= Each integer value <= 10^8

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains the resulting N*2 integers in sorted order separated by a space.

Example Input/Output 1:
Input:
4
14 23 10 51

Output:
2 2 2 3 3 5 6 7

Explanation:
14 -> 1110 -> 11, 10 -> 3, 2
23 -> 10111 -> 101, 111 -> 5, 7
10 -> 1010 -> 10, 10 -> 2, 2
51 -> 110011 -> 110, 011 -> 6, 3
So the 8 integers are printed in sorted order.

Example Input/Output 2:
Input:
5
34 2 69 51 30

Output:
0 1 2 3 4 5 6 6 7 8
"""
n=int(input())
l=list(map(int,input().split()))
res=[]
for i in l:
    b=bin(i)[2:]
    s=len(b)
    res.append(int(b[:s//2+s%2],2))
    res.append(int(b[s//2:],2))
print(*sorted(res))
