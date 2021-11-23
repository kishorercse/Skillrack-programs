"""
There are N houses in a row. A serial killer plans to kill people in these houses. If he targets Xth house, he will kill 2 persons in that house and 1 person from nearby by
houses (left and right). If there is no person in the Xth house, he will not kill any person in the nearby houses. The program must accept N integers representing the number 
of persons in the N houses and M integers representing the positions of the houses he is targeting. The program must print the number of persons remaining in the N houses
after the series of murders as the output.

Boundary Condition(s):
1 <= N <= 100
0 <= Number of persons in each house <= 1000
1 <= M <= 1000

Input Format:
The first line contains N.
The second line contains N integers separated by a space.
The third line contains M.
The fourth line contains M integers separated by a space.

Output Format:
The first line contains the number of persons remaining in the N houses after the series of murders.

Example Input/Output 1:
Input:
5
12 6 8 2 4
3
2 5 4

Output:
11 4 6 0 1

Explanation:
Here N = 5 and the number of persons in the 5 houses are 12 6 8 2 4.
After killing the persons in the 2nd house, the number of persons remaining in the 5 houses are given below.
11 4 7 2 4
(House 2: 2 persons killed, Houses 1 and 3: 1 person killed)
After killing the persons in the 5th house, the number of persons remaining in the 5 houses are given below.
11 4 7 1 2
(House 5: 2 persons killed, House 4: 1 person killed)
After killing the persons in the 4th house, the number of persons remaining in the 5 houses are given below.
11 4 6 0 1
(House 4: 1 person killed, Houses 3 and 5: 1 person killed)

Example Input/Output 2:
Input:
6
2 0 7 5 8 3
4
5 6 2 1

Output:
0 0 7 4 5 0
"""
n=int(input())
h=list(map(int,input().split()))
m=int(input())
l=list(map(int,input().split()))
for p in l:
    p-=1
    if h[p]>0:
        h[p]=max(h[p]-2,0)
        if p>=1:
            h[p-1]=max(h[p-1]-1,0)
        if p<n-1:
            h[p+1]=max(h[p+1]-1,0)
print(*h)
