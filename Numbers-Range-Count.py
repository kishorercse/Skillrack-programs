"""
Given N distinct integers, the program must print the number of ranges R present. A range is defined as two or more consecutive integers.

Input Format:
The first line contains N.
The second line contains N integer values separated by a space.

Output Format:
The first line contains R.

Boundary Conditions:
2 <= N <= 100000
1 <= R <= 10000

Example Input/Output 1:
Input:
5
2 1 4 9 3

Output:
1

Explanation:
The only range which is present is 1 2 3 4.
9 is not a range (as a range needs two or more consecutive integers).

Example Input/Output 2:
Input:
7
1 3 11 -15 -20 9 5

Output:
0
"""
n=int(input())
l=sorted(map(int,input().split()))
count=0
a=0
for i in range(n):
    if l[i-1]+1==l[i]:
        a+=1
    else:
        if a>0:
            count+=1
        a=0
if a>0:
    count+=1
print(count)
