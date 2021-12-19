"""
The program must accept four string values S1, S2, S3 and S4 as the input. The program must print the irregular plus shape pattern using the four string values. All four 
string values start with the same letter. The string S1 must be printed from the middle to the top, S2 must be printed from the middle to the right, S3 must be printed 
from the middle to the bottom and S4 must be printed from the middle to the left. The empty spaces must be printed as asterisks as shown in the Example Input/Output section.

Boundary Condition(s):
2 <= Length of each string <= 100

Input Format:
The first line contains S1.
The second line contains S2.
The third line contains S3.
The fourth line contains S4.

Output Format:
The lines contain the pattern as shown in the Example Input/Output section.

Example Input/Output 1:
Input:
lion
ladder
lands
led

Output:
**n*****
**o*****
**i*****
deladder
**a*****
**n*****
**d*****
**s*****

Explanation:
The string lion is printed from the middle to the top.
The string ladder is printed from the middle to the right.
The string lands is printed from the middle to the bottom.
The string led is printed from the middle to the left.
The empty spaces in the pattern are printed as asterisks.

Example Input/Output 2:
Input:
kit
kingdom
know
kettle

Output:
*****t******
*****i******
elttekingdom
*****n******
*****o******
*****w******
"""
a=input().strip()
b=input().strip()
c=input().strip()
d=input().strip()
p,q='*'*(len(d)-1),'*'*(len(b)-1)
for i in range(len(a)-1,0,-1):
    print(p,a[i],q,sep='')
print(d[-1:0:-1],b,sep='')
for i in range(1,len(c)):
    print(p,c[i],q,sep='')
