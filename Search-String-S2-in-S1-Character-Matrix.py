"""
Given two strings S1 and S2, form a R*C matrix with the string S1 (You may repeat the string S1 to fill in the rest of the matrix, if length of S1 is less than R*C). 
Then search for the string S2 along rows from left to right or along columns from top to bottom) and print the number of occurrence of S2.

Input Format:
The first line contains R and C separated by a space.
The second line contains S1.
The third line contains S2.

Output Format:
The first line contains the integer value denoting the number of occurrence of S2 in the character matrix formed.

Boundary Conditions:
2 <= R, C <= 100
2 <= Length of S1 <= 10000
2 <= Length of S2 <= 200

Example Input/Output 1:
Input:
5 4
managermetuatten
man

Output:
3

Explanation:
The 5*4 character matrix formed using S1 is
mana
germ
etua
tten
mana

man can be found in 1st row from left to right and in 4th column from top to bottom. Then it is also found in 5th row. 
Hence the overall occurrence count is 3.
"""
r,c=map(int,input().split())
s1=input().strip()
s2=input().strip()
tot=r*c
l=len(s1)
s1=s1*(tot//l) + s1[:tot%l]
l=len(s2)
count=0
start=0
for i in range(r):
    for j in range(c-l+1):
        if s2==s1[start+j:start+j+l]:
            count+=1
    start+=c
for j in range(c):
    t=j
    s=""
    for i in range(r):
        s+=s1[t]
        t+=c
    for i in range(r-l+1):
        if s2==s[i:i+l]:
            count+=1
print(count)
