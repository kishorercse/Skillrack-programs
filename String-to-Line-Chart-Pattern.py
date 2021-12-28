"""
The program must accept a string S containing only alphabets as the input. The string S always starts with a consonant. The program must print the string like a line chart as
shown in the Example Input/Output section. The line in the chart always increases till the 1st vowel. Then the line decreases till the 2nd vowel. Then the line increases till
the 3rd vowel. Then the line decreases till the 4th vowel, and so on. The empty spaces before each character must be printed as hyphens.

Boundary Condition(s):
2 <= Length of S <= 100

Input Format:
The first line contains S.

Output Format:
The lines contain the string like a line chart as shown in the Example Input/Output section.

Example Input/Output 1:
Input:
skillrack

Output:
--i
-k-l
s---l---k
-----r-c
------a

Explanation:
Here S = "skillrack".
The first occuring vowel is 'i', so the characters till 'i' are printed in increasing order.
The second occuring vowel is 'a', so the characters till 'a' are printed in decreasing order.
No more vowels left in the given string, so the remaining characters are printed in increasing order.

Example Input/Output 2:
Input:
pineapple

Output:
-i
p-n-a
---e-p
------p
-------l
--------e

Example Input/Output 3:
Input:
NOTEBOOKS

Output:
--------S
-O---O-K
N-T-B-O
---E
"""
s=input().strip()
m=[]
rows=0
diff=-1
ind=0
chars=0
for i in s:
    if ind==rows:
        m.append('-'*chars+i)
        rows+=1
    elif ind==-1:
        m.insert(0,'-'*chars+i)
        ind=0
        rows+=1
    else:
        m[ind]+='-'*(chars-len(m[ind]))+i
    if i in "AEIOUaeiou":
        diff*=-1
    ind+=diff
    chars+=1
for i in m:
    print(*i,sep='')
