"""
The program must accept three string values S1, S2 and S3 of equal length as the input. All three string values contain only nonzero digits. In the given three string values, 
the sum of the digits that occur in the same position is always equal to 9. For each digit D1, D2 and D3 of the three string values, the program must print D1 asterisks,
D2 hyphens and D3 asterisks vertically as shown in the Example Input/Output section.

Boundary Condition(s):
1 <= Length of S1, S2, S3 <= 100

Input Format:
The first line contains S1.
The second line contains S2.
The third line contains S3.

Output Format:
The first nine lines contain the asterisks and hyphens based on the given conditions.

Example Input/Output 1:
Input:
2134
5212
2653

Output:
****
*-**
--**
-*-*
-**-
-**-
-***
****
****

Explanation:
Here S1=2134, S2=5212, S3=2653.
The first digit in the three string values are 2, 5 and 2. So 2 asterisks, 5 hyphens and 2 asterisks are printed vertically in the first column.
The second digit in the three string values are 1, 2 and 6. So 1 asterisk, 2 hyphens and 6 asterisks are printed vertically in the second column.
The third digit in the three string values are 3, 1 and 5. So 3 asterisks, 1 hyphen and 5 asterisks are printed vertically in the third column.
The fourth digit in the three string values are 4, 2 and 3. So 4 asterisks, 2 hyphens and 3 asterisks are printed vertically in the fourth column.

Example Input/Output 2:
Input:
1234567
7654321
1111111

Output:
*******
-******
--*****
---****
----***
-----**
------*
-------
*******
"""
a=input().strip()
b=input().strip()
c=input().strip()
l=len(a)
for i in range(9):
    for j in range(l):
        x=int(a[j])
        y=x+int(b[j])
        z=y+int(c[j])
        if i<x:
            print('*',end='')
        elif i<y:
            print('-',end='')
        else:
            print('*',end='')
    print()
