"""
The program must accept N integers and print all possible pairs of integers (X, Y) where both X and Y are formed using same digits. If there is no such pair, then the program must
print -1 as the output. 

Boundary Condition(s): 
2 <= N <= 100 
1 <= Each integer value <= 10^8 

Input Format:
The first line contains N.
The second line contains N integer values separated by a space. 

Output Format: 
The lines contain all the possible pairs of integers separated by a space or the first line contains -1.

Example Input/Output 1: 
Input:
6
134 5489 4413 745 88549 3114 

Output:
134 4413 
134 3114 
5489 88549
4413 3114 

Explanation:
134 and 4413 are using the digits 1, 3 and 4.
134 and 3114 are using the digits 1, 3 and 4.
5489 and 88549 are using the digits 4, 5, 8 and 9. 
4413 and 3114 are using the digits 1, 3 and 4.

Example Input/Output 2:
Input: 
5
105 840 550 115 841 

Output: -1
"""
n=int(input())
l=input().split()
f=False
for i in range(n):
    t=sorted(set(l[i]))
    for j in range(i+1,n):
        if t==sorted(set(l[j])):
            print(l[i],l[j])
            f=True
if not f:
    print(-1)
