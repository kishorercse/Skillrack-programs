"""
The program must accept an integer N as the input. The program must print the tilted rectangele pattern of N lines based on the following conditions.
- In the 1st line, the program must print N-1 hyphens and N asterisks.
- In the 2nd line, the program must print N-2 hyphens, an asterisk, N-2 hyphens and an asterisk.
- In the 3rd line, the program must print N-3 hyphens, an asterisk, N-2 hyphens and an asterisk.
- Similarly, the first N-1 lines are printed.
- In the Nth line, the program must print N asterisks.

Boundary Condition(s):
1 <= N <= 100 

Input Format: 
The first line contains N. 

Output Format: The first N lines contain the pattern as shown in the Example Input/Output Section. 

Example Input/Output 1: 
Input: 
4 

Output: 
---**** 
--*--* 
-*--* 
**** 

Explanation: 
Here N = 4, so the pattern contains 4 lines of output. 
1st line: 3 hyphens and 4 asterisks. 
2nd line: 2 hyphens, an asterisk, 4/2 hyphens and an asterisk. 
3rd line: 1 hyphen, an asterisk, 4/2 hyphens and an asterisk. 
4th line: 4 asterisks. 

Example Input/Output 2: 
Input: 3 Output: 
--*** 
-*-* 
***
"""
n=int(input())
