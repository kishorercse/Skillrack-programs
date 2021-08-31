"""
Inverted Trapezium Pattern Program In C: The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output sections.

Boundary Condition(s):
1 <= N <= 100

Input Format:
The first line contains the value of N.

Output Format:
The first N lines contain the desired pattern as shown in the Example Input/Output sections.

Example Input/Output 1:
Input:
4

Output:
– – – 10 11
– – 8 9 12 13
– 5 6 7 14 15 16
1 2 3 4 17 18 19 20

Example Input/Output 2:
Input:
5

Output:
– – – – 15 16
– – – 13 14 17 18
– – 10 11 12 19 20 21
– 6 7 8 9 22 23 24 25
1 2 3 4 5 26 27 28 29 30
"""
n=int(input())
a=n*(4+(n-1)*2)//4
a=b=a+1
hy=n-1
for i in range(n):
    print('- '*hy,end='')
    a=a-i-1
    for j in range(i+1):
        print(a+j,end=' ')
    for j in range(i+1):
        print(b,end=' ')
        b+=1
    print()
    hy-=1
