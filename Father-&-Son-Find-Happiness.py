"""
There is a family consisting of a father-son. Every day, the father gives his son a certain number of chocolates. The son will be happy or fine or sad depending on the number 
of chocolates the father gives. Every day, the son updates the records of maximum (X) and minimum (Y) chocolates that the father gives. He gets happy only when his father gives
more than X chocolates and gets sad only when his father gives less than Y chocolates. Otherwise, he will be fine.

The program must accept N integers, which represent the number of chocolates the father gives to his son in N days. The program must print the number of days the boy is happy H,
the number of days the boy is fine F, and the number of days the boy is sad S as the output.

Boundary Condition(s):
1 <= N <= 100
1 <= Each integer value <= 10^5

Input Format:
The first line contains N.
The second line contains N integers separated by a space representing the number of chocolates the father gives to his son in N days.

Output Format:
The first line contains H, F and S separated by a space.

Example Input/Output 1:
Input:
9
15 10 25 25 9 10 7 30 6

Output:
2 3 4

Explanation:
1st day - Fine (Always fine on the 1st day)
2nd day - Sad (10 < 15)
3rd day - Happy (25 > 15)
4th day - Fine
5th day - Sad (9 < 10)
6th day - Fine
7th day - Sad (7 < 9)
8th day - Happy (30 > 25)
9th day - Sad (6 < 7)
Happy = 2 days, Fine = 3 days and Sad = 4 days.
Hence the output is
2 3 4

Example Input/Output 2:
10
14 40 31 50 72 59 86 23 9 29

Output:
4 5 1
"""
n=int(input())
l=list(map(int,input().split()))
happy=sad=0
fine=1
mx=l[0]
mn=l[0]
for i in range(1,n):
    if l[i]>mx:
        mx=l[i]
        happy+=1
    elif l[i]<mn:
        mn=l[i]
        sad+=1
    else:
        fine+=1
print(happy,fine,sad)
