/*
The program must accept N integers representing the length of N rods. A boy cuts the rods into smaller rods based on the following conditions.
- He finds the length of the shortest rod. Then he cuts that length from each of the longer rods and then he removes all the pieces of the shortest length. 
When all the remaining rods are the same length, they cannot be shortened so he removes those rods.
- He repeats the above process until there are no rods left.
The program must print the number of rods remaining before each cutting process.

Boundary Condition(s):
1 <= N, Length of each rod <= 1000

Input Format:
The first line contains N.
The second line contains N integers separated by a space representing the length of N rods.

Output Format:
The lines contain the integer values based on the given conditions.

Example Input/Output 1:
Input:
6
8 4 2 2 7 8

Output:
6
4
3
2

Explanation:
Here N = 6 and the lengths of the 6 rods are 8 4 2 2 7 8.
Initially, there are 6 rods.
Shortest length = 2 -> 6 2 * * 5 6
Now 4 rods are remaining.
Shortest length = 2 -> 4 * * * 3 4
Now 3 rods are remaining.
Shortest length = 3 -> 1 * * * * 1
Now 2 rods are remaining. Both the rods have the same length, so he removes them.
The asterisks represent the empty spaces.

Example Input/Output 2:
Input:
9
1 2 3 4 5 4 3 2 1

Output:
9
7
5
3
1
*/
n=int(input())
l=list(map(int,input().split()))
rem=n
mn=min(l)
while rem>0:
    print(rem)
    x=9999
    for i in range(n):
        if l[i] >= mn:
            l[i] -= mn
            if l[i]!=0 and l[i] < x:
                x=l[i]
            if l[i]==0:
                rem-=1
                if rem==0:
                    break
    mn=x
