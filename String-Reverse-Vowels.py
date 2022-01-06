"""
Given a string S, reverse only the vowels in the string S and print the resultant string R as the output. The consonants must maintain their original locations in S.

Input Format:
The first line contains S.

Output Format:
The first line contains R.

Boundary Conditions:
Length of S is from 2 to 500.

Example Input/Output 1:
Input:
idea

Output:
adei

Example Input/Output 2:
Input:
hello

Output:
holle
"""
s=list(input().strip())
i,j=0,len(s)-1
while i<j:
    if s[i] in "AEIOUaeiou" and s[j] in "AEIOUaeiou":
        s[i],s[j]=s[j],s[i]
        i+=1
        j-=1
    while i<j and s[i] not in "AEIOUaeiou":
        i+=1
    while i<j and s[j] not in "AEIOUaeiou":
        j-=1
print(''.join(s))
