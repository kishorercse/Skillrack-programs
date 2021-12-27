"""
The program must accept a string S containing only alphabets as the input. The program must replace all the consecutive occurrences of the alphabets(ignoring case) with 1s and 
all the remaining alphabets with 0s. Finally, the program must print the decimal equivalent of S by considering it as a binary representation.

Boundary Condition(s):
1 <= Length of S <= 50

Input Format:
The first line contains S.

Output Format:
The first line contains an integer value based on the given conditions.

Example Input/Output 1:
Input:
oops

Output:
12

Explanation:
oops -> 1100 -> 12

Example Input/Output 2:
Input:
AabBCcdeEeg

Output:
2030

Explanation:
AabBCcdeEeg -> 11111101110 -> 2030
"""
s=input().strip().lower()
res='0'
l=len(s)
started=False
for i in range(1,l):
    if s[i]==s[i-1]:
        if not started:
            res=res[:-1]
            res+='11'
            started=True
        else:
            res+='1'
    else:
        res+='0'
        started=False
print(int(''.join(res),2))
