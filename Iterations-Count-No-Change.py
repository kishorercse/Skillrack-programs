"""
The program must accept N unique integers as the input. The program must print the count of iterations in which no change happens when sorting the given integers in ascending 
using Insertion Sort algorithm.

Boundary Condition(s):
2 <= N <= 100
1 <= Each integer value <= 10^5

Input Format:
The first line contains N.
The second line contains N integers.

Output Format:
The first line contains an integer.

Example Input/Output 1:
Input:
8
5 4 3 10 12 2 6 7

Output:
2

Explanation:
The given 8 integers are 5 4 3 10 12 2 6 7.
The 7 iterations in the Insertion Sort algorithm are given below.
After the 1st iteration, the integers become 4 5 3 10 12 2 6 7.
After the 2nd iteration, the integers become 3 4 5 10 12 2 6 7.
After the 3rd iteration, the integers become 3 4 5 10 12 2 6 7.
After the 4th iteration, the integers become 3 4 5 10 12 2 6 7.
After the 5th iteration, the integers become 2 3 4 5 10 12 6 7.
After the 6th iteration, the integers become 2 3 4 5 6 10 12 7.
After the 7th iteration, the integers become 2 3 4 5 6 7 10 12.

Example Input/Output 2:
Input:
5
50 10 20 30 40

Output:
0

Example Input/Output 3:
Input:
6
21 45 78 90 101 150

Output:
5
"""
n=int(input())
l=list(map(int,input().split()))
count=0
for i in range(1,n):
    key=l[i]
    j=i-1
    flag=False
    while j>=0 and key<l[j]:
        l[j+1]=l[j]
        j-=1
        flag=True
    if not flag:
        count+=1
    else:
        l[j+1]=key
print(count)
