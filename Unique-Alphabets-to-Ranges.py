"""
The program must accept a string S containing only lower case alphabets as the input. The program must find the unique alphabets in the given string and print the
alphabets as ranges in sorted order as shown in the Example Input/Output section.

Boundary Condition(s):
1 <= Length of S <= 100

Input Format:
The first line contains S.

Output Format:
The lines contain the alphabets ranges in sorted order.

Example Input/Output 1:
Input:
fhjgipqrtsifif

Output:
f:j
p:t

Explanation:
Here S = fhjgipqrtsifif.
The unique alphabets present in the string S are given below.
f g h i j p q r s t
1st range -> f:j
2nd range -> p:t

Example Input/Output 2:
Input:
abbackxxyzzponm

Output:
a:c
k:k
m:p
x:z
"""
s=sorted(set(input().strip()))
l=len(s)
print(s[0],end=':')
for i in range(1,l):
    if ord(s[i])-ord(s[i-1])!=1:
        print(s[i-1])
        print(s[i],end=':')
print(s[-1])
