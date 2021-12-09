"""
N numbers (A0, A1, A2, ..., AN-1) are passed as input to the program. A positive integer D is also passed as input to the program.
The program must find and print the count C of pairs where Ai + Aj (with i < j) is divisible by D without leaving a remainder.

Input Format:
The first line contains N
The second line contains D
The third line contains the N space separated numbers A0, A1, A2, ..., AN-1

Output Format:
The first line contains the value of C

Boundary Conditions:
2 <= N <= 50
1 <= D <= 1000
1 <= Ai <= 999999


Example Input/Output 1:
Input:
5
3
5 2 1 4 7

Output:
6

Explanation:
The 6 divisible pairs are 5,1 5,4 5,7 2,1 2,4 2,7
"""
n=int(input())
d=int(input())
l=list(map(int,input().split()))
count=0
for i in range(n):
    for j in range(i+1,n):
        if (l[i]+l[j])%d==0:
            count+=1
print(count)
