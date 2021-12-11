"""
A string S will be passed as input to the program. The program must reverse the characters in between the first and last letters and print the new value R.

Input Format:
First line contains total number of test cases, denoted by T
Next T lines will contain value of S for that test case.

Output Format:
T lines containing the reversed number as per the condition mentioned.

Boundary Conditions / Constraints:
1 <= T <= 25
3 <= Length of S <= 1000


Example Input/Output 1:
Input:
3
902871
sunrise56morning
kick_torrent_pira()cy

Output:
978201
sninrom65esirnug
kc)(arip_tnerrot_kciy
"""
t=int(input())
while t>0:
    s=input().strip()
    print(s[0]+s[-2:0:-1]+s[-1])
    t-=1
