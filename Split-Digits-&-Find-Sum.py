"""
The program must accept two string values S1 and S2 as the input. The string S1 contains only digits. The string S2 contains a series of nonzero digits enclosed within
parentheses. The length of S1 is always equal to the sum of digits in the string S2 by ignoring the sign of digits. The program must form integer values from S1 based on 
the following conditions.
- For the 1st digit D in S2, the program must form an integer using the first D digits of S1.
- For the 2nd digit D in S2, the program must form an integer using the next D digits of S1.
- Similarly, the program must form integer values from the digits of S1, but if a digit in S2 is negative, then the sign of the corresponding integer must be negative.
Finally, the program must print the sum of integers obtained from S1 as the output.

Boundary Condition(s):
1 <= Length of S1 <= 100
3 <= Length of S2 <= 100

Input Format:
The first line contains S1.
The second line contains S2.

Output Format:
The first line contains an integer representing the sum of integers obtained from S1 based on the given conditions.

Example Input/Output 1:
Input:
5465798465141212465
(4)(-3)(1)(-2)(5)(4)

Output:
21192

Explanation:
(4) -> 5465
(-3) -> -798
(1) -> 4
(-2) -> -65
(5) -> 14121
(4) -> 2465
5465-798+4-65+14121+2465 = 21192.

Example Input/Output 2:
Input:
120044572112
(2)(4)(-6)

Output:
-572056

Explanation:
(2) -> 12
(4) -> 0044 -> 44
(-6) -> 572112
12+44-572112 = -572056.
"""
a=input().strip()
b=input().strip()
total=0
flag=False
t=''
for i in b:
    if i==')':
        flag=False
        t=int(t)
        if t<0:
            t=-t
            total-=int(a[:t])
        else:
            total+=int(a[:t])
        a=a[t:]
        t=''
    else:
        if flag:
            t+=i
        if i=='(':
            flag=True
print(total)
