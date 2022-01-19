"""
A company plans a viral marketing strategy in which an existing customer will invite N other new customers every day for D days. At the end of the Dth day, a customer will get 
a gift and must leave (the left customers will not invite any new customers on D+1 th day). A customer who has got a gift and left will not be invited again. On Day 1 there 
will be only one customer to begin with and this customer will leave at the end of the Dth day. Given N and D, the program must calculate the number of customers who are 
eligible to invite new customers on the Tth day.

Input Format:
The first line will contain N and D separated by a space.
The second line will contain T.

Output Format:
The first line will contain the number of customers who are eligible to invite new customers on the Tth day

Boundary Conditions:
1 <= N <= 5
1 <= D <= 10
1 <= T <= 50

Example Input/Output 1:
Input:
2 6
3

Output:
9

Example Input/Output 2:
Input:
2 6
7

Output:
726

Explanation:
Customers remaining at the end of day 1 is = 3
Customers remaining at the end of day 2 is = 9
Customers remaining at the end of day 3 is = 27
Customers remaining at the end of day 4 is = 81
Customers remaining at the end of day 5 is = 243
Customers remaining at the end of day 6 is = 726 (3 leave)
So customers who can invite on 7th day = 726
"""
n,d=map(int,input().split())
t=int(input())
l=[0,n+1] #Storing number of customers joined on the ith day
ans=l[-1]
for i in range(2,t):
    l.append(ans*n)
    ans=l[-1]+ans
    if i>=d:
        ans-=l[i-d+1]  #Subtracting the customers who joined before d days (not the customers present before d days)
print(ans)
