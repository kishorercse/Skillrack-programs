"""
The program must accept an integer matrix of size R*C as the input. For each column in the matrix, the program must remove the digits at the end of integers so that the number of 
digits in all the integers are equal to the number of digits in the smallest integer in that column. Then the program must print the revised matrix and its sum as the output. 

Boundary Condition(s): 
2 <= R, C <= 50 
1 <= Matrix element value <= 10^5 

Input Format: 
The first line contains R and C separated by a space. 
The next R lines, each contains C integers separated by a space. 

Output Format:
The first R lines, each contains C integers separated by a space representing the revised matrix. 
The R+1st line contains an integer representing the sum of integers in the revised matrix. 

Example Input/Output 1:
Input: 
3 3 
12 500 26
6 812 657
498 458 32 

Output: 
1 500 26
6 812 65
4 458 32
1904 

Explanation:
1st column -> Smallest integer 6 -> 1 digit.
2nd column -> Smallest integer 458 -> 3 digits. 
3rd column -> Smallest integer 26 -> 2 digits. 
After removing the digits of integers based on the given conditions, the matrix becomes 
1 500 26 
6 812 65 
4 458 32 
The sum of integers in the revised matrix is 1904. 

Example Input/Output 2: 
Input: 
3 5
8230 106 38005 79 3 
847 1377 1 450 3
47 3347 655 76 341 

Output: 
82 106 3 79 3 
84 137 1 45 3 
47 334 6 76 3 
1009
"""
r,c=map(int,input().split())
m=[input().split() for _ in range(r)]
s=0
for j in range(c):
    mn=10
    for i in range(r):
        mn=min(len(m[i][j]),mn)
    for i in range(r):
        m[i][j]=int(m[i][j][:mn])
        s+=m[i][j]
for i in m:
    print(*i)
print(s)
