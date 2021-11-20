"""
The program must accept an integer matrix of size RxC as the input. The program must print YES if the number of odd integers in each column of the matrix is same. Else the program
must print NO as the output.

Boundary Condition(s):
2 <= R, C <= 50 
1 <= Matrix element value <= 1000

Input Format: 
The first line contains R and C separated by a space. 
The next R lines, each containing C integers separated by a space. 

Output Format: 
The first line contains YES or NO. 

Example Input/Output 1: 
Input: 
5 4
11 23 20 41 
40 36 35 68 
19 30 43 44 
44 45 22 44 
26 42 10 29

Output:
YES

Explanation:
Each column of the matrix contains exactly 2 odd integers. So YES is printed as the output. 

Example Input/Output 2: 
Input: 
4 7
4 6 4 3 9 9 2
5 8 5 9 2 7 3
6 9 6 7 5 8 8
3 3 7 7 6 9 4

Output:
NO
"""
r,c=map(int,input().split())
m=[list(map(int,input().split())) for _ in range(r)]
common=-1
for j in range(c):
    count=0
    for i in range(r):
        if m[i][j]%2!=0:
            count+=1
    if common==-1:
        common=count
    if count!=common:
        print("NO")
        break
else:
    print("YES")
