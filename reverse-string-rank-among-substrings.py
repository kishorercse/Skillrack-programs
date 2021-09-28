"""
A string S is passed as the input. The program must generate the set (all unique) of all the substrings of S in the reverse order and then sort that set lexicographically. Now the program must print the rank of the reverse of the string S in the new set formed.

Note:
– String S contains only lowercase English letters.
– Time complexity matters, optimize your algorithm

Boundary Condition(s):
1 <= Length of S <= 100

Input Format:
The first line contains S.

Output Format:
The first line contains the integer value denoting the rank.

Example Input/Output 1:
Input:
eren

Output:
7

Explanation:
Reverse of eren is nere
Lexicograhically sorted set of unique substrings of nere is
e
er
ere
n
ne
ner
nere
r
re

In this nere appears in the 7th position.
"""
s=input().strip()[::-1]
l=len(s)
a=sorted(set([s[i:j] for i in range(l) for j in range(i+1,l+1)]))
print(a.index(s)+1)
