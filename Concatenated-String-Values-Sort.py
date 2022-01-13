"""
The program must accept two string values S1 and S2 of equal length L as the input. Both S1 and S2 have the same unique lower case alphabets. The program must form L string 
values based on the following condition.
- For each alphabet CH in S1, the program must form a string using the alphabets that occur till CH in S1 and the alphabets that occur after CH in S2.
Then the program must print the obtained L string values in sorted order.

Boundary Condition(s):
2 <= Length of S1, S2 <= 26

Input Format:
The first line contains S1.
The second line contains S2.

Output Format:
The first L lines contain L string values in sorted order.

Example Input/Output 1:
Input:
lion
oiln

Output:
liln
lioiln
lion
ln

Explanation:
Here S1 = "lion" and S2 = "oiln".
1st string: "l" + "n" = "ln".
2nd string: "li" + "ln" = "liln".
3rd string: "lio" + "iln" = "lioiln".
4th string: "lion" + "" = "lion".
So the four string values are printed in sorted order.

Example Input/Output 2:
Input:
capture
rcupeat

Output:
capeat
capt
captupeat
capturcupeat
captureat
cat
cupeat
"""
s1=input().strip()
s2=input().strip()
l=len(s2)
ind={}
for i in range(l):
    ind[s2[i]]=i
ans=[]
t=''
for i in s1:
    ans.append(t+s2[ind[i]:])
    t+=i
print(*sorted(ans),sep='\n')
