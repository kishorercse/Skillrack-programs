"""
Celine is training her dog to participate in a jumping show where the barricades height differ randomly. As the barricades are inclined, if the dog jumps X feet, it will be
dragged down by Y feet due to it's body weight until it balances and jumps again. Every day she trains her dogs to jump N such barricades.

Help Celine by complete the program below which calculates the minimum number of jumps the dog needs to jump the barricades for D days.

Input Format:
The first line contains the value of D, which denotes the number of days the dog is trained.
For each day, the first line contains the values of X, Y and N, with the values separated by a space and the second line contains the height of the N barricades separated by a 
space.

Output Format:
D lines containing the minimum jump required by the dog on each day from 1 to D.

Boundary Conditions:
2 <= D <= 15
1 <= N <= 20
X > Y

Example Input/Output 1:
Input:
2
10 2 4
5 14 19 22
4 1 5
6 9 11 4 6

Output:
9
12

Explanation:
The dog has been trained for 2 days.
First Day:
X = 10, Y=2 and N - the number of barricades is 4.
So to jump first barricade of height 5 feet, it needs just 1 jump.
To jump second barricade of height 14 feet, it needs 2 jumps.
To jump third barricade of height 19 feet, it needs 3 jumps. (After first jump it is at 10-2 = 8 feet, second jump it is at 8+10-2 = 16 feet and in third it crossed the 
barricade).
To jump fourth barricade of height 22 feet, it needs 3 jumps.
Hence a total of 1+2+3+3 = 9 jumps are needed which is the output for Day 1.
Similarly for the second day, the number of jumps required is 12.
"""
d=int(input())
for _ in range(d):
    x,y,n=map(int,input().split())
    heights=list(map(int,input().split()))
    jumps=0
    t=x-y
    for i in heights:
        p=max(0,i-x)
        jumps+=p//t+(p%t!=0)+1
    print(jumps)
