"""
The program must accept an array of N distinct integers as the input. The program must print the absolute difference between X and Y as the output. The integer X represents the
sum of integers whose positions are not changed in the array when sorted in ascending order. The integer Y represents the sum of integers whose positions are changed in the 
array when sorted in ascending order.

Boundary Condition(s):
1 <= N <= 1000
1 <= Each integer value <= 10^5

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains an integer representing the absolute difference between X and Y.

Example Input/Output 1:
Input:
8
60 10 70 40 50 20 30 80

Output:
20

Explanation:
After sorting the given 8 integers in ascending order, the integers become
10 20 30 40 50 60 70 80
X = 40 + 50 + 80 = 170.
Y = 60 + 10 + 70 + 20 + 30 = 190.
The absolute difference between X and Y is 20, which is printed as the output.

Example Input/Output 2:
Input:
5
1 2 5 4 3

Output:
1
"""
n=int(input())
l=list(map(int,input().split()))
changed=sum(l)
unchanged=0
t=sorted(l)
for i in range(n):
    if l[i]==t[i]:
        unchanged+=l[i]
        changed-=l[i]
print(abs(unchanged-changed))
