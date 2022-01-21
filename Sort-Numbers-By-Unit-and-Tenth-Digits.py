"""
Given N positive integers, the program must sort the numbers based on their unit digits (Smaller to larger). If the unit digits are same, then consider tenth digit to sort.
Assume no two numbers will have both unit and tenth digits equal.

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains the sorted integers separated by a space.

Boundary Conditions:
1 <= N <= 100

Example Input/Output 1:
Input:
9
12 223 10 4345 189 9 455 61 82

Output:
10 61 12 82 223 4345 455 9 189
"""
n=int(input())
print(*sorted(map(int,input().split()),key=lambda x:(x%10,x/10%10)))
