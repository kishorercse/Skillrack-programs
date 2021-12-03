"""
The program must accept three string values S1, S2 and S3 containing only lower case alphabets as the input. The program must print the desired pattern as shown in the
Example Input/Output section.
Note:
 There is only one possible way to rearrange the three string values for the N pattern.
 The length of S1, S2 and S3 are always equal.

Boundary Condition(s):
3 <= Length of S1, S2, S3 <= 100

Input Format:
The first line contains S1, S2 and S3 separated by a space.

Output Format:
The lines contain the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
Input:
hello order range

Output:
o***e
lr**g
l*d*n
e**ea
h***r

Example Input/Output 2:
Input:
google amazon errata

Output:
e****n
lr***o
g*r**z
o**a*a
o***tm
g****a
"""
a,b,c=input().split()
l=len(a)
if c[0]==a[-1] and c[-1]==b[0]:
    b,c=c,b
elif c[0]==b[-1] and c[-1]==a[0]:
    a,b,c=b,c,a
elif b[0]==c[-1] and b[-1]==a[0]:
    a,c=c,a
elif a[0]==b[-1] and a[-1]==c[0]:
    a,b=b,a
elif a[0]==c[-1] and a[-1]==b[0]:
    a,b,c=c,a,b
for i in range(l):
    print(a[-i-1],end='')
    for j in range(1,l-1):
        if i==j:
            print(b[j],end='')
        else:
            print('*',end='')
    print(c[-i-1])
