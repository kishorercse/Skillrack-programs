"""
There are N string values that start with the same letter, but some string values are reversed. The program must accept those N string values and print the N string values that 
indicate the original string values as the output. 

Note:
- There will be no string that starts and ends with the same letter.
- All string values do not end with the same letter. 
- All string values contain only lower case alphabets. 

Boundary Condition(s):
2 <= N <= 50 
2 <= Length of each string <= 100

Input Format: 
The first line contains N. 
The next N lines, each contains a string value. 

Output Format: 
The first N lines, each contains a string value.

Example Input/Output 1: 
Input: 
5 
rabbit
rose 
tekcor
egnar 
robbery 

Output: 
rabbit 
rose 
rocket
range 
robbery 

Explanation:
The first letter of all the 5 strings values is r. 
So the 3rd and 4th string values are reversed. 
tekcor -> rocket 
egnar -> range 

Example Input/Output 2:
Input:
4
olleh
oah
hacked
dah

Output:
hello 
hao 
hacked 
had
"""
n=int(input())
s=input().strip()
a=s[0][0]
b=s[0][-1]
for i in range(1,n):
    l.append(input().strip())
    if a!=l[i][0] and a!=l[i][-1]:
        a=''
    if b!=l[i][0] and b!=l[i][-1]:
        b=''
a=max(a,b)
for i in l:
    if i[0]!=a:
        print(i[::-1])
    else:
        print(i)
