"""
The program must accept an integer N and a digit D as the input. The program must print the maximum possible integer value that can be formed by removing the digit D exactly 
once in the integer N.
Note: The integer N will have at least one digit D.

Boundary Condition(s):
-10^5 <= N <= 10^5

Input Format:
The first line contains N.
The second line contains D.

Output Format:
The first line contains an integer representing the maximum possible integer value based on the given conditions.

Example Input/Output 1:
Input:
26967
6

Output:
2967

Explanation:
Here N = 26967 and D = 6.
The two possible integer values obtained by removing the digit 6 exactly once in N are 2697 and 2967.
The maximum value between the above two integers is 2967.
Hence 2967 is printed as the output.

Example Input/Output 2:
Input:
-4749
4

Output:
-479

Example Input/Output 3:
Input:
-8000
8

Output:
0
"""
n=input().strip()
d=input().strip()
mx=-999999999
l=len(n)
for i in range(l):
    if n[i]==d:
        mx=max(mx,int(n[:i]+n[i+1:]))
print(mx)
