"""
A mini bus having S seats can be overbooked during festival times. Out of N bookings made C bookings can be cancelled. Hence the final travelling list has to be prepared for 
the first S bookings considering the cancellations. Each booking is assigned a PNR. Given the list of PNRs for all the bookings, the program must print the final list of PNRs 
for the confirmed bookings after cancellation. (The first S bookings remaining after cancellation are considered confirmed)

Input Format:
The first line contains S and N separated by a space.
Next N lines contain the PNRs of the N bookings made.
N+2 th line contains C
Next C lines contain the PNRs of the C bookings cancelled.

Output Format:
S lines contain the PNRs of the confirmed bookings.

Boundary Conditions:
5 <= S <= 30
2 <= N <= 50
N-C > 0
Length of PNR is from 1 to 20

Example Input/Output 1:
Input:
8 10
Q78QJ
BKT6V
32KEW
ETDZI
EH16B
UVZFS
V3ITC
WGGLO
41VJ8
NVIRB
2
UVZFS
BKT6V

Output:
Q78QJ
32KEW
ETDZI
EH16B
V3ITC
WGGLO
41VJ8
NVIRB
"""
s,n=map(int,input().split())
arr=[input().strip() for _ in range(n)]
c=int(input())
for _ in range(c):
    arr.remove(input().strip())
print(*arr[:s],sep='\n')
