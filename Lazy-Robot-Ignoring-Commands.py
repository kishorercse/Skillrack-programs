"""
In a straight line, a robot is placed at position 0 (i.e., at the time t=0, the robot is placed at 0). The robot receives N moving commands. Each command contains two
integers T and X, where T represents the time in which the robot receives the command and X represents the destination point on the straight line. If the robot 
receives a command, it starts moving towards the destination point X with the speed of 1 unit per second and it stops when it reaches the destination point. The 
robot ignores the commands when it is moving. The N commands are passed as the input to the program. The program must print the number of commands ignored by the
robot as the output. Then the program must print the position of the robot after processing the N commands.

Note: All commands are always given in chronological order based on the time T.

Boundary Condition(s):
1 <= N <= 100
1 <= T <= 10^4
-100 <= X <= 100

Input Format:
The first line contains N.
The next N lines, each contains two integers separated by a space representing the values of T and X.

Output Format:
The first line contains an integer representing the number of commands ignored by the robot.
The second line contains an integer representing the final position of the robot.

Example Input/Output 1:
Input:
3
1 5
2 4
6 1

Output:
1
1

Explanation:
At t=0, the position of the robot is 0.
At t=1, the robot receives the 1st command and its position is 0.
At t=2, the position of the robot is 1 (The 2nd command is ignored by the robot as it is moving).
At t=3, the position of the robot is 2.
At t=4, the position of the robot is 3.
At t=5, the position of the robot is 4.
At t=6, the position of the robot is 5 and it receives the 3rd command.
At t=7, the position of the robot is 4.
At t=8, the position of the robot is 3.
At t=9, the position of the robot is 2.
At t=10, the position of the robot is 1.
Only one command is ignored by the robot. So 1 is printed in the first line.
The final position of the robot is 1. So 1 is printed in the second line.

Example Input/Output 2:
Input:
6
1 -5
2 4
3 5
4 0
7 6
10 1

Output:
4
6
"""
n=int(input())
time=1
pos=ignored=0
for _ in range(n):
    t,x=map(int,input().split())
    if t>=time:
        time+= (t-time) + abs(pos-x)
        pos=x
    else:
        ignored+=1
print(ignored)
print(pos)
