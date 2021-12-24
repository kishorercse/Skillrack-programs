"""
The program must accept an integer N as the input. The program must form a word matrix of size N*N based on the following conditions.
- In the 1st row, the N words must be formed using consecutive lower case alphabets of lengths 1, 2, 3, ... N.
- In the 2nd row, the N words must be formed using consecutive lower case alphabets of lengths 2, 3, 4, ... N+1.
- In the 3rd row, the N words must be formed using consecutive lower case alphabets of lengths 3, 4, 5, ... N+2.
- Similarly, the words in the remaining rows must be formed.
- Consider the English alphabet set in circular fashion when creating the words of length more than 26.
Finally, the program must print the N*N word matrix as the output.

Boundary Condition(s):
2 <= N <= 25

Input Format:
The first line contains N.

Output Format:
The first N lines, each contains N words separated by a space.

Example Input/Output 1:
Input:
4

Output:
a ab abc abcd
ab abc abcd abcde
abc abcd abcde abcdef
abcd abcde abcdef abcdefg

Explanation:
The length of each word in the 4*4 word matrix is given below.
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7

So the 4*4 word matrix is formed using the consecutive lower case alphabets as given below.
a ab abc abcd
ab abc abcd abcde
abc abcd abcde abcdef
abcd abcde abcdef abcdefg

Example Input/Output 2:
Input:
5

Output:
a ab abc abcd abcde
ab abc abcd abcde abcdef
abc abcd abcde abcdef abcdefg
abcd abcde abcdef abcdefg abcdefgh
abcde abcdef abcdefg abcdefgh abcdefghi
"""
n=int(input())
s="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
for i in range(1,n+1):
    for j in range(i,n+i):
        print(s[:j],end=' ')
    print()
