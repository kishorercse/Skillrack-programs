"""
N persons first and last names are passed as input. The program must sort them based on the last name. (All last names are distinct, that is last name will not repeat)

Input Format:
The first line contains the value of N.
Next N lines contain the first name and the last name of N persons, with the values separated by a space.

Output Format:
N lines containing the N first and last names separated by a space (sorted by last name)

Boundary Conditions:
2 <= N <= 15
Length of first and last name is between 2 and 50.

Example Input/Output 1:
Input:
6
Arul Prakash
Banu Govind
Syed Siraj
John Joshua
Dhanraj Pillay
Bhagat Singh

Output:
Banu Govind
John Joshua
Dhanraj Pillay
Arul Prakash
Bhagat Singh
Syed Siraj
"""
n=int(input())
l=sorted([input().split() for _ in range(n)],key=lambda x:x[1])
for i in l:
    print(*i)
