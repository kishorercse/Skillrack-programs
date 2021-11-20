"""
The program must accept N integers as the input. For each integer X among the N integers, the program must replace the largest digit with its binary representation. Then the 
program must print the sum of the N revised integers as the output. If the largest digit occurs more than once in an integer, then consider the first occurrence in the integer. 

Boundary Condition(s):
1 <= N <= 100
1 <= Each integer value <= 10^8 

Input Format: 
The first line contains N.
The second line contains N integer values separated by a space. 

Output Format:
The first line contains an integer representing the sum of the N revised integers.

Example Input/Output 1: 
Input: 
4 
204 535 190 99 

Output: 
150264

Explanation:
204 -> 20100
535 -> 10135
190 -> 110010
99 -> 10019 
20100 + 10135 + 110010 + 10019 = 150264. 

Example Input/Output 2: 
Input:
5
93 99 34 56 20 

Output:
28342
"""
n=int(input())
l=input().split()
s=0
for i in range(n):
    mx=max(l[i])
    l[i]=l[i].replace(mx,bin(int(mx))[2:],1)
    s+=int(l[i])
print(s)
