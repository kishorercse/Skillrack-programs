"""
The program must accept a string S as the input. The program must print the desired pattern as shown in the Example Input/Output section. 

Boundary Condition(s): 
2 <= Length of S <= 100

Input Format: 
The first line contains S. 

Output Format: 
The lines containing the desired pattern as shown in the Example Input/Output section. 

Example Input/Output 1:
Input:
hello

Output:
hellohello
*hellohel*
**helloh**
***hell***
****he****

Example Input/Output 2: 
Input:
ACHIEVED

Output:
ACHIEVEDACHIEVED
*ACHIEVEDACHIEV*
**ACHIEVEDACHI**
***ACHIEVEDAC***
****ACHIEVED****
*****ACHIEV*****
******ACHI******
*******AC*******
"""
s=input().strip()
l=len(s)
s*=2
star='*'
a=-2
print(s)
for i in range(1,l):
    print(star,s[:a],star,sep='')
    star+='*'
    a-=2
