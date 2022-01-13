"""
Given a string S of length L, the program must print the pattern as described in the Example Input/Output.

Input Format:
First line contains the string S.

Output Format:
L lines containing the desired pattern.

Boundary Condition:
2 <= L <= 100

Example Input/Output 1:
Input:
ABCD

Ouput:
A
BB
CCC
DDDD

Example Input/Output 2:
Input:
EAGLE

Ouput:
E
AA
GGG
LLLL
EEEEE
"""
s=input().strip()
l=len(s)
for i in range(l):
    print(s[i]*(i+1))
