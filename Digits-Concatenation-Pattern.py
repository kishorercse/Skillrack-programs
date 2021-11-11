"""
The program must accept an integer N as the input. For each digit D in the integer N (except the last digit), the program must print the output based on the following conditions. 
- If D is a non-zero digit, the program must form an integer by concatenating the all the digits of N after D for D times and print it as the output.
- if D is 0, the program does not print anything. 

Boundary Condition(s):
10 <= N <= 10^8 

Input Format:
The first line contains N. 

Output Format: 
The lines contain the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1: 
Input:
18745

Output:
8745 
745745745745745745745745 
45454545454545 
5555 

Example Input/Output 2:
Input:
200501

Output:
50100501 
101010101

Example Input/Output 3: 
Input:
1000 

Output:
0
"""
n=input().strip()
l=len(n)
flag=False
for i in range(l):
    if n[i]!='0':
        if flag:
            print()
        s=n[i+1:]*int(n[i])
        if s:
            print(int(s),end='')
        flag=True
