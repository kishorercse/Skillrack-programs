"""
Alisha visits a fruit shop which has N boxes and each box has one or more apples in it. The shop keeper will not allow transfer of apples from one box to another. The number
of apples in each of these N boxes is passed as the input. Suppose Alisha wishes to buy exactly K apples, the program has to print the distinct ways in which Alisha can pick
and buy exactly K apples considering the fact that Alisha's bike can carry only a maximum of 2 boxes.

Input Format:
The first line contains N and K separated by a space.
The second line contains the count of apples C1 to CN in each of the boxes separated by a space.

Output Format:
The first line contains the integer value representing the number of ways in which Alisha can pick boxes to buy exactly K apples.

Boundary Conditions:
2 <= N <= 99999
1 <= K <= 99999
1 <= Ci <= K

Note: Optimize the logic to find the count. Else Timeout will occur.

Example Input/Output 1:
Input:
7 6
1 2 3 4 3 4 2

Output:
2

Explanation:
The combinations 2,4 and 3,3 gives exactly 6.
Please note that 2,4 is same as 4,2.

Example Input/Output 2:
Input:
7 6
6 6 6 6 3 3 3

Output:
2

Explanation:
The distinct combinations are 6 (where only one box is picked) and 3,3
"""
n,k=map(int,input().split())
l=list(map(int,input().split()))
res=set()
for i in range(n):
    if l[i]==k:
        res.add(l[i])
        continue
    for j in range(i+1,n):
        if l[i]+l[j]==k:
            a=min(l[i],l[j])
            b=max(l[i],l[j])
            res.add(str(a)+'+'+str(b))
print(len(res))
