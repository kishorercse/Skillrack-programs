"""
Given an array of N positive integers, print the integer having the least number of factors.

Note: If multiple numbers have the least factor count, print the largest number among them.

Input Format:
The first line contains N
The second line contains N positive integers, each separated by a space.

Output Format:
The first line contains the integer which has the least number of factors

Boundary Conditions:
1 <= N <= 1000

Example Input/Output 1:
Input:
5
15 12 18 15 10

Output:
15

Example Input/Output 2:
Input:
6
1 7 9 11 19 23

Output:
1
"""
def factorCount(a):
    if a==1:
        return 1
    count=2
    t=int(a**0.5)
    for i in range(2,t+1):
        if a%i==0:
            count+=1
            if a//i!=i:
                count+=1
    return count
n=int(input())
l=list(map(int,input().split()))
minCount=9999
ans=-1
for i in l:
    fact=factorCount(i)
    if fact<minCount:
        minCount=fact
        ans=i
    elif fact==minCount:
        ans=max(i,ans)
print(ans)
