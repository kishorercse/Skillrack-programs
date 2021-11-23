"""
The program must accept N integers as the input. The program must sort the integers based on the parity (Even parity followed by Odd parity). If two or more integers having 
the same parity, then the program must sort those integers in ascending order.
If the number of 1s in the binary representation of an integer is even, then it represents Even Parity.
If the number of 1s in the binary representation of an integer is odd, then it represents Odd Parity.

Boundary Condition(s):
2 <= N <= 100
1 <= Each integer value <= 1000

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains the sorted integers based on the given conditions.

Example Input/Output 1:
Input:
6
15 25 387 440 48 80

Output:
15 48 80 387 25 440

Explanation:
Here N = 6.
The integer 15 has Even parity (1111).
The integer 25 has Odd parity (11001).
The integer 387 has Even parity (110000011).
The integer 440 has Odd parity (110111000).
The integer 48 has Even parity (110000).
The integer 80 has Even parity (1010000).
After sorting the integers based on the given conditions, the integers become 15 48 80 387 25 440.

Example Input/Output 2:
Input:
7
78 32 10 15 98 35 26

Output:
10 15 78 26 32 35 98
"""
n=int(input())
even=[]
odd=[]
for i in list(map(int,input().split())):
    if bin(i).count('1')%2==0:
        even.append(i)
    else:
        odd.append(i)
print(*sorted(even),*sorted(odd))
