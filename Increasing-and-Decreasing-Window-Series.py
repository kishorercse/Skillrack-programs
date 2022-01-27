"""
The program must accept two integers N and K as the input. The program must generate a series as given below and print the Kth term as the output.
1 to N, 2*N to N+1, (2*N)+1 to 3*N, 4*N to (3*N)+1, (4*N)+1 to 5*N, ... and so on.

Boundary Condition(s):
1 <= N <= 100
1 <= K <= 1000

Input Format:
The first line contains N and K separated by a space.

Output Format:
The first line contains an integer representing the Kth term in the series.

Example Input/Output 1:
Input:
4 15

Output:
14

Explanation:
Here N=4 and K=15.
The increasing and decreasing window series of size 4 is given below.
1 2 3 4 8 7 6 5 9 10 11 12 16 15 14 13 and so on...
The 15th term in the above series is 14. So 14 is printed as the output.

Example Input/Output 2:
Input:
5 8

Output:
8
"""
n,k=map(int,input().split())
q=k//n
r=k%n
if r==0:
    q-=1
    r=n
if q%2==0:
    print(k)
else:
    print((q+1)*n-(r-1))
