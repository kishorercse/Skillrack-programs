"""
String S is passed as the input to the program. S will have positive numbers in it along with other characters. The program must print the sum of all numbers embedded in the 
string.

Input Format:
The first line contains S

Output Format:
The first line contains the sum of all numbers in S.

Boundary Conditions:
5 <= Length of S <= 1000


Example Input/Output 1:
Input:
kilo100gram555dhal900

Output:
1555

Example Input/Output 2:
Input:
65rich100guys70went100to22park

Output:
357
"""
s=input().strip()
n=''
total=0
for i in s:
    if i.isnumeric():
        n+=i
    else:
        if n:
            total+=int(n)
            n=''
if n:
    total+=int(n)
print(total)
