"""
The program must accept a string S containing alphabet-integer pairs as the input. For each alphabet-integer pair (CH-X), the program must form a square matrix of size X*X with 
the alphabet CH. Then the program must print those matrices horizontally as shown in the Example Input/Output section. The empty spaces must be printed as asterisks.

Boundary Condition(s):
2 <= Length of S <= 100
1 <= X <= 15

Input Format:
The first line contains S.

Output Format:
The lines contain the matrices horizontally as shown in the Example Input/Output section.

Example Input/Output 1:
Input:
a3b4c5d2

Output:
a a a b b b b c c c c c d d
a a a b b b b c c c c c d d
a a a b b b b c c c c c * *
* * * b b b b c c c c c * *
* * * * * * * c c c c c * *

Explanation:
Here the given string is a3b4c5d2.
For the 1st pair (a, 3), the 3*3 matrix is given below.
a a a
a a a
a a a

For the 2nd pair (b, 4), the 4*4 matrix is given below.
b b b b
b b b b
b b b b
b b b b

For the 3rd pair (c, 5), the 5*5 matrix is given below.
c c c c c
c c c c c
c c c c c
c c c c c
c c c c c

For the 4th pair (d, 2), the 2*2 matrix is given below.
d d
d d

So the four square matrices are printed horizontally.

Example Input/Output 2:
Input:
Y2Z1W3

Output:
Y Y Z W W W
Y Y * W W W
* * * W W W
"""
s=input().strip()
rows=-1
l=[]
ch=s[0]
x=''
for i in s[1:]:
    if i.isalpha():
        x=int(x)
        rows=max(x,rows)
        l.append([x,ch*x])
        ch=i
        x=''
    else:
        x+=i
x=int(x)
rows=max(x,rows)
l.append([x,ch*x])
for i in range(rows):
    for c,s in l:
        if i>=c:
            print('* '*c,end='')
        else:
            print(*s,end=' ')
    print()
