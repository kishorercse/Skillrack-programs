"""
The program must accept N integers and an integer X as the input. The program must sort the first X integers in ascending order among the N integers. Then the program must sort 
the last X integers in descending order among the N modified integers. Finally, the program must print the modified values of N integers as the output. 

Boundary Condition(s): 
3 <= N <= 100 
1 <= Each integer value <= 10^5 
1 <= X <= N 

Input Format:
The first line contains N. 
The second line contains N integers separated by a space.
The third line contains X.

Output Format:
The first line contains the modified values of N integers.

Example Input/Output 1:
Input:
6
87 31 69 28 94 88 
3

Output: 
31 69 87 94 88 28 

Explanation:
After sorting the first 3 integers in ascending order, the integers become 31 69 87 28 94 88 
After sorting the last 3 integers in descending order, the integers become 31 69 87 94 88 28 
Hence the output is 31 69 87 94 88 28 

Example Input/Output 2:
Input:
9
62 81 27 67 69 49 95 23 39
5

Output: 
27 62 67 69 95 81 49 39 23

Explanation:
After sorting the first 5 integers in ascending order, the integers become 27 62 67 69 81 49 95 23 39
After sorting the last 5 integers in descending order, the integers become 27 62 67 69 95 81 49 39 23
Hence the output is 27 62 67 69 95 81 49 39 23
"""
n=int(input())
l=list(map(int,input().split()))
x=int(input())
l[:x]=sorted(l[:x])
l[-x:]=sorted(l[-x:],reverse=True)
print(*l)
