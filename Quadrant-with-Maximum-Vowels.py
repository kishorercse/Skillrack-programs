"""
The program must accept a character matrix of size RxC as the input. The program must print the quadrant of the matrix having the maximum number of vowels. If more than one
quadrants have the same maximum number of vowels, the program must print the first occurring quadrant as the output. Note: The values of R and C are always even. At least one
vowel will occur in the matrix. 

Boundary Condition(s): 
2 <= R, C <= 50 

Input Format: 
The first line contains R and C separated by a space.
The next R lines, each containing C characters separated by a space.

Output Format: 
The first R/2 lines, each containing C/2 characters separated by a space. 

Example Input/Output 1:
Input:
4 6
a m b b u o 
e q z k g e 
c f x i i n 
o s t e x a 

Output:
i i n 
e x a

Explanation:
The number of vowels in the first quadrant is 2. 
The number of vowels in the second quadrant is 3.
The number of vowels in the third quadrant is 1. 
The number of vowels in the fourth quadrant is 4.
Here the fourth quadrant has the maximum number of vowels.
So it is printed as the output. 

Example Input/Output 2:
Input:
8 10
p S T I A J K Q k D
H k V e d W G W c y
m v I n Z Q J O i P
X T I n c y W y R j
x c k R u r s w E o
U U w f H A f n M b
r J H W y S n I s e
A w w n K y M V R d

Output:
p S T I A 
H k V e d 
m v I n Z 
X T I n c
"""
r,col=map(int,input().split())
m=[input().split() for _ in range(r)]
rh=r//2
ch=col//2
a=b=c=d=0
for i in range(r):
    for j in range(col):
        if m[i][j] in "AEIOUaeiou":
            if i<rh:
                if j<ch:
                    a+=1
                else:
                    b+=1
            else:
                if j<ch:
                    c+=1
                else:
                    d+=1
mx=max(a,b,c,d)
if mx==a:
    r1,r2=0,rh
    c1,c2=0,ch
elif mx==b:
    r1,r2=0,rh
    c1,c2=ch,col
elif mx==c:
    r1,r2=rh,r
    c1,c2=0,ch
else:
    r1,r2=rh,r
    c1,c2=ch,col
for i in range(r1,r2):
    for j in range(c1,c2):
        print(m[i][j],end=' ')
    print()
