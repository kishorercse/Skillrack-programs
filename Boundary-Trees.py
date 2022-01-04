"""
Certain trees are planted in R rows and C columns in a rectangular field. The current height of the trees are passed as the input. In a month, each tree normally grows by N inches.
But the trees on the edge of the rectangular field can grow double the normal rate as they get more sunlight when compared to other trees.

The program must print the height of the trees after M months.

Input Format:
The first line contains the values of R and C separated by a space.
Next R lines will contain C values each which represents the current height of the trees, with the values separated by a space.
The next line will contain the value of N (the normal growth rate) and M (the number of months) separated by a space.

Output Format:
R lines will contain C values each representing the height of the trees after M months.

Boundary Conditions:
1 <= R, C <= 20
1 <= N <= 100
1 <= M <= 12

Example Input/Output 1:
Input:
4 3
5 3 6
9 4 10
7 8 7
8 9 9
1 3

Output:
11 9 12
15 7 16
13 11 13
14 15 15
"""
