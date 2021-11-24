"""
The program must accept an integer N as the input. The program must print each place value in the integer N as the output.

Boundary Condition(s):
-10^18 <= N <= 10^18

Input Format:
The first line contains N.

Output Format:
The first line contains the integer values representing the place values in the integer N.

Example Input/Output 1:
Input:
49

Output:
40 9

Explanation:
Here the given integer is 49.
The digit 4 is in the tenth place, so 40 is printed.
The digit 9 is in the unit place, so 9 is printed.

Example Input/Output 2:
Input:
-525

Output:
-500 -20 -5

Example Input/Output 3:
Input:
1000

Output:
1000 0 0 0
"""
n=input().strip()
place='0'*(len(n)-1)
neg=False
if n[0]=='-':
    neg=True
    n=n[1:]
    place=place[1:]
for i in n:
    if neg and i!='0':
        print('-',end='')
    print(int(i+place),end=' ')
    place=place[1:]
