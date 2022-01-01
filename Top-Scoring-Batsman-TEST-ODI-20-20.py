"""
The program must accept the runs scored by N batsmen in the various cricket formats - TEST, ODI and 20-20 and print the top scoring batsman.
- In case two batsmen have scored same total runs, consider TEST cricket runs. The batsman who has scored higher runs in TEST cricket is the top scoring batsman.
- In case two batsmen have scored same total runs and have TEST cricket runs equal, consider ODI runs.
- In case two students have scored same total runs and have TEST and ODI runs equal, consider 20-20 runs.

Input Format:
The first line contains N.
N lines follow with each line containing Batsman Name and runs in TEST, ODI and 20-20 runs (the values are separated by a space).

Output Format:
The first line contains the name of the top Scoring Batsman.

Boundary Conditions:
1 <= N <= 20

Example Input/Output 1:
Input:
3
Raman 400 300 200
Dujon 800 50 50
Chandan 500 200 200

Output:
Dujon
"""
n=int(input())
l=[]
for _ in range(n):
    s=input().split()
    s[1:]=map(int,s[1:])
    s+=[sum(s[1:])]
    l.append(s)
print(max(l,key=lambda x:(x[-1],x[1],x[2],x[3]))[0])
