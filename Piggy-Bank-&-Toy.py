"""
A boy wants to save money to buy a toy. He puts money in his piggy bank every day. Every day, he puts 1 rupee more than the previous day. Every sunday, he starts with a new 
value 1 rupee more than the previous sunday. The cost of the toy is T rupees. The boy already has X rupees in his piggy bank. On the first sunday, he puts Y rupees in his 
piggy bank. The values of T, X and Y are passed as the input to the program. The program must print the number of days he needs to buy the toy as the output.

Boundary Condition(s):
1 <= T <= 10^4
0 <= X < T
1 <= Y <= 100

Input Format:
The first line contains T, X and Y separated by a space.

Output Format:
The first line contains the number of days he needs to buy the toy.

Example Input/Output 1:
Input:
170 50 10

Output:
10

Explanation:
Here T = 170, X = 50 and Y = 10.
Initially, he has 50 rupees in his piggy bank.
Day 1: Sun -> 50 + 10 = 60
Day 2: Mon -> 60 + 11 = 71
Day 3: Tue -> 71 + 12 = 83
Day 4: Wed -> 83 + 13 = 96
Day 5: Thu -> 96 + 14 = 110
Day 6: Fri -> 110 + 15 = 125
Day 7: Sat -> 125 + 16 = 141
Day 8: Sun -> 141 + 11 = 152
Day 9: Mon -> 152 + 12 = 164
Day 10: Tue -> 164 + 13 = 177
After 10 days he can buy the toy. So 10 is printed as the output.

Example Input/Output 2:
Input:
400 298 50

Output:
3

Explanation:
Here T = 400, X = 298 and Y = 50.
Initially, he has 298 rupees in his piggy bank.
Day 1: Sun -> 298 + 50 = 348
Day 2: Mon -> 348 + 51 = 399
Day 3: Tue -> 399 + 52 = 451
After 3 days he can buy the toy. So 3 is printed as the output.
"""
t,x,y=map(int,input().split())
days=0
p=y
while x<t:
    x+=p
    p+=1
    days+=1
    if days%7==0:
        p=y+days//7
print(days)
