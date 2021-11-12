"""
The program must accept a string S that indicates the input of the keys entered on a keyboard. In the string S, each hyphen represents a backspace key. The program must modify 
the string S by performing the function of the backspace key. Then the program must print the modified string S as the output. If there are no alphabets after performing the 
function of backspace key in the string S, the program must print -1 as the output. 

Boundary Condition(s):
1 <= Length of S <= 1000 

Input Format: 
The first line contains S.

Output Format: 
The first line contains the modified string S. 

Example Input/Output 1:
Input:
skill----rack 

Output: 
srack 

Explanation: 
In the string skill----rack, four hyphens (backspace keys) have occurred.
So four characters entered before them are removed from the string. 
Hence the output is srack 

Example Input/Output 2:
Input: 
ab---d-monky-ey

Output: 
monkey 

Example Input/Output 3:
Input:
sdk---file---- 

Output:
-1
"""
s=input().strip()
t=''
for i in s:
    if i=='-':
        t=t[:-1]
    else:
        t+=i
if t:
    print(t)
else:
    print(-1)
