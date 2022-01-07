"""
Alok is playing N round of card games with his friend Brinda. He gets postive or negative points based on whether he won or lost in a specific round. Alok can also get zero 
points in case of a tie. Given the points obtained in N rounds, the program must print the maximum sum of points obtained in any of the winning streak sequence.

Input Format:
The first line contains N.
The second line contains the points P(i), i=1 to N with the points separated by a space.

Output Format:
The first line contains M which represents the maximum number of points obtained in any of the winning sequence.

Boundary Conditions:
3 <= N <= 100
-100 <= P(i) <= 100

Example Input/Output 1:
Input:
7
9 2 3 -1 1 2 4

Output:
14

Example Input/Output 2:
Input:
15
11 20 6 7 -4 2 -5 15 8 3 16 8 3 -1 -2

Output:
53
"""
n=int(input())
l=list(map(int,input().split()))
mx=total=0
for i in l:
    if i>0:
        total+=i
    else:
        mx=max(total,mx)
        total=0
mx=max(total,mx)
print(mx)
