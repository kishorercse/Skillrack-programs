"""
N positive integers are passed as the input. The program must print the largest possible differences between N/2 pairs in the descending order as the output.

Boundary Condition(s):
2 <= N <= 50
1 <= Each integer value <= 1000

Input Format:
The first line contains N.

Output Format:
The first line contains the largest possible differences between N/2 pairs in the descending order.

Example Input/Output 1:
Input:
5
100 50 12 60 55

Output:
88 10

Explanation:
The largest difference is possible for 100-12.
Now the remaining values are 50 60 55.
Now the largest possible difference is 60-50.

Example Input/Output 2:
Input:
6
10 20 30 40 50 60

Output:
50 30 10

Example Input/Output 3:
Input:
3
77 98 53

Output:
45
"""
n=int(input())
l=sorted(map(int,input().split()))
i=0
j=n-1
while i<j:
    print(l[j]-l[i],end=' ')
    i+=1
    j-=1
