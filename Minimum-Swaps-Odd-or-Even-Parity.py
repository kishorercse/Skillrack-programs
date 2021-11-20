"""
The program must accept N integers as the input. The program must print the minimum number of swaps required to rearrange the N integers such that the odd integers present in the
odd positions and the even integers present in the even positions. If it is not possible to rearrange the N integers as per the given conditions, the program must print -1 as the 
output.

Boundary Condition(s):
1 <= N <= 10^5
1 <= Each integer value <= 1000 

Input Format: 
The first line contains N. 
The second line contains N integers separated by a space.

Output Format: 
The first line contains an integer representing the minimum number of swaps required to rearrange the N integers as per the given conditions or -1. 

Example Input/Output 1:
Input: 
4
2 3 6 7 

Output:
2 

Explanation: 
In the first swap, 2 and 3 can be swapped. 
In the second swap, 6 and 7 can be swapped.
Now the four integers become 3 2 7 6. 
Here the odd integers present in the odd positions and the even integers present in the even positions. 

Example Input/Output 2:
Input:
3
5 4 8

Output:
-1

Example Input/Output 3: 
Input:
7
1 4 5 10 3 2 9

Output:
0
"""
n=int(input())
l=list(map(int,input().split()))
odd=even=0
for i in range(n):
    if i%2==l[i]%2:
        if i%2==0:
            odd+=1
        else:
            even+=1
if odd==even:
    print(even)
else:
    print(-1)
