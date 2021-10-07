"""
The program must accept an integer matrix of size R*C, where C is even and swap the unit digits of the elements in columns 1 and 2, then 3 and 4 and so on till columns C-1 and C.
Then the program must print the revised matrix as the output.

Boundary Condition(s):
1 <= R, C <= 100 
1 <= Value of an element in the matrix <= 1000 

Input Format: 
The first line contains R and C separated by space(s).
The next R lines each containing C integer values separated by a space. 

Output Format: 
R lines each containing C integer values separated by a space. 
Example Input/Output 1: 
Input:
3 4 
96 61 138 32
150 67 131 177 
172 103 83 45 

Output: 
91 66 132 38 
157 60 137 171 
173 102 85 43
"""
r,c=map(int,input().split())
for _ in range(r):
    t=input().split()
    for j in range(0,c,2):
        print(t[j][:-1]+t[j+1][-1],t[j+1][:-1]+t[j][-1],end=' ')
    print()
