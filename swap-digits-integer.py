"""
The program must accept an integer N and Q queries as the input. Each query contains two integers X and Y representing
the positions of two digits in the integer N. For each query (X, Y), the program must swap the digits at the specified
positions in the integer N. After Q swaps, if the resulting integer R is equal to the given integer N, then the program
must print "YES". Else the program must print the value of 2*R.

Boundary Condition(s):
10 <= N <= 10^8
1 <= Q <= 50

Input Format:
The first line contains N. 
The second line contains Q. 
The next Q lines contain two integers X and Y representing the positions of two digits in the integer N. 

Output Format: 
The first line contains the string value "YES" or the integer value of 2*R.

Example Input/Output 1: 
Input: 
1234
6
1 3
1 4
2 4
2 3
1 4
1 2 

Output: 
YES 

Explanation: 
Here N = 1234. 
1st swap: 1 3 -> 3214 
2nd swap: 1 4 -> 4213 
3rd swap: 2 4 -> 4312 
4th swap: 2 3 -> 4132 
5th swap: 1 4 -> 2134 
6th swap: 1 2 -> 1234 
After 6 swaps, the resulting integer R = 1234 which is equal to N. 
Hence YES is printed as the output. 

Example Input/Output 2:
Input:
2139 
3
1 3
2 4 
1 4 

Output: 
3846
"""
n=list(input().strip())
q=int(input())
t=list(n)
while q>0:
    x,y=map(int,input().split())
    x-=1
    y-=1
    t[x],t[y]=t[y],t[x]
    q-=1
if t==n:
    print("YES")
else:
    print(2*int(''.join(t)))
