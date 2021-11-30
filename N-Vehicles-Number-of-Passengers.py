"""
The capacity of N vehicles are passed as the input. The program must print the number of passengers who can travel in such a way that the occupied vehicles are filled to their
capacity. The output containing the number of passengers must be sorted.

Boundary Condition(s):
1 <= N <= 10
1 <= Capacity of each vehicle <= 1000

Input Format:
The first line contains N.
The second line contains N integer values separated by a space representing the capacity of N vehicles.

Output Format:
The first line contains the integer values separated by a space representing the number of passengers.

Example Input/Output 1:
Input:
3
5 4 10

Output:
4 5 9 10 14 15 19

Explanation:
When just 1 vehicle alone is used the filled capacity is 4, 5 and 10.
When Vehicle 1 and 2 are filled, the count of passengers is 9.
When Vehicle 1 and 3 are filled, the count of passengers is 15.
Similarly, for Vehicle 2 and 3 it is 14.
When all three vehicles are filled, the count is 19.
The output is these count of passengers sorted in ascending order.

Example Input/Output 2:
Input:
4
14 5 10 20

Output:
5 10 14 15 19 20 24 25 29 30 34 35 39 44 49
"""
from itertools import combinations
n=int(input())
l=sorted(map(int,input().split()))
if n==1:
    print(l[0])
else:
    ans=[]
    for i in range(2,n):
        for i in combinations(l,i):
            ans.append(sum(i))
    print(*sorted(l+ans+[sum(l)]))
