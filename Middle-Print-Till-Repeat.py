"""
A string S (without any spaces) whose length is odd is passed as the input. The program must start printing from the middle character, then its immediate left and right 
characters. Then it must print the next immediate left and right characters and so on till one of the characters is repeated.

Boundary Condition(s):
1 <= Length of S <= 101

Input Format:
The first line contains S.

Output Format:
The first line contains a string value.

Example Input/Output 1:
Input:
character

Output:
arca

Explanation:
The middle character is a. Then r, c are printed.
Then a, t are to be printed. But when a is printed it has been repeated already.
So we stop.

Example Input/Output 2:
Input:
mango

Output:
nagmo
"""
s=input().strip()
l=len(s)
rep=set([s[l//2]])
print(s[l//2],end='')
left=l//2 - 1
right=l//2 + 1
while right<l:
    print(s[left],end='')
    if s[left] in rep:
        break
    rep.add(s[left])
    left-=1
    print(s[right],end='')
    if s[right] in rep:
        break
    rep.add(s[right])
    right+=1
