"""
There are several cubes placed in N stacks. Each cube has a number K (where K is from 1 to 99) printed on all the sides. Each of these N stacks can have only the top most cube 
removed. The program must find the maximum possible sum of numbers S appearing on the cubes left in a stack, so that S is same for each of the N stacks. The top of the stack 
has the first number in the input line for that specific stack.

Input Format:
The first line will contain N.
The second line will contain the count of cubes in stack 1, say C1.
The third line will contain the numbers appearing on C1 cubes with each number separated by a space.
The pattern of second and third line repeated as the input for the remaining N-1 stacks.

Output Format:
The first line will contain the maximum possible sum S of the numbers left in the stack where S is equal for all stacks.

Boundary Conditions:
3 <= N <= 10
2 <= Ci <= 100 (Count of cubes in each stack)

Example Input/Output 1:
Input:
3
5
6 2 1 1 1
3
4 3 2
4
3 5 4 1

Output:
5

Explanation:
There are 3 stacks.
Stack 1 contains 5 cubes having numbers 6 2 1 1 1. (Top of the stack has 6).
Stack 2 contains 3 cubes having numbers 4 3 2.
Stack 3 contains 4 cubes having numbers 3 5 4 1.
Now when we remove 6 from stack 1 we have 2 1 1 1 and sum=5.
When we remove 4 from stack 2 we have 3 2 and sum=5.
When we remove 3 and 5 from stack 3, we have 4 1 and sum=5.
So here the maximum possible sum is 5.

Example Input/Output 2:
Input:
3
2
6 2
3
4 3 2
2
12 4

Output:
0
"""
n=int(input())
d={}
for _ in range(n):
    t=int(input())
    l=list(map(int,input().split()))
    d[l[t-1]]=d.get(l[t-1],0)+1
    for i in range(t-2,-1,-1):
        l[i]+=l[i+1]
        d[l[i]]=d.get(l[i],0)+1
mx=0
for i in d:
    if d[i]==n and i>mx:
        mx=i
print(mx)
