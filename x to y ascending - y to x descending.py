"""

Three positive integers X, Y and Z are passed as the input to the program. The program must print from X to Z in the forward direction and then print from Y to X in the reverse direction.

Boundary Condition(s):
1 <= X < Y < Z <= 1000

Input Format:
The first line contains X, Y and Z separated by a space.

Output Format:
The first line contains the values from X to Z separated by a space.
The second line contains the values from Y to X separated by a space.

Example Input/Output 1:
Input:
5 10 15

Output:
5 6 7 8 9 10 11 12 13 14 15
10 9 8 7 6 5
 
Example Input/Output 2:
Input:
2 5 9

Output:
2 3 4 5 6 7 8 9
5 4 3 2
"""
x,y,z=map(int,input().split())
for i in range(x,z+1):
    print(i,end=' ')
print()
for i in range(y,x-1,-1):
    print(i,end=' ')
