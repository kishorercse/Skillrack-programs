"""
The program must accept two string values S1, S2 and an integer N as the input. The program must print the string ladder pattern based on the following conditions.
- The ladder must have N rungs, where each rung must be formed by the string S2.
- The rungs must be evenly spaced apart.
- The two rails of the ladder must be formed by the string S1 and the reverse of S1 alternatively as show in the Example Input/Output section.
- The asterisks must be printed instead of the empty spaces in the string ladder pattern.

Note: The first and last characters of S1 and S2 are always same.

Boundary Condition(s):
5 <= Length of S1, S2 <= 100
1 <= N <= 100

Input Format:
The first line contains S1.
The second line contains S2.
The third line contains N.

Output Format:
The lines contain the string ladder pattern as shown in the Example Input/Output section.

Example Input/Output 1:
Input:
classic
cryptic
2

Output:
c*****c
l*****l
a*****a
s*****s
s*****s
i*****i
cryptic
i*****i
s*****s
s*****s
a*****a
l*****l
cryptic
l*****l
a*****a
s*****s
s*****s
i*****i
c*****c

Explanation:
Here S1 = classic, S2 = cryptic and N = 2. So the ladder has 2 rungs.
Each rung of the ladder is formed using the string S2.
The two rails of the ladder are formed using the string S1, reverse of S1 and S1.

Example Input/Output 2:
Input:
level
label
3

Output:
l***l
e***e
v***v
e***e
label
e***e
v***v
e***e
label
e***e
v***v
e***e
label
e***e
v***v
e***e
l***l
"""
a=input().strip()
b=input().strip()
n=int(input())
a_len=len(a)
b_len=len(b)
s='*'*(b_len-2)
l=[a[i]+s+a[i] for i in range(a_len)]
print(l[0])
for rungs in range(1,n+2):
    if rungs%2!=0:
        for row in range(1,a_len-1):
            print(l[row])
    else:
        for row in range(a_len-2,0,-1):
            print(l[row])
    if rungs<=n:
        print(b)
print(l[0])
