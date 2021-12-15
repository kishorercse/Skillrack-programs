"""
Policeman1 and Policeman2 along with a thief are standing on X-axis. The integral value of their location on the X-axis is passed as the input.
Both the policemen run at the same speed and they start running at the same time to catch the thief.
- The program must print Police1 if Policeman1 will catch the thief first.
- The program must print Police2 if Policeman2 will catch the thief first.
- The program must print Both if Policeman1 and Policeman2 will reach the thief at the same time.

Input Format:
The first line will contain the value of N which represents the number of test cases to be passed as the input.
Next N lines will contain the integral location of Policeman1, Policeman2 and the thief each separated by a space.

Output Format:
The first line will contain one of the following values - Police1, Police2, Both

Constraints:
1 <= N <= 20

Example Input/Output 1:
Input:
3
1 2 3
1 3 2
2 1 3

Output:
Police2
Both
Police1

Example Input/Output 1:
Input:
2
-2 2 0
10 5 -1

Output:
Both
Police2
"""
n=int(input())
while n>0:
    p1,p2,t=map(int,input().split())
    a=abs(p1-t)
    b=abs(p2-t)
    if a<b:
        print("Police1")
    elif b<a:
        print("Police2")
    else:
        print("Both")
    n-=1
