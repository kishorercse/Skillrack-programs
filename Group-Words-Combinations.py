"""
The program must accept a string S containing multiple words as the input. The program must group the words where each word is a combination of the other words. 
Then the program must print the groups of words in separate lines in the order of their occurrence.

Boundary Condition(s):
3 <= Length of S <= 1000

Input Format:
The first line contains S.

Output Format:
The lines contain the groups of words separated by a space based on the given conditions.

Example Input/Output 1:
Input:
neon nose ones race none noes care

Output:
neon none
nose ones noes
race care

Explanation:
Here S = "neon nose ones race none noes care".
1st group: neon none
2nd group: nose ones noes
3rd group: race care
In each group, each word is a combination of the other words in the group.
Hence the output is
neon none
nose ones noes
race care

Example Input/Output 2:
Input:
seven oil evens lio smart loi skill

Output:
seven evens
oil lio loi
smart
skill
"""
from collections import Counter
s=input().split()
n=len(s)
for i in range(n):
    flag=False
    if s[i]!=-1:
        print(s[i],end=' ')
        c=Counter(s[i])
        for j in range(i+1,n):
            if s[j]!=-1 and c==Counter(s[j]):
                print(s[j],end=' ')
                s[j]=-1
        print()
