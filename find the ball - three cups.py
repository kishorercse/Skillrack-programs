"""
There are three cups on a table, at the positions 1, 2 and 3. Initially, there is a ball hidden under the cup at the position P.
The program must accept N pairs of integers and the value of P as the input. Each pair (X, Y) represents the positions of two cups to be swapped.
After performing N swaps on the three cups, the program must print the position of the ball as the output.

Boundary Condition(s):
1 <= N <= 1000
1 <= P,X,Y <=3

Input Format:
The first line contains N and P separated by a space.
The next N lines, each contains a pair (X, Y) represents the positions of two cups to be swapped.

Output Format: 
The first line contains the position of the ball after performing N swaps on the three cups. 

Example Input/Output 1: 
Input: 
4 2 
1 2 
3 1 
1 2
3 1 

Output: 
1 
Explanation: 
Initially, the ball is present at the position 2. 
After 1st swap (1, 2), the position of the ball becomes 1. 
After 2nd swap (3, 1), the position of the ball becomes 3. 
After 3rd swap (1, 2), the ball remains in the same position 3. 
After 4th swap (3, 1), the position of the ball becomes 1. 

Example Input/Output 2: 
Input: 
4 3 
2 1 
3 1 
3 2 
2 1 
Output: 
2
"""
n,p=map(int,input().split())
t=[0,1,2,3]
while n>0:
    x,y=map(int,input().split())
    t[x],t[y]=t[y],t[x]
    n-=1
print(t.index(p))
