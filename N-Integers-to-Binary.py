"""
The program must accept N integers as the input. The program must form an integer K whose binary representation is formed by choosing Xth bit from the LSB(Least Significant Bit)
of Xth integer among the N integers, where X represents the position of the integer. Then the program must print the integer K as the output.

Boundary Condition(s):
1 <= N <= 50
1 <= Each integer value <= 10^18

Input Format:
The first line contains N.
The second line contains N integer values separated by a space.

Output Format:
The first line contains K.

Example Input/Output 1:
Input:
5
6 10 15 2 16

Output:
22

Explanation:
Here N = 5.
1st integer: 6 -> 00110 -> 0.
2nd integer: 10 -> 01010 -> 1.
3rd integer: 15 -> 01111 -> 1.
4th integer: 2 -> 00010 -> 0.
5th integer: 16 -> 10000 -> 1.
K = 10110 -> 22.

Example Input/Output 2:
Input:
3
7 4 12

Output:
5
"""
