"""
The program must accept two string values S1 and S2 of equal length as the input. The program must split both the string values at the same position. If the concatenation of the first part of S1 and the second part of S2 forms a palindrome or the concatenation of the first part of S2 and the second part of S1 forms a palindrome, then the program must print YES as the output. Else the program must print NO as the output.

Boundary Condition(s):
1 <= Length of S1, S2 <= 1000

Input Format:
The first line contains S1.
The second line contains S2.

Output Format:
The first line contains YES or NO.

Example Input/Output 1:
Input:
hello
poleh

Output:
YES

Explanation:
Here S1 = hello and S2 = poleh.
All possible splits are given below.
h ello
p oleh

he llo
po leh

hel lo
pol eh

hell o
pole h
The palindrome heleh is formed by concatenating (hel and eh) or (he and leh).
So YES is printed as the output.

Example Input/Output 2:
Input:
abcdef
fecdba

Output:
NO
"""
def ispalindrome(s):
    i=0
    j=l-1
    while i<j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True
a=input().strip()
b=input().strip()
l=len(a)
for i in range(1,l):
    if ispalindrome(a[:i]+b[i:]) or ispalindrome(b[:i]+a[i:]):
        print("YES")
        break
else:
    print("NO")
