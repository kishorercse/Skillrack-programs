"""
An array of N numbers is passed as input. The program must print all the LEADERS in the array. A number is a LEADER if it is greater than all the numbers to it's right.

Note: The rightmost number is always a leader.

Input Format:
The first line contains N numbers, each separated by a space.

Output Format:
The first line contains the LEADERS, each separated by a space.

Boundary Conditions:
1 <= N <= 9999

Example Input/Output 1:
Input:
10 17 4 3 5 2

Output:
17 5 2
"""
l=list(map(int,input().split()))
mx=-1
n=len(l)
ans=[]
for i in range(n-1,-1,-1):
    if l[i]>mx:
        mx=l[i]
        ans.insert(0,l[i])
print(*ans)
