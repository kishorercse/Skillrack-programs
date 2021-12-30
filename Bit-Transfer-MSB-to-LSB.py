"""
The program must accept an array of N integers as the input. The program must transfer the MSB of each integer to the LSB of its previous integer in the given array. For the 
first integer in the array, consider the last integer as the previous integer. Then the program must print the revised values of the N integers as the output.

Boundary Condition(s):
2 <= N <= 100
1 <= Each integer value <= 10^8

Input Format:
The first line contains N.
The second line contains N integer values separated by a space.

Output Format:
The first line contains the revised N integers separated by a space.

Example Input/Output 1:
Input:
4
15 10 12 35

Output:
15 5 9 7

Explanation:
The binary representations of the 4 integers are given below.
1111 1010 1100 100011

After transferring the MSB of each integer to the LSB of its previous integer, the binary representations become
1111 0101 1001 000111

Example Input/Output 2:
Input:
5
32 21 65 56 9

Output:
1 11 3 49 3

Explanation:
The binary representations of the 5 integers are given below.
100000 10101 1000001 111000 1001

After transferring the MSB of each integer to the LSB of its previous integer, the binary representations become
000001 01011 0000011 110001 0011
"""
n=int(input())
l=[bin(int(i))[2:] for i in input().split()]
for i in range(n):
    l[i-1]=l[i-1]+l[i][0]
    l[i]=l[i][1:]
for i in l:
    print(int(i,2),end=' ')
