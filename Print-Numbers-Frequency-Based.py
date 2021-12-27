"""
An array of N positive integers is passed as input. The program must print the numbers in the array based on the frequency of their occurrence. The highest frequency numbers 
appear first in the output.

Note: If two numbers have the same frequency of occurrence (repetition) print the smaller number first.

Input Format:
The first line contains N
The second line contains the N positive integers, each separated by a space.

Output Format:
The first line contains the numbers ordered by the frequency of their occurrence as described above.

Boundary Conditions:
1 <= N <= 1000

Example Input/Output 1:
Input:
10
1 3 4 4 5 5 1 1 2 1

Output:
1 4 5 2 3

Example Input/Output 2:
Input:
12
7 1 9 12 13 9 7 22 21 13 22 100

Output:
7 9 13 22 1 12 21 100

Example Input/Output 3:
Input:
5
11 11 11 11 11

Output:
11
"""
n=int(input())
l=list(map(int,input().split()))
count={}
for i in l:
    count[i]=count.get(i,0)+1
count=sorted(count.items(),key=lambda x:(-x[1],x[0]))
for i in count:
    print(i[0],end=' ')
