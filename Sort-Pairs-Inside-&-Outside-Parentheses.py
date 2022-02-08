"""
The program must accept N pairs of integers as the input. One of the two integers in each pair is enclosed within a pair of parentheses. The program must sort the integers that
present inside the parentheses in ascending order and sort the integers that present outside the parentheses in descending order. Finally, the program must print N revised pairs
as the output.

Boundary Condition(s):
2 <= N <= 100
1 <= Each integer value <= 10^5

Input Format:
The first line contains N.
The second line contains N pairs of integers separated by a space.

Output Format:
The first line contains the revised N pairs of integers separated by a space.

Example Input/Output 1:
Input:
4
12(52) (25)50 (35)10 44(60)

Output:
50(25) (35)44 (52)12 10(60)

Explanation:
Here N = 4.
The 4 integers that present inside the parentheses are 52, 25, 35 and 60.
The 4 integers that present outside the parentheses are 12, 50, 10 and 44.
After sorting those integers in the pairs based on the given conditions, the pairs become
50(25) (35)44 (52)12 10(60)

Example Input/Output 2:
Input:
3
626(564) (343)752 (179)99

Output:
752(179) (343)626 (564)99
"""
n=int(input())
l=input().split()
out=[]
inn=[]
par_pos=[0]*n
ind=0
for i in l:
    a=''
    for j in i:
        if j==')':
            inn.append(int(a))
            a=''
        elif j=='(': 
            if a:
                out.append(int(a))
                a=''
        else:
            a+=j
    if a:
        out.append(int(a))
        par_pos[ind]=1
    else:
        par_pos[ind]=2
    ind+=1
inn.sort() 
out.sort(reverse=True)
for i in range(n):
    if par_pos[i]==2:
        print(out[i],inn[i],sep='(',end=') ')
    else:
        print('(',end='')
        print(inn[i],out[i],sep=')',end=' ')
