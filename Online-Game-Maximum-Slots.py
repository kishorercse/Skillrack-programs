"""
In an online game, a 15-minute round starts in each quarter-hour period (00:00 - 00:15, 00:15 - 00:30, 00:30 - 00:45, 00:45 - 01:00, ... 23:15 - 23:30, 23:30 - 23:45, 
23:45 - 00:00, ... and so on). Hector wants to play the game from T1 to T2 (in 24-hr format). The starting time T1 and the ending time T2 are passed as the input. 
The program must print the maximum number of times Hector can play the game completely as the output.

Input Format:
The first line contains the starting time T1 and the ending time T2 (in 24-hr format).

Output Format:
The first line contains the maximum number of times Hector can play the game.

Example Input/Output 1:
Input:
10:18 11:13

Output:
2

Explanation:
Hector can play the game completely twice and the two slots are given below.
10:30 to 10:45
10:45 to 11:00

Example Input/Output 2:
Input:
15:00 17:59

Output:
11

Example Input/Output 3:
Input:
22:50 00:35

Output:
6
"""
s,e=input().split()
a,b=map(int,s.split(':'))
s=a*60+b
if (b%15!=0):
    s+=(15-b%15)
a,b=map(int,e.split(':'))
e=a*60+b-b%15
if e<s:
    e+=24*60
print((e-s)//15)
