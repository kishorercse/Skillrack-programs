"""
The program must accept a string S representing an arithmetic expression. The expression contains the integer values and the operators in words (plus for +, minus for -, 
multiply for * and divide for /). The program must evaluate the expression from left to right and print the resulting integer value as the output.

Note: The divide operator (/) must return the quotient when the numerator is divided by the denominator.

Boundary Condition(s):
8 <= Length of S <= 1000
1 <= Each integer value <= 100

Input Format:
The first line contains S.

Output Format:
The first line contains an integer value representing the resulting integer.

Example Input/Output 1:
Input:
10 plus 20 minus 5 multiply 4 divide 50

Output:
2

Explanation:
S = 10 plus 20 minus 5 multiply 4 divide 50
= 10 + 20 - 5 * 4 / 50
= 30 - 5 * 4 / 50
= 25 * 4 / 50
= 100 / 50
= 2

Example Input/Output 2:
Input:
50 multiply 3 plus 21 plus 13 divide 3

Output:
61
"""
s=input().split()
res=int(s[0])
l=len(s)
for i in range(2,l,2):
    if s[i-1]=='plus':
        res+=int(s[i])
    elif s[i-1]=='minus':
        res-=int(s[i])
    elif s[i-1]=='multiply':
        res*=int(s[i])
    else:
        res//=int(s[i])
print(res)
