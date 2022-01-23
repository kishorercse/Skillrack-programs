"""
The program must accept a string S representing the keys that are used to type a message in a text editor. The keys can be any of the following.
- All 26 lower case alphabets.
- "SHIFT" key.
- "CAPSLOCK" key.
Initially, the CAPSLOCK is turned off. The alphabets that occur after "SHIFT+" must be toggled(upper to lower or lower to upper). The program must find the message from the 
given string and print it is as the output.

Boundary Condition(s):
1 <= Length of S <= 1000

Input Format:
The first line contains S.

Output Format:
The first line contains a string value representing the message.

Example Input/Output 1:
Input:
SHIFT+s k i l l CAPSLOCK r SHIFT+ack a b c

Output:
SkillRackABC

Explanation:
Initially, the CAPSLOCK = OFF.
SHIFT+s -> S
k -> k
i -> i
l -> l
l -> l
CAPSLOCK = ON.
r -> R
SHIFT+ack -> ack
a -> A
b -> B
c -> C
Hence the output is SkillRackABC.

Example Input/Output 2:
Input:
CAPSLOCK s k i l l SHIFT+rack CAPSLOCK SHIFT+c o d e

Output:
SKILLrackCode
"""
s=input().split()
caps=False
for i in s:
    if i[:6]=='SHIFT+':
        if caps==False:
            print(i[6:].swapcase(),end='')
        else:
            print(i[6:],end='')
    elif i=='CAPSLOCK':
        caps=not caps
    else:
        if caps:
            print(i.upper(),end='')
        else:
            print(i,end='')
