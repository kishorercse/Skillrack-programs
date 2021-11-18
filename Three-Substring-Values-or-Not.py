"""
The program must accept a string S as the input. The program must print YES if the string S is formed using exactly three same substring values. Else the program must print NO 
as the output. 

Note: The length of S is always divisible by 3. 

Boundary Condition(s): 
3 <= Length of S <= 99 

Input Format: 
The first line contains S. 

Output Format: 
The first line contains YES or NO.

Example Input/Output 1: 
Input: 
goldgoldgold

Output:
YES 

Explanation: 
Here the string goldgoldgold is formed using exactly three substring values gold. So YES is printed as the output. 

Example Input/Output 2: 
Input:
byebyeeye 

Output:
NO
"""
s=input().strip()
l=len(s)
t=l//3
a=s[:t]
if all(s[i:i+t]==a for i in range(t,l,t)):
    print("YES")
else:
    print("NO")
