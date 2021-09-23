"""
The program must accept an integer N as the input. The program must find two consecutive prime integers X and Y,
where the middle integer in the range (X,Y) is equal to N (i.e., N is a composite integer which is equidistant from
two consecutive primes X and Y). If there is no such prime pair, then the program must print -1 as the output.

Boundary Condition(s):
2 <= N <= 10^5

Input Format:
The first line contains N.

Output Format: 
The first line contains X and Y separated by a space or -1. 

Example Input/Output 1: 
Input: 
6 

Output: 
5 7 

Explanation: 
Here N = 6, which is a composite integer. 
So the prime pair is (5, 7). 6-5 = 7-6 = 1. 

Example Input/Output 2: 
Input: 
473 

Output: 
467 479 

Example Input/Output 3: 
Input: 
10 

Output: 
-1
"""
