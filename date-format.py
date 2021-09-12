"""

The program must accept a date as the input. The program must print the date in the mentioned format as shown in the Example Input/Output section.

Input Format:
The first line contains the input date in the format YYYYMMDD where YYYY represents Year, MM represents Month and DD represents Date.

Output Format:
The first line contains the date as shown in the Example Input/Output section.

Example Input/Output :
Input:
20160302

Output:
2016, 2nd of March
"""
s=input().strip()
l=['January','February','March','April','May','June','July','August','September','October','November','December']
t=int(s[-2:])
a='th'
if t==1 or t==21:
    a='st'
elif t==2 or t==22:
    a='nd'
elif t==3 or t==23:
    a='rd'
print(s[:4],end=', ')
print(t,a,sep='',end=' ')
print('of',l[int(s[4:6])-1])
