"""
The program must accept N integers as the input. The program must print the maximum possible odd sum from the given N integers as the output. If it is not possible to find the 
odd sum from the given N integers, then the program must print -1 as the output.

Boundary Condition(s):
1 <= N <= 100
1 <= Each integer value <= 10^7

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains an integer value representing the maximum possible odd sum or -1.

Example Input/Output 1:
Input:
7
2 7 5 1 6 3 4

Output:
27

Explanation:
The maximum possible odd sum is 27, which is obtained by adding 2, 7, 5, 6, 3 and 4.

Example Input/Output 2:
Input:
4
16 24 70 58

Output:
-1

Example Input/Output 3:
Input:
8
33 43 37 43 23 31 10 49

Output:
269
"""
n=int(input())
l=list(map(int,input().split()))
total=0
minOdd=99999999999
for i in l:
    total+=i
    if i%2!=0 and i<minOdd:
        minOdd=i
if total%2!=0:
    print(total)
else:
    if minOdd!=99999999999:
        print(total-minOdd)
    else:
        print(-1)
