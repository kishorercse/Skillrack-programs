"""
In the amusement park at Jooneys amusement, there is a Weighted Maze challenge. This consist of a set of East West roads and North South roads (referred to as up down roads). 
There are N intersections and each intersection has a block of iron bar, the weight of which is given. You enter the maze at the top left corner. The exit from the maze is at
the bottom right corner. Movement at any intersection is to the right or down provided a road exists in that direction. At each Intersection you pass through, you must exchange 
the weight in your cart with the weight of the bar at the intersection if it is heavier than the weight in you have in the cart. 
The objective is to determine a path through the maze along the roads so that one can exit the maze with the minimum weight in the cart. 

Boundary Condition(s): 
2 <= N <= 100

Input Format: 
The first line contains the number of intersections N. 

Output Format: 
The first line contains the minimum weight in the cart at the exit.

Example Input/Output 1: 
Input:
4
1,8,21,7
19,17,10,20
2,18,23,22
14,25,4,13

Output: 
22 
Example Input/Output 2: 
Input:
5
1,69,51,68,19 
98,92,100,77,54 
8,32,73,31,71 
55,68,98,41,42 
35,70,16,57,60 

Output:
71
"""
n=int(input())
m=[list(map(int,input().split(','))) for _ in range(n)]
for i in range(1,n):
    m[0][i]=max(m[0][i],m[0][i-1])
    m[i][0]=max(m[i][0],m[i-1][0])
for i in range(1,n):
    for j in range(1,n):
        m[i][j]=max(min(m[i-1][j],m[i][j-1]),m[i][j])
print(m[-1][-1])
