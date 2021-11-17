"""
The program must accept a string S as the input. The program must print the desired pattern as shown in the Example Input/Output section. 

Boundary Condition(s): 
3 <= Length of S <= 100 

Input Format:
The first line contains the string S.

Output Format: 
The list of lines containing the desired pattern as shown in the Example Input/Output section. 

Example Input/Output 1: 
Input:
abcde

Output:
abcd* 
****e 
abc** 
***de 
ab*** 
**cde
a****
*bcde

Example Input/Output 2:
Input:
calendar

Output:
calenda*
*******r
calend**
******ar
calen***
*****dar
cale****
****ndar
cal*****
***endar
ca******
**lendar
c*******
*alendar
"""
s=input().strip()
l=len(s)
for i in range(1,l):
    print(s[:l-i],'*'*i,sep='')
    print('*'*(l-i),s[l-i:],sep='')
