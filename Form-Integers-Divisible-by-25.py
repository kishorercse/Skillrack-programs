"""
The program must accept a string S representing a number. The string S contains digits, underscores and X's. The program must print the number of possible integers that can be
formed from the string S based on the following conditions.
- All the underscores must be replaced with the digits.
- All X's must be replaced with a same digit.
- The integer must be divisible by 25 and does not contain any leading zeroes.

Boundary Condition(s):
1 <= Length of S <= 7

Input Format:
The first line contains S.

Output Format:
The first line contains an integer value representing the number of possible integers that can be formed from the string S.

Example Input/Output 1:
Input:
8_XX

Output:
10

Explanation:
Here the given string is 8_XX.
The 10 possible integers are given below.
8000
8100
8200
8300
8400
8500
8600
8700
8800
8900

Example Input/Output 2:
Input:
_25

Output:
9

Example Input/Output 3:
Input:
0_75

Output:
0

Explanation:
Here the given string is 0_75.
There is no way to form such integers as the given string starts with 0.

Example Input/Output 4:
Input:
0

Output:
1

Explanation:
Here the given string is 0.
The only integer that can be formed is 0 which is divisible by 25.
"""
def form_integers(s,x,num):
    if s=='':
        if int(num)%25==0 and len(str(int(num)))==l:
            global count
            count+=1
        return
    if s[0]=='X':
        form_integers(s[1:],x,num+x)
    elif s[0]=='_':
        for i in range(10):
            form_integers(s[1:],x,num+str(i))
    else:
        form_integers(s[1:],x,num+s[0])
s=input().strip()
if s=='0':
    print(1)
    exit()
l=len(s)
count=0
if s[0]!='0':
    if 'X' in s:
        for i in range(10):
            form_integers(s,str(i),'')
    else:
        form_integers(s,'','')
print(count)
