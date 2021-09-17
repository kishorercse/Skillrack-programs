"""
The program must accept a string value S as the input. The program must print the vowels in S and then print the consonants in S as the output. 

Boundary Condition(s): 
1 <= Length of S <= 100 

Input Format: 
The first line contains the values of string S. 

Output Format: 
The first line contains the vowels in S and the consonants in S. 

Example Input/Output 1: 
Input: 
Hello 

Output: 
eoHll 

Explanation: 
In Hello, the vowels are e and o. 
The consonants are H, l and l. 
Hence the output is eoHll 

Example Input/Output 2: 
Input: 
EncycLopediA 

Output: 
EoeiAncycLpd
"""
s=input().strip()
t=''
for i in s:
    if i in "AEIOUaeiou":
        print(i,end='')
    else:
        t+=i
print(t)
