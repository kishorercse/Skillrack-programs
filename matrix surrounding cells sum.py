"""
The program must accept an R*C matrix containing integer values. An integer N is also passed as the input. 
The program must find the first occurrence of N in the matrix and print the sum S of the surrounding integer values. 

Note: The integer N always occurs at least once in the matrix. 

Boundary Condition(s): 

2 <= R, C <= 10 

Input Format: 
The first line contains R and C separated by a space.
Next R lines contain C integer values each. 
The R+2nd line contains the value of N. 

Output Format: 
The first line contains the value of S. 

Example Input/Output 1: 
Input: 
5 4 
1 2 3 4 
6 7 8 9 
1 5 20 3 
5 4 3 2 
6 8 7 4 
20 

Output: 
41 

Explanation: 
Sum = 7+8+9+5+3+4+3+2 = 41. 

Example Input/Output 2: 

Input: 
5 4 
1 2 3 4 
6 7 8 9 
1 5 20 3 
5 4 3 2 
6 8 7 4 
9 
Output: 
38
"""
r,c=map(int,input().split())
m=[input().split() for _ in range(r)]
n=input().strip()
l=[[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
for i in range(r):
    for j in range(c):
        if m[i][j]==n:
            s=0
            for x,y in l:
                a,b=i+x,j+y
                if 0<=a<r and 0<=b<c:
                    s+=int(m[a][b])
            print(s)
            quit()
