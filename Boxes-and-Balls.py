"""
There are N boxes and N balls on a table. Each box can hold a maximum of one ball only if the size of the ball is less than the size of the box. The size of each box and the
size of each ball are passed as the input. The program must print YES if all N balls fit into N boxes. Else the program must print NO as the output.

Boundary Condition(s):
1 <= N <= 100
1 <= Size of each box and ball <= 10^5

Input Format:
The first line contains N.
The second line contains N integers representing the size of the N boxes separated by a space.
The third line contains N integers representing the size of the N balls separated by a space.

Output Format:
The first line contains YES or NO.

Example Input/Output 1:
Input:
5
5 6 9 8 7
3 2 1 7 8

Output:
YES

Explanation:
One of the possible ways to keep the 5 balls in the 5 boxes is given below.
box 5 - ball 1
box 6 - ball 2
box 9 - ball 8
box 8 - ball 7
box 7 - ball 3

Example Input/Output 2:
Input:
5
5 6 9 8 7
4 7 2 7 8

Output:
NO
"""
n=int(input())
box=sorted(map(int,input().split()))
ball=sorted(map(int,input().split()))
if all(ball[i]<box[i] for i in range(n)):
    print("YES")
else:
    print("NO")
