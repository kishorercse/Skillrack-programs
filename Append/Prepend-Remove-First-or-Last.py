"""
The program must accept N queries as the input. The program must form a string S based on the given N queries. Initially, the string S is empty. Each query can be any of the
following four types.
1) +CH => Append the character CH to S.
2) CH+ => Prepend the character CH to S.
3) -CH => Remove the last occurrence of CH in S only if CH is present in S.
4) CH- => Remove the first occurrence of CH in S only if CH is present in S.
The program must print the string S after processing the N queries as the input. If the string S is empty after processing the N queries, then the program must print -1 as the 
output.

Boundary Condition(s):
1 <= N <= 1000

Input Format:
The first line contains N.
The second line contains N queries separated by a space.

Output Format:
The first line contains S or -1.

Example Input/Output 1:
Input:
8
+c o+ c+ -c e+ +d +e e-

Output:
code

Explanation:
Initially, the string S is empty.
+c => S = "c"
o+ => S = "oc"
c+ => S = "coc"
-c => S = "co"
e+ => S = "eco"
+d => S = "ecod"
+e => S = "ecode"
e- => S = "code"

Example Input/Output 2:
Input:
9
+c +k -S a+ R+ -R -a -c -k

Output:
-1
"""

n=int(input())
l=input().split()
s=[]
length=0
for i in l:
    if i[0]=='+':
        s.append(i[1])
        length+=1
    elif i[-1]=='+':
        s.insert(0,i[0])
        length+=1
    elif i[0]=='-':
        for ind in range(length-1,-1,-1):
            if s[ind]==i[-1]:
                s.pop(ind)
                length-=1
                break
    elif i[-1]=='-':
        try:
            s.remove(i[0])
            length-=1
        except ValueError:
            pass
if length==0:
    print(-1)
else:
    print(''.join(s))
