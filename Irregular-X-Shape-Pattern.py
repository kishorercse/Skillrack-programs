"""
The program must accept four string values S1, S2, S3 and S4 as the input. The program must print the irregular X-shape pattern using the four string values. The string S1 must
be printed from the middle to the top-left, S2 must be printed from the middle to the top-right, S3 must be printed from the middle to the bottom-left and S4 must be printed 
from the middle to the bottom-right. The empty spaces must be printed as asterisks as shown in the Example Input/Output section.

Boundary Condition(s):
3 <= Length of S1, S2, S3, S4 <= 100

Input Format:
The first line contains S1.
The second line contains S2.
The third line contains S3.
The fourth line contains S4.

Output Format:
The lines contain the irregular X-shape pattern as shown in the Example Input/Output section.

Example Input/Output 1:
Input:
forest
plant
college
code

Output:
*t**********
**s********t
***e******n*
****r****a**
*****o**l***
******fp****
******cc****
*****o**o***
****l****d**
***l******e*
**e*********
*g**********
e***********

Explanation:
S1(forest) is printed from the middle to the top-left.
S2(plant) is printed from the middle to the top-right.
S3(college) is printed from the middle to the bottom-left.
S4(code) is printed from the middle to the bottom-right.
All the empty spaces are printed as asterisks.

Example Input/Output 2:
Input:
fox
tiger
cow
monkey

Output:
*******r*
******e**
x****g***
*o**i****
**ft*****
**cm*****
*o**o****
w****n***
******k**
*******e*
********y
"""
a=input().strip()
b=input().strip()
c=input().strip()
d=input().strip()
al,bl,cl,dl=len(a),len(b),len(c),len(d)
rows=max(al,bl)
cols=max(al,cl)+max(bl,dl)
ar=rows-al
ac=max(al,cl)-al
br=rows-bl
bc=cols-(max(bl,dl)-bl)-1
aind=al-1
bind=bl-1
for i in range(rows):
    fa=fb=False
    for j in range(cols):
        if i>=ar and j==ac:
            print(a[aind],end='')
            aind-=1
            fa=True
        elif i>=br and j==bc:
            print(b[bind],end='')
            bind-=1
            fb=True
        else:
            print('*',end='')
    print()
    if fa: ac+=1
    if fb: bc-=1
rows=max(cl,dl)
cind=dind=0
cc=max(al,cl)-1
dc=cc+1
for i in range(rows):
    for j in range(cols):
        if cind<cl and j==cc:
            print(c[cind],end='')
            cind+=1
        elif dind<dl and j==dc:
            print(d[dind],end='')
            dind+=1
        else:
            print('*',end='')
    print()
    cc-=1
    dc+=1
