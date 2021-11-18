"""
The program must accept a string S and an integer K as the input. The program must print the string S in triangular wave pattern of width K as shown in the Example Input/Output
section. 

Boundary Condition(s):
1 <= Length of S <= 100 
2 <= K <= 20 

Input Format: 
The first line contains S.
The second line contains K.

Output Format:
The lines contain the string S in triangular wave pattern as shown in the Example Input/Output section. 

Example Input/Output 1:
Input:
Algorithm
3

Output: 
A
*l
**g
*o 
r
*i
**t
*h
m

Explanation:
Here the given string is Algorithm and the value of K is 3. 
The length of the string is 9, so the pattern contains 9 lines of output.
The vertical triangular wave pattern of width 3 for the given string is 
A
*l
**g
*o 
r 
*i
**t
*h
m

Example Input/Output 2: 
Input:
abcdefghijklmnopqrstuvwxyz 
4

Output:
a
*b
**c
***d
**e 
*f
g
*h
**i
***j 
**k
*l
m
*n
**o
***p
**q
*r
s 
*t
**u
***v
**w
*x
y 
*z
"""
s=input().strip()
k=int(input())
l=len(s)
a=0
diff=1
for i in range(0,l,k):
    for j in range(i,min(l,i+k)):
        print('*'*a,s[j],sep='')
        a+=diff
        if a==k:
            diff=-1
            a=k-2
        elif a==-1:
            diff=1
            a=1
