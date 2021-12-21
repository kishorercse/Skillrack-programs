"""
The program must accept N integers and an integer K as the input. The program must sort the N integers in ascending order based on the decimal equivalent of the last K bits. 
If two or more integers have the same last K bits, then the program must sort those integers in ascending order.

Boundary Condition(s):
2 <= N <= 100
1 <= Each integer value <= 10^9
1 <= K <= 30

Input Format:
The first line contains N.
The second line contains N integers separated by a space.
The third line contains K.

Output Format:
The first line contains N integers separated by a space.

Example Input/Output 1:
Input:
7
10 4 15 8 2 3 9
2

Output:
4 8 9 2 10 3 15

Explanation:
10 -> 1010
4 -> 0100
15 -> 1111
8 -> 1000
2 -> 0010
3 -> 0011
9 -> 1001
After sorting the 7 integers based on the decimal equivalent of the last 2 bits, the integers become
4 8 9 2 10 3 15

Example Input/Output 2:
Input:
8
61 36 45 80 31 53 16 75
3

Output:
16 80 75 36 45 53 61 31

Explanation:
61 -> 0111101
36 -> 0100100
45 -> 0101101
80 -> 1010000
31 -> 0011111
53 -> 0110101
16 -> 0010000
75 -> 1001011
After sorting the 8 integers based on the decimal equivalent of the last 3 bits, the integers become
16 80 75 36 45 53 61 31
"""
n=int(input())
l=list(map(int,input().split()))
k=int(input())
l.sort(key=lambda x:(int(bin(x)[2:][-k:]),x))
print(*l)
