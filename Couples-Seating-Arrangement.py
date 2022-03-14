"""
There are N seats in a row and some seats are already booked. The program must accept a string S representing the status of N seats. The character M indicates a male. The 
character F indicates a female. The character hash symbol (#) indicates an empty seat. The program must print the maximum number of couples that can be seated together in the 
empty seats based on the following condition.
- The neighboring seats of couples must be of the same gender or empty.

Boundary Condition(s):
1 <= N <= 100

Input Format:
The first line contains N.
The second line contains S.

Output Format:
The first line contains the maximum number of couples that can be seated together in the empty seats.

Example Input/Output 1:
Input:
19
FF##MM##MFF##FFF###

Output:
2

Explanation:
A maximum of 2 couples can be seated in the row.
One of the possible ways is given below.
FFFMMM##MFF##FFFFM#

Example Input/Output 2:
Input:
18
####MM###M######M#

Output:
5

Example Input/Output 3:
Input:
16
##########F####M

Output:
6
"""
n=int(input())
s=list(input().strip())
couple=i=0
if (s[i]=='#'):
    while i<n and s[i]=='#':
        i+=1
    couple+=i//2
while i+1<n:
    if s[i]=='#' and s[i+1]=='#':
        if s[i-1]=='M' and (i+2>=n or s[i+2] in "F#"):
            s[i]='M'
            s[i+1]='F'
            i+=2
            couple+=1
            continue
        elif s[i-1]=='F' and (i+2>=n or s[i+2] in "M#"):
            s[i]='F'
            s[i+1]='M'
            i+=2
            couple+=1
            continue
    i+=1
print(couple)
