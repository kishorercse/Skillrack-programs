"""
In a shop, N items are stacked one above another. Each item has a unique ID. If a customer requests an item, the shopkeeper picks up the items above the requested item and 
delivers the item to the customer. After processing the customer request, the shopkeeper fills the stack with the remaining items in the original order. The program must 
accept N integers representing the IDs of N items from bottom to top. The program also accepts R integers representing the IDs of the items requested by the customers.
The program must print the total number of non-requested items that he has picked from the stack when processing the R requests as the output.

Boundary Condition(s):
1 <= R <= N <= 100
1 <= ID of each item <= 1000

Input Format:
The first line contains N.
The second line contains N integers separated by a space.
The third line contains R.
The fourth line contains R integers separated by a space.

Output Format:
The first line contains an integers representing the total number of non-requested items that he has picked from the stack.

Example Input/Output 1:
Input:
5
10 20 30 40 50
3
20 50 10

Output:
5

Explanation:
Initially, there are 5 items in the stack (10 20 30 40 50).
1st request 20: He picks up the items 50, 40, 30 from the stack and delivers the item 20.
Now there are 4 items in the stack (10 30 40 50).
2nd request 50: He delivers the item 50 which is already on the top.
Now there are 3 items in the stack (10 30 40).
3rd request 10: He picks up the items 30, 40 from the stack and delivers the item 10.
Now there are 2 items in the stack (30 40).
The total number of non-requested items that he has picked from the stack is 5 (3 items in the 1st request and 2 items in the 3rd request).
So 5 is printed as the output.

Example Input/Output 2:
Input:
10
74 29 73 42 55 25 41 32 38 18
6
74 32 55 18 41 29

Output:
20
"""
n=int(input())
stack=list(map(int,input().split()))
r=int(input())
l=list(map(int,input().split()))
non_requested=0
for item in l:
    for ind in range(n):
        if stack[ind]==item:
            stack.pop(ind)
            non_requested+=n-ind-1
            n-=1
            break
print(non_requested)
