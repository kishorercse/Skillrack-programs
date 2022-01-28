"""
In a flower garden, people can book tickets to visit the garden. Each ticket has two numbers X and Y, where X represents the ticket number and Y represents the slot number. The
program must accept N pairs of integers representing the tickets of N people. The program must sort the tickets based on the slot number. If two or more tickets are in the same
slot, then the program must sort those tickets based on the ticket number. Finally, the program must print the ticket number and the slot number of the N tickets as the output.

Boundary Condition(s):
1 <= N <= 100
1 <= Ticket Number, Slot Number <= 10^5

Input Format:
The first line contains N.
The next N lines, each contains two integers separated by a space representing the ticket number and the slot number.

Output Format:
The first N lines contain the ticket number and the slot number of the N sorted tickets.

Example Input/Output 1:
Input:
7
3 3
3 1
7 4
4 2
2 3
8 3
2 2

Output:
3 1
2 2
4 2
2 3
3 3
8 3
7 4

Explanation:
Slot 1: Only one ticket 1.
Slot 2: Two tickets 2 and 4.
Slot 3: Three tickets 2, 3 and 8.
Slot 4: Only one ticket 7.
After sorting the tickets based on the slot number and ticket number, the tickets become
3 1
2 2
4 2
2 3
3 3
8 3
7 4

Example Input/Output 2:
Input:
8
40 5
30 2
40 1
30 5
10 2
20 5
10 5
20 2

Output:
40 1
10 2
20 2
30 2
10 5
20 5
30 5
40 5
"""
n=int(input())
l=sorted([list(map(int,input().split())) for _ in range(n)],key=lambda i:(i[-1],i[-2]))
for i in l:
    print(*i)
