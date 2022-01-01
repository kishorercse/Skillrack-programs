"""
The program must accept first and last names of three persons who are in a family tree and print the grandson's name.

Input Format:
The first line contains the first and last name of person 1 separated by a space.
The second line contains the first and last name of person 2 separated by a space.
The third line contains the first and last name of person 3 separated by a space.

Output Format:
The first line contains the first and last name of the grandson separated by a space.

Boundary Conditions:
Length of first and last names are from 3 to 100

Note: The last name of a person is nothing but the father's first name.

Example Input/Output 1:
Input:
Arun Kumar
Swamy Nathan
Kumar Swamy

Output:
Arun Kumar
"""
l=[input().split() for _ in range(3)]
for i in range(3):
    if (l[i][-1]==l[(i+1)%3][0] and l[(i+1)%3][-1]==l[(i+2)%3][0]) or (l[i][-1]==l[(i+2)%3][0] and l[(i+2)%3][-1]==l[(i+1)%3][0]):
        print(*l[i])
