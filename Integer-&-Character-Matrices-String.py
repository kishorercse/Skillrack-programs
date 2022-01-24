"""
The program must accept a string S and an integer N as the input. The string contains N*N integers and N*N alphabets without any space. The number of digits in all N*N integers
is equal. The program must form two matrices M1(integer matrix) and M2(character matrix) of equal size N*N. The matrix M1 must be formed using the integers in S and the matrix
M2 must be formed using the alphabets in S. Finally, the program must print the matrices M1 and M2 as the output.

Boundary Condition(s):
8 <= Length of S <= 4000
2 <= N <= 25

Input Format:
The first line contains S.
The second line contains N.

Output Format:
The first N lines, each contains N integer values separated by a space.
The next N lines, each contains N characters separated by a space.

Example Input/Output 1:
Input:
1045a20s80df
2

Output:
10 45
20 80
a s
d f

Explanation:
Here N = 2, so the size of M1 and M2 is equal to 2*2.
There are four 2-digit integers in the string.
10 45 20 80

There are four alphabets in the string.
a s d f

The integer matrix M1 is
10 45
20 80

The character matrix M2 is
a s
d f

Example Input/Output 2:
Input:
123471859548f3214g7410hiabc50006006de98746542
3

Output:
1234 7185 9548
3214 7410 5000
6006 9874 6542
f g h
i a b
c d e
"""
s=input().strip()
n=int(input())
a=d=''
for i in s:
    if i.isalpha():
        a+=i
    else:
        d+=i
l=len(d)//(n*n)
for i in range(n):
    for j in range(n):
        print(d[:l],end=' ')
        d=d[l:]
    print()
ind=0
for i in range(n):
    for j in range(n):
        print(a[ind],end=' ')
        ind+=1
    print()
