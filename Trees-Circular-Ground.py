"""
There are N trees planted circularly in a ground. Every day, the gardener will cut down X trees circularly so that the height of each tree will be reduced by 1. Similarly, each 
tree will grow, thus increasing the height by 1 each day (The trees cut down by the gardener will not grow on that day). If the height of a tree is 1, then he cannot cut down the
tree even if it is present in the X trees that he wants to cut down. The program must accept N integers representing the height of N trees and the value of X as the input. The 
program must print the height of the N trees after T days. The value of T is also passed as the input to the program.

Boundary Condition(s): 
1 <= X <= N <= 100
1 <= T <= 100 

Input Format:
The first line contains N.
The second line contains N integers separated by a space.
The third line contains X and T separated by a space. 

Output Format:
The first line contains the height of the N trees after T days separated by a space. 

Example Input/Output 1:
Input: 
5
10 7 5 8 6 
3 4 

Output: 
8 5 5 8 6 

Explanation: 
Here X = 3 and T = 4. 
Initially, the height of the 5 trees are 10 7 5 8 6. 
After day 1, the height of the 5 trees become 9 6 4 9 7. 
After day 2, the height of the 5 trees become 8 7 5 8 6. 
After day 3, the height of the 5 trees become 9 6 4 7 7. 
After day 4, the height of the 5 trees become 8 5 5 8 6. 

Example Input/Output 2:
Input: 
8
8 2 4 1 9 8 8 7
5 7 

Output:
5 1 1 2 8 7 7 6 

Example Input/Output 3:
Input:
3 
4 2 7
3 3

Output:
1 1 4
"""
n=int(input())
l=list(map(int,input().split()))
x,t=map(int,input().split())
index=0
while t>0:
    for i in range(x):
        if l[index]>1:
            l[index]-=1
        index=(index+1)%n
    other=index
    for i in range(n-x):
        l[other]+=1
        other=(other+1)%n
    t-=1
print(*l)
