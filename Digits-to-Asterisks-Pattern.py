 """
The program must accept a string S containing only nonzero digits as the input. The program must print the pattern based on the following conditions. - For each digit D in S, 
the program must print D asterisks in the Dth line from the bottom of the pattern. - After printing D asterisks in the Dth line, then the asterisks for the next digit of D must
be printed from the next column of the pattern. 
- Similarly, the asterisks must be printed for all the digits in the string S. 
- The empty spaces in the pattern must be printed as hyphens. 
  
Boundary Condition(s):
1 <= Length of S <= 100 
 
Input Format: 
The first line contains S.
 
Output Format:
The lines contain the asterisks and hyphens as shown in the Example Input/Output section.

Example Input/Output 1:
Input: 
1234325 

Output:
---------------*****
------****----------
---***----***-------
-**----------**-----
*-------------------

Explanation:
1 -> 1 asterisk is printed in the 1st line from the bottom.
2 -> 2 asterisks are printed in the 2nd line from the bottom.
3 -> 3 asterisks are printed in the 3rd line from the bottom.
4 -> 4 asterisks are printed in the 4th line from the bottom.
3 -> 3 asterisks are printed in the 3rd line from the bottom.
2 -> 2 asterisks are printed in the 2nd line from the bottom.
5 -> 5 asterisks are printed in the 5th line from the bottom.
The remaining empty spaces are printed as hyphens. 

Example Input/Output 2:
Input:
412735 

Output: 
-------*******--------
----------------------
-----------------*****
****------------------
--------------***-----
-----**---------------
----*-----------------
"""
s=list(map(int,input().strip()))
l=len(s)
mx=max(s)
x=0
tot=sum(s)
m=[list('-'*tot) for i in range(mx)]
for i in range(l):
    m[s[i]-1][x:x+s[i]]=list('*'*s[i])
    x+=s[i]
for i in m[::-1]:
    print(*i,sep='')
