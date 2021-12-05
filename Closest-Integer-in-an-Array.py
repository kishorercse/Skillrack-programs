"""
An array of N positive integers are passed as the input. The program must print the closest integer in the array for each integer. If more than one integers are equidistant 
then print the larger integer.

Boundary Condition(s):
2 <= N <= 50
1 <= Each integer value <= 1000

Input Format:
The first line contains N.

Output Format:
The first line contains N integers based on the given condition.

Example Input/Output 1:
Input:
5
100 50 12 60 55

Output:
60 55 50 55 60

Explanation:
The closest integer of 100 is 60.
The closest integer of 50 is 55.
The closest integer of 12 is 50.
The closest integer of 60 is 55.
The closest integer of 55 has two equidistant integers 50 and 60, 60 is the larger integer so 60 is printed as the output.
Hence the output is 60 55 50 55 60

Example Input/Output 2:
Input:
9
5 8 9 7 1 2 4 3 6

Output:
6 9 8 8 2 3 5 4 7

Example Input/Output 3:
Input:
6
10 267 3893 63 438 2

Output:
2 438 438 10 267 10
"""
n=int(input())
l=list(map(int,input().split()))
a=sorted(l)
d={}
d[a[0]]=a[1]
d[a[-1]]=a[-2]
for i in range(1,n-1):
    if (a[i]-a[i-1])<(a[i+1]-a[i]):
        d[a[i]]=a[i-1]
    else:
        d[a[i]]=a[i+1]
for i in range(n):
    print(d[l[i]],end=' ')
