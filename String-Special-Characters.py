"""
The program must accept a string S as the input. The program must print the special characters in the string S as the output. A special character is a character that is not an 
alphabetic or numeric or space character.
Note: At least one special character is always present in the string S. 

Boundary Condition(s):
1 <= Length of S <= 100 

Input Format:
The first line contains S. 

Output Format:
The first line contains the special characters in the string S. 

Example Input/Output 1: 
Input: 
skill@rack#123 

Output: 
@# 

Explanation: 
The special characters in the string skill@rack#123 are @ and #.
Hence the output is @# 

Example Input/Output 2:
Input:
Sum: 45+10 = 55 

Output: 
:+=
"""
s=input().strip()
for i in s:
    if i!=' ' and not i.isnumeric() and not i.isalpha():
        print(i,end='')
