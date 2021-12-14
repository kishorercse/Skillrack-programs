"""
A shop to increase sales during a festival has an offer that a customer will get a discount if the customer buys shirts having same size in pairs. Any customer who buys will
choose N shirts and the size of the shirt is denoted by S(i) where 1 <= i <=N. Two shirts S(i) and S(j) are matching and form a pair only if S(i) = S(j).

The program must print the number of pairs eligible for the discount.

Input Format:
The first line will contain the value of N
The second line will contain the the size of N shirts S(1) to S(N) with each size separated by a space.

Output Format:
The first line will contain the number of matching pairs eligible for the discount.

Constraints:
2 <= N <= 100

Example Input/Output 1:
Input:
9
10 20 20 10 10 30 44 10 20

Output:
3

Explanation:
The matching pairs are (10,10) (20,20) (10,10).


Example Input/Output 2:
Input:
6
42 44 40 42 44 42

Output:
2

Explanation:
The matching pairs are (42,42) (44,44)
"""
n=int(input())
l=list(map(int,input().split()))
d={}
pairs=0
for i in l:
    d[i]=d.get(i,0)+1
    if d[i]==2:
        pairs+=1
        d[i]=0
print(pairs)
