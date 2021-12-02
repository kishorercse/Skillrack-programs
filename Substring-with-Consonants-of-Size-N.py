"""
The program must accept a string S containing only alphabets and an integer N as the input. The program must print all the substring values of size N in S, where all the
alphabets are consonants as the output. If there is no such substring of size N then the program must print -1 as the output.
Note: The substring values must be printed in the order of their occurrences.

Boundary Condition(s):
1 <= Length of S <= 100
1 <= N <= Length of S

Input Format:
The first line contains S and N separated by a space.

Output Format:
The first line contains the substring value(s) based on the given conditions or -1.

Example Input/Output 1:
Input:
skillrack 2

Output:
sk ll lr ck

Explanation:
In the string skillrack, there are 4 substring values of size 2 containing only consonants.
So the output is sk ll lr ck

Example Input/Output 2:
Input:
ENTERPRISE 3

Output:
RPR

Example Input/Output 3:
Input:
Banana 4

Output:
-1
"""
s,n=input().split()
l=len(s)
n=int(n)
i=0
f=False
while i<=l-n:
    for ind in range(i,i+n):
        if s[ind] in "AEIOUaeiou":
            i=ind+1
            break
    else:
        print(s[i:i+n],end=' ')
        f=True
        i+=1
if not f:
    print(-1)
