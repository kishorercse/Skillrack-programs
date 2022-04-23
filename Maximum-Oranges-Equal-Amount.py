"""
There are N orange trees in a row. The number of oranges in each tree is passed as the input. Hector wants to pluck a maximum number of oranges based on the following
condition.
- He can start collecting oranges from any tree, but once he starts collecting, he must collect an equal amount of oranges from each tree from the tree he started to
the last tree.
The program must print the maximum number of oranges Hector can collect as the output.

Boundary Condition(s):
1 <= N <= 100
1 <= Each integer value <= 1000

Input Format:
The first line contains N.
The second line contains N integer values separated by a space.

Output Format:
The first line contains an integer value representing the maximum number of oranges Hector can collect.

Example Input/Output 1:
Input:
5
4 3 5 2 6

Output:
10

Explanation:
Hector can collect 2 oranges from each tree (from 1st tree to 5th tree).
So he gets 10 oranges.

Example Input/Output 2:
Input:
5
1 3 2 4 6

Output:
8

Explanation:
Hector can collect 2 oranges from each tree (from 2nd tree to 5th tree).
or
Hector can collect 4 oranges from each tree (from 4th tree to 5th tree).
So he gets 8 oranges.

Example Input/Output 3:
Input:
10
5 5 5 5 2 5 5 5 3 21

Output:
21
"""
n=int(input())
l=list(map(int,input().split()))
mx=0
min_value=100000
for i in range(n-1,-1,-1):
    if l[i]<min_value:
        min_value=l[i]
    mx=max(min_value*(n-i),mx)
print(mx)
