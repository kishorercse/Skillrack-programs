"""
The program must accept N ranges and an integer X as the input. If the value X is present in a range A-B (both exclusive), then the program must divide range into two ranges as
A-X and X-B. Then the program must print the ranges in ascending order based on the start value. If two or more ranges start with the same value, then the program must print
those ranges in ascending order based on the end value.

Boundary Condition(s):
1 <= N <= 100
1 <= A <= B <= 1000
1 <= X <= 1000

Input Format:
The first line contains N.
The second line contains N ranges separated by a space.
The third line contains X.

Output Format:
The lines contain the ranges based on the given conditions.

Example Input/Output 1:
Input:
4
5-15 2-8 12-15 1-20
10

Output:
1-10
2-8
5-10
10-15
10-20
12-15

Explanation:
Here N=4 and X=10.
1st range 5-15 contains 10. So it is divided into two ranges as 5-10 and 10-15.
2nd range 2-8 does not contain 10.
3rd range 12-15 does not contain 10.
4th range 1-20 contains 10. So it is divided into two ranges as 1-10 and 10-20.
So the obtained ranges are printed in sorted order based on the given conditions.
1-10
2-8
5-10
10-15
10-20
12-15

Example Input/Output 2:
Input:
7
1-20 1-10 17-28 10-20 4-11 9-23 10-15
10

Output:
1-10
1-10
4-10
9-10
10-11
10-15
10-20
10-20
10-23
17-28
"""
n=int(input())
ranges=input().split()
res=[]
x=int(input())
for i in ranges:
    a,b=map(int,i.split('-'))
    if x>a and x<b:
        res.append([a,x])
        res.append([x,b])
    else:
        res.append([a,b])
res.sort(key=lambda x:(x[0],x[1]))
for i in res:
    print(*i,sep='-')
