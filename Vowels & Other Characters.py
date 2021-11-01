"""
The program must accept a character CH and an integer N as the input. The program must print the output based on the following condition. 
- If CH is a vowel, then the program must print the vowel N times. Else the program must print the character 2*N times.

Boundary Condition(s):
1 <= N <= 50 

Input Format: 
The first line contains CH. 
The second line contains N. 

Output Format:
The first line contains a string value based on the given condition.

Example Input/Output 1:
Input:
E 
6

Output:
EEEEEE

Explanation: 
Here CH = E, which is a vowel. So E is printed 6 times. 

Example Input/Output 2:
Input: 
# 
4 

Output:
######## 

Explanation: 
Here CH = #, which is not a vowel. So # is printed 8 times (2*4).
"""
ch=input().strip()
n=int(input())
if ch in "AEIOUaeiou":
    print(ch*n)
else:
    print(ch*(2*n))
