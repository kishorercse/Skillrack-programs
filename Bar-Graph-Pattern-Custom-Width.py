"""
The program must accept N integers representing the height of bars in a bar graph. The program must print the bar graph using asterisks(bars) and hyphens(empty spaces) as shown in
the Example Input/Output section. The width of each bar in the graph must be equal to X. The value of X is also passed as the input. 

Boundary Condition(s): 
1 <= N <= 100 
1 <= Height of each bar <= 100 
1 <= X <= 10 

Input Format: 
The first line contains N. 
The second line contains N integers separated by a space. 
The third line contains X. 

Output Format: 
The lines contain the bar graph pattern as shown in the Example Input/Output section.

Example Input/Output 1:
Input:
6
4 5 8 3 2 4 
3 

Output: 
------***--------- 
------***--------- 
------***--------- 
---******--------- 
*********------*** 
************---*** 
****************** 
****************** 

Explanation: 
There are 6 bars in the graph and their heights are 4 5 8 3 2 4. 
The width of each bar is 3.

Example Input/Output 2: 
Input:
6
5 4 8 3 1 4 
2 

Output: 
----**------ 
----**------ 
----**------ 
**--**------ 
******----** 
********--** 
********--** 
************ 
"""
n=int(input())
l=list(map(int,input().split()))
x=int(input())
mx=max(l)
for i in range(mx-1,-1,-1):
    for j in range(n*x):
        t=j//x
        if i<l[t]:
            print('*',end='')
        else:
            print('-',end='')
    print()
