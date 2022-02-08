"""
The program must accept an integer N as the input. The program must print (2*N)-1 lines of pattern as shown in the Example Input/Output section. The asterisks in the pattern
indicate the diamond and plus symbols. The hyphens in the pattern indicate the empty spaces.

Boundary Condition(s):
2 <= N <= 50

Input Format:
The first line contains N.

Output Format:
The first (2*N)-1 lines contain the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
Input:
5

Output:
--------*
------*-*-*
----*---*---*
--*-----*-----*
*-*-*-*-*-*-*-*-*
--*-----*-----*
----*---*---*
------*-*-*
--------*

Explanation:
Here N=5, so the pattern contains 9 lines ((2*5)-1) of output.

Example Input/Output 2:
Input:
3

Output:
----*
--*-*-*
*-*-*-*-*
--*-*-*
----*

Example Input/Output 3:
Input:
6

Output:
----------*
--------*-*-*
------*---*---*
----*-----*-----*
--*-------*-------*
*-*-*-*-*-*-*-*-*-*-*
--*-------*-------*
----*-----*-----*
------*---*---*
--------*-*-*
----------*
"""
n=int(input())
col=n*2-1
start_hy=col-1
center_hy=-1
l=[]
for i in range(n-1):
    s=''
    s+='-'*start_hy
    if i>0:
        for j in range(2):
            s+='*','-'*center_hy
    s+='*'
    start_hy-=2
    center_hy+=2
    print(s)
    l.insert(0,s)
print('*-'*(col-1),'*',sep='')
for i in l:
    print(i)
