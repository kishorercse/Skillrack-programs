"""
In a village there are N people whose identification numbers are from 1 to N. These villagers team together among themselves to form a certain number of gangs. There may be
some villagers who are not part of any of these gangs. A combination (i,j) where 1 <= i,j <= N indicates that i and j belong to the same gang. C is the number of such 
combinations that are passed as input to the program.

The program must print the size of the gang which has the maximum number of people. 
(People who are not part of any of the gangs are considered as individual gangs whose size is 1)

Input Format:
First line contains N and C separated by a space.
Next C lines contain two identification numbers i and j separated by a space.

Output Format:
First line contains the size of the gang which has the maximum number of people.

Boundary Conditions:
1 <= N <= 100000
1 <= C <= 100000
1 <= i,j <= N in the C lines.

Note:
In a combination (i,j),  i and j can be equal.

Example Input/Output 1:
Input:
5 6
2 2
3 3
1 1
2 3
1 4
3 4

Output:
4

Explanation:
There are 5 people and 6 combinations are provided. So based on the input we have the following gangs.
(2,3,1,4) (5).
Gang (2,3,1,4) is the largest with size as 4.

Example Input/Output 2:
Input:
10 11
1 2
7 8
10 9
10 10
4 4
3 10
8 5
6 5
6 6
9 4
3 2

Output:
6

Explanation:
The largest gang is (1,2,3,10,9,4) whose size is 6.
"""
n,c=map(int,input().split())
gangtopeople={}
peopletogang={}
gang=1
for _ in range(c):
    a,b=map(int,input().split())
    x,y=peopletogang.get(a,-1), peopletogang.get(b,-1)
    if x!=-1 and y!=-1 and x==y:
        continue
    if x!=-1 and y!=-1:
        mx,mn=max(x,y),min(x,y)
        gangtopeople[mn][0]=gangtopeople[mn][0].union(gangtopeople[mx][0])
        gangtopeople[mn][1]+=gangtopeople[mx][1]
        for i in gangtopeople[mx][0]:
            peopletogang[i]=mn
            peopletogang[i]=mn
        del gangtopeople[mx]
    elif x!=-1 or y!=-1:
        t=x
        if x==-1:
            t=y
        gangtopeople[t][0].add(a)
        gangtopeople[t][0].add(b)
        gangtopeople[t][1]+=1
        peopletogang[a]=t
        peopletogang[b]=t
    else:
        if a==b:
            t=1
        else:
            t=2
        gangtopeople[gang]=[set([a,b]),t]
        peopletogang[a]=gang
        peopletogang[b]=gang
        gang+=1
mx=-1
for i in gangtopeople:
    mx=max(gangtopeople[i][1],mx)
print(mx)
