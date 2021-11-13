"""
The program must accept three alphabets as the input. The program must form an integer X by adding the ASCII values of those three alphabets. Then the program must print the
binary representation of X as the output. 

Input Format:
The first line contains three alphabets separated by a space. 

Output Format: 
The first line contains the binary representation of X.

Example Input/Output 1:
Input:
a b c

Output: 
100100110 

Explanation:
The ASCII value of a is 97. 
The ASCII value of b is 98.
The ASCII value of c is 99.
So their sum is 294 (97+98+99).
The binary representation of 294 is 100100110.

Example Input/Output 2: 
Input: 
C S K

Output:
11100001
"""
print(bin(sum([ord(i) for i in input().split()]))[2:])
