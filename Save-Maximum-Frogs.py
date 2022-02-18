"""
There are N frogs, a snake and a hole in a straight line. The snake is present at 0 and the hole is present at X. All the N frogs are present between the snake and the hole. The
value of X and the positions of N frogs are passed as the input to the program. Every second, a frog can move exactly 1 position to the right, but the snake always moves 1 
position to the right after the frog's movement. If a frog reaches the hole, then it is safe from the snake. If the snake reaches any frog's position, then it eats all the frogs
in that position. The program must print the maximum number of frogs that can be saved from the snake as the output.
Note: The snake never enters into the hole.

Boundary Condition(s):
1 <= N, X <= 10^5
1 <= Position of each frog < X

Input Format:
The first line contains N.
The second line contains N integers separated by a space.
The third line contains X.

Output Format:
The first line contains an integer value representing the maximum number of frogs that can be saved from the snake.

Example Input/Output 1:
Input:
6
4 7 5 8 4 9
10

Output:
3

Explanation:
Here N=6, X=10 and the given 6 integers are 4 7 5 8 4 9.
The maximum number of frogs that can be saved from the snake is 3.
One of the possible ways to save 3 frogs is given below.
At T=0, [S, *, *, *, FF, F, *, F, F, F, H].
At T=1, [*, S, *, *, FF, F, *, F, F, *, HF].
At T=2, [*, *, S, *, FF, F, *, F, *, F, HF].
At T=3, [*, *, *, S, FF, F, *, F, *, *, HFF].
At T=4, [*, *, *, *, S, F, *, *, F, *, HFF].
At T=5, [*, *, *, *, *, S, *, *, *, F, HFF].
At T=6, [*, *, *, *, *, *, S, *, *, *, HFFF].
S indicates the snake.
H indicates the hole.
Each F indicates a frog.
Each * indicates an empty space.

Example Input/Output 2:
Input:
5
2 2 1 2 3
4

Output:
2
"""
n=int(input())
l=list(map(int,input().split()))
x=int(input())
arr=[0]*(x+1)
for i in l:
    arr[i]+=1
snake=1
ind=x-1
while ind>=snake:
    if arr[ind]>0:
        arr[ind]-=1
        arr[x]+=1
        snake+=(x-ind)
    else:
        ind-=1
print(arr[x])
