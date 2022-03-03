"""
The program must accept an array of N integers as the input. The program must print the output based on the following conditions.
- For each integer X in the array, the program must decrement the value of X by the size of the array.
- Then the program must remove 0s and negative integers from the revised array.
- Then the program must print all the integers in the revised array only if the size is greater than 0.
- Then the program must repeat the above three processes till the size of the array becomes 0.

Note: There will be at least one integer greater than N in the given array.

Boundary Condition(s):
1 <= N <= 100
1 <= Each integer value <= 10^4

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The lines contain the integer values based on the given conditions.

Example Input/Output 1:
Input:
6
24 23 14 21 20 15

Output:
18 17 8 15 14 9
12 11 2 9 8 3
6 5 3 2
2 1

Explanation:
Initially, the size of the array is 6.
At t = 1: 18 17 8 15 14 9

At t = 2: 12 11 2 9 8 3

At t = 3: 6 5 -4 3 2 -3 => 6 5 3 2 (negative integers are removed)
Now the size of the array becomes 4.

At t = 4: 2 1 -1 -2 => 2 1 (negative integers are removed)
Now the size of the array becomes 2.

At t = 5: 0 -1 (zero and negative integer are removed)
Now the size of the array becomes 0.

Example Input/Output 2:
Input:
9
10 18 12 17 13 14 21 22 11

Output:
1 9 3 8 4 5 12 13 2
3 4
1 2

Example Input/Output 3:
Input:
2
15 16

Output:
13 14
11 12
9 10
7 8
5 6
3 4
1 2
"""
n=int(input())
l=list(map(int,input().split()))
t=n
while t>0:
    prev=t
    for i in range(n):
        if l[i]>0:
            l[i]-=prev
            if l[i]<=0:
                t-=1
            else:
                print(l[i],end=' ')
    if t>0:
        print()
