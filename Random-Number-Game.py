"""
In a game, there is a machine that generates a random number when a player presses a button. Initially, a player puts X rupees in the machine and starts the game. He
can press the button N times. If he gets a random number equal to the amount in the machine, then the amount gets doubled. After pressing the button N times, he can
collect the amount from the machine if the amount is doubled at least once. Otherwise, he will lose the amount. The program must accept N integers representing the N
random numbers and the value of X as the input. The program must print the final amount the player gets as the output.

Boundary Condition(s):
1 <= N <= 100
1 <= Each random number, X <= 10^6

Input Format:
The first line contains N.
The second line contains N integers separated by a space representing the N random numbers.
The third line contains X.

Output Format:
The first line contains an integer representing the final amount the player gets.

Example Input/Output 1:
Input:
7
10 2 4 11 15 12 8
2

Output:
16

Explanation:
Here X = 2.
1st random number: 10 != X, so the amount is NOT doubled.
2nd random number: 2 == X, so the amount is doubled (X = 4).
3rd random number: 4 == X, so the amount is doubled (X = 8).
4th random number: 11 != X, so the amount is NOT doubled.
5th random number: 15 != X, so the amount is NOT doubled.
6th random number: 12 != X, so the amount is NOT doubled.
7th random number: 8 == X, so the amount is doubled (X = 16).
After completing the game, the player gets 16 rupees.

Example Input/Output 2:
Input:
6
15 20 50 4 6 10
5

Output:
0
"""
n=int(input())
l=list(map(int,input().split()))
x=int(input())
doubledFlag=False
for i in range(n):
    if l[i]==x:
        x*=2
        doubledFlag=True
if doubledFlag:
    print(x)
else:
    print(0)
