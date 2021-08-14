"""
The program must accept N integers as the input. The program must print "YES" if the given N integers represent a binary growing
sequence. Else the program must print "NO" as the output. A binary growing sequence is a sequence of positive integers (B1, B2, B3,...Bn),where all ones in the binary representation of Bi are in the places of ones in the binary representation of B(i+1).

     
Boundary Condition(s):

2 <=N <= 1000

1 <= Each integer value <= 1045

     

Input Format:
The first line contains N.
The second line contains N integer values separated by a space.

Output Format:
The first line contains YES or NO.

Example Input/Output 1:
Input:

4

15723

Output:
YES

Explanation:
The binary representation of 1 is 1.

The binary representation of 5 is 101.

The binary representation of 7 is 111.

The binary representation of 23 is 10111.

The binary growing sequence is 1, 101, 111 and 10111.

Example Input/Output 2:
Input:

5

2.1027 219 731

Output:
YES

Example Input/Output 3:
Input:

4

41257 185

Output:
NO
"""
