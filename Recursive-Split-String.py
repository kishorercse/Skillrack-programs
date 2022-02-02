"""
The program must accept a string S as the input. The program must split the string recursively based on the following conditions.
- If the length of the string is even, then the program must split the string into two equal halves. Else consider the middle character for the second half. After dividing the
string, the program must print the resulting string values.
- Then the program must repeat the above process of dividing each word in the string S till the length of each word becomes 1.

Boundary Condition(s):
2 <= Length of S <= 100

Input Format:
The first line contains S.

Output Format:
The lines contain the string values separated by a space.

Example Input/Output 1:
Input:
abcdefgh

Output:
abcd efgh
ab cd ef gh
a b c d e f g h

Explanation:
Here the given string is abcdefgh.
1st split: abcd efgh
2nd split: ab cd ef gh
3rd split: a b c d e f g h

Example Input/Output 2:
Input:
skillrack

Output:
skil lrack
sk il lr ack
s k i l l r a ck
s k i l l r a c k

Example Input/Output 3:
Input:
exhibition

Output:
exhib ition
ex hib it ion
e x h ib i t i on
e x h i b i t i o n
"""
#Recursive
def fun(lst):
    f=False
    r=[]
    for i in lst:
        l=len(i)
        if l>1:
            l//=2
            r+=[i[:l],i[l:]]
            f=True
        else:
            r+=[i]
    if f:
        print(*r)
        fun(r)
#Iterative
s=[input().strip()]
fun(s)
s=[input().strip()]
l=[]
f=True
while f:
    f=False
    for i in s:
        t=len(i)
        if t>1:
            t//=2
            l+=[i[:t],i[t:]]
            f=True
        else:
            l+=[i]
    s=l[:]
    if f: 
        print(*l)
    l.clear()
