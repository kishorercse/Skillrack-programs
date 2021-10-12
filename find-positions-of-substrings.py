"""
The program must accept a string S and its substrings as the input. All the substrings of S have an equal length.
For each substring, the program must print the substring position in the string S as the output.
Note: All the substrings of S are always unique.

Boundary Condition(s):
1 <= Length of S <= 100

Input Format:
The first line contains S. 
The lines contain the substrings of S.

Output Format:
The lines contain the positions of the substrings in S.

Example Input/Output 1:
Input: 
skillrack 
ack 
ski 
llr

Output: 
3
1
2

Explanation: 
Here S = "skillrack" and its substrings are given below. 
ack -> 3rd substring of S.
ski -> 1st substring of S.
llr -> 2nd substring of S. 

Example Input/Output 2:
Input: 
donkeymonkeykangaroo
ymonk 
eykan 
donke 
garoo 

Output: 
2 
3 
1 
4 

Explanation: 
Here S = "donkeymonkeykangaroo" and its substrings are given below. 
ymonk -> 2nd substring of S. 
eykan -> 3rd substring of S. 
donke -> 1st substring of S. 
garoo -> 4th substring of S.
"""
