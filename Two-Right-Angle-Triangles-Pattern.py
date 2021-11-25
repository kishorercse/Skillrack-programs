"""
The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s):
2 <= N <= 50

Input Format:
The first line contains N.

Output Format:
The first N lines contain the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
Input:
3

Output:
----*
--*-*-*
*-*-*-*-*

Explanation:
Here N=3, so the pattern contains 3 lines of output.
The asterisks in the pattern represent the two right-angle triangles and the hyphens in the pattern represent the empty spaces.

Example Input/Output 2:
Input:
5

Output:
--------*
------*-*-*
----*---*---*
--*-----*-----*
*-*-*-*-*-*-*-*-*

Example Input/Output 3:
Input:
6

Output:
----------*
--------*-*-*
------*---*---*
----*-----*-----*
--*-------*-------*
*-*-*-*-*-*-*-*-*-*-*
"""
n=int(input())
hyphen='-'*(n*2-2)
print(hyphen,'*',sep='')
hyphen=hyphen[2:]
centre_hyphen='-'
while hyphen:
    print(hyphen,'*',centre_hyphen,'*',centre_hyphen,'*',sep='')
    hyphen=hyphen[2:]
    centre_hyphen+='--'
print('*','-*'*(n*2-2),sep='')
