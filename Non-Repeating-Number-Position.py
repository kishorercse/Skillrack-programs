"""
2N+1 numbers are passed as input to the program. Out of these numbers, N numbers repeat twice and hence account for 2N numbers. Only one number I is a non-repeating number. 
The program must print the position of the non-repeating number (The position starts from 1).

Note: You need to optimize the logic for large input values. Else "Timeout" will occur.

Input Format:
First line contains N.
Second line contains 2N+1 numbers separated by a space.

Output Format:
First line contains the position of the only non-repeating number I.

Boundary Conditions:
1 <= N <= 1000000
1 <= Value of an individual number <= 9999999

Example Input/Output 1:
Input:
10
86 11 40 10 78 63 73 68 16 44 86 11 40 10 78 73 68 16 24 44 24

Output:
6

Explanation:
N=10, Hence 21 numbers are passed as the input. Among these numbers, only 63 is not repeated. The position of 63 is 6 (As it occurs as the sixth number)


Example Input/Output 2:
Input:
12
7514716 2638298 6854805 6770589 1632983 6032326 6854805 2312182 2312182 367141 9985662 4682266 4682266 6770589 8713485 8964136 8964136 367141 9985662 3099970 1632983 3099970 6032326 8713485 2638298

Output:
1

Explanation:
The only non repeating number is 7514716 which is in the first position.
"""
n=int(input())
l=list(map(int,input().split()))
count={}
for i in range(2*n+1):
    try:
        count[l[i]][1]+=1
    except KeyError:
        count[l[i]]=[i,1]
for i in  count:
    if count[i][1]==1:
        print(count[i][0]+1)
        break
