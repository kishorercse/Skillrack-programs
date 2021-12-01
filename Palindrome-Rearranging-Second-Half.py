"""
The program must accept a string S as the input. The program must print a palindromic string P if it is possible to form the string P by rearranging the characters in the second
half of S. Else the program must print -1 as the output.
Note: The length of S is always even.

Boundary Condition(s):
2 <= Length of S <= 100

Input Format:
The first line contains S.

Output Format:
The first line contains P or -1

Example Input/Output 1:
Input:
rackcrak

Output:
rackkcar

Explanation:
The second half of the string "rackcrak" is "crak". So it can be rearranged as "kcar".
Now the string becomes "rackkcar" which is a palindrome.
Hence the output is rackkcar

Example Input/Output 2:
Input:
labcab

Output:
-1
"""
s=input().strip()
l=len(s)
firstHalf={}
secondHalf={}
f=True
for i in range(l//2):
    firstHalf[s[i]]=firstHalf.get(s[i],0)+1
for i in range(l//2,l):
    if s[i] not in firstHalf:
        f=False
        break
    secondHalf[s[i]]=secondHalf.get(s[i],0)+1
if f and (all(firstHalf[i]==secondHalf[i]) for i in firstHalf):
    print(s[:l//2]+s[l//2-1::-1])
else:
    print(-1)
