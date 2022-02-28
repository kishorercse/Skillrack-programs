"""
The program must accept a string S containing multiple words as the input. Each word contains an integer value (i.e., An integer value is embedded in the word). The program 
must sort the words based on the embedded integer values. If two or more words have the same integer, then those words must be sorted in the order of their occurrence.

Boundary Condition(s):
2 <= Length of S <= 1000

Input Format:
The first line contains S.

Output Format:
The first line contains the words separated by a space based on the given conditions.

Example Input/Output 1:
Input:
li55on t70iger 66goat h70en deer40

Output:
deer40 li55on 66goat t70iger h70en

Explanation:
There are 5 words in the given string.
li55on = lion and 55
t70iger  = tiger and 70
66goat = goat and 66
h70en = hen and 70
deer40 = deer and 40
After sorting the words based on the embedded integer values, the words become
deer40 li55on 66goat t70iger h70en

Example Input/Output 2:
Input:
key512board m512ouse wi510re monitor512 lapt512op

Output:
wi510re key512board m512ouse monitor512 lapt512op
"""
from re import findall
arr=input().split()
d={}
for s in arr:
    d[s]=int(''.join(findall('\d+',s)))
arr.sort(key=lambda x:d[x])
print(*arr)
