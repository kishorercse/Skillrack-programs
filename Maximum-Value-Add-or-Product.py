"""
The program must accept N integers as the input. For each integer X among the given N integers, the program must print the maximum between the sum of digits in X and the 
product of digits in X.

Boundary Condition(s):
1 <= N <= 1000
1 <= Each integer value <= 10^5

Input Format:
The first line contains N.
The second line contains N integer values separated by a space.

Output Format:
The first line contains N integer values separated by a space.

Example Input/Output 1:
Input:
5
140 34 61 10 59

Output:
5 12 7 1 45

Explanation:
Here N=5 and the given 5 integers are 140 34 61 10 59.
1st integer 140: (1+4+0) > (1*4*0) = 5 is the maximum.
2nd integer 34: (3+4) < (3*4) = 12 is the maximum.
3rd integer 61: (6+1) > (6*1) = 7 is the maximum.
4th integer 10: (1+0) > (1*0) = 1 is the maximum.
5th integer 59: (5+9) < (5*9) = 45 is the maximum.

Example Input/Output 2:
Input:
4
99 91 90001 444

Output:
81 10 10 64
"""
n=int(input())
l=input().split()
for i in l:
    s=0
    p=1
    for j in i:
        s+=int(j)
        p*=int(j)
    print(max(s,p),end=' ')
