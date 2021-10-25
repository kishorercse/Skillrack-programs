"""
The program must accept N arrays of integers of different sizes as the input. The program must print the sum of integers in the longest array as the output. If two or more arrays 
have the same longest length, then consider the array having the maximum sum. Boundary Condition(s): 1 <= N <= 50 1 <= Each integer value <= 10^5 Input Format: The first line 
contains N. The next N lines, each contains integer values separated by a space. Output Format: The first line contains an integer value representing the sum of integers in the 
longest array. 

Example Input/Output 1: 
Input: 
5 
12 10 50 30 
500 800 900 
1 2 3 4 5
10 20 
15 320 5 15

Output: 
15

Explanation:
The longest array among the given 5 arrays is [1 2 3 4 5]. The sum of integers in the array is 15. 

Example Input/Output 2:
Input: 
4 
10 20 30 40 50 
100 200 300 400 500 
11 22 33 44 55 
6 7 8 9 10 

Output:
1500
"""
n=int(input())
max_sum=0
max_size=0
for _ in range(n):
    l=list(map(int,input().split()))
    t=len(l)
    s=sum(l)
    if t>max_size:
        max_size=t
        max_sum=s
    elif t==max_size:
        max_sum=max(s,max_sum)
print(max_sum)
