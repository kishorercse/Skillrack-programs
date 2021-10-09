"""
The program must accept an integer N and a character CH as the input. The program must print the desired pattern as shown in the Example Input/Output section. 
Note: The character CH can be D or X. 

Boundary Condition(s): 
1 <= N <= 50

Input Format: 
The first line contains N and CH separated by a space. 

Output Format: 
The lines containing the desired pattern as shown in the Example Input/Output section. 

Example Input/Output 1:
Input:
1 D 

Ouptut: 
/\ 
\/

Example Input/Output 2: 
Input:
2 X 

Ouptut: 
\/\/ 
/\/\ 
\/\/
/\/\ 

Example Input/Output 3: 
Input: 
4 D 

Output: 
/\/\/\/\ 
\/\/\/\/ 
/\/\/\/\
\/\/\/\/ 
/\/\/\/\
\/\/\/\/
/\/\/\/\ 
\/\/\/\/ 

Example Input/Output 4:
Input:
4 X 

Output:
\/\/\/\/
/\/\/\/\
\/\/\/\/
/\/\/\/\
\/\/\/\/
/\/\/\/\
\/\/\/\/
/\/\/\/\
"""
n,ch=input().split()
n=int(n)
a='/\\'
b='\\/'
if ch=='X':
    a,b=b,a
for i in range(n*2):
    if i%2==0:
        print(a*n)
    else:
        print(b*n)
