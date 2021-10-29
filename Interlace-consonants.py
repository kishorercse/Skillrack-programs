"""
The program must accept two string values S1 and S2 as the input. The program must print all the consonants in the string S1 in forward order interlaced with all the consonants 
in the string S2 in reverse order as the output.
Note: The string S1 and S2 always contain atleast one consonant.

Boundary Condition(s):
1 <= Length of S1, S2 <= 1000

Input Format: 
The first line contains S1. 
The second line contains S2. 

Output Format: 
The first line contains the string based on the given condition.

Example Input/Output 1: 
Input: 
AABCD 
beftrgdhmesk 

Output: 
BkCsDmhdgrtfb 

Explanation: 
The consonants in the string AABCD in forward order are BCD 
The consonants in the string beftrgdhmesk in reverse order are ksmhdgrtfb 
By Interlacing these consonants we get BkCsDmhdgrtfb. 
So it is printed as the output. 

Example Input/Output 2: 
Input: 
ASDHIOJGK 
OIJLMHA 

Output: 
SHDMHLJJGK
"""
a=input().strip()
b=input().strip()
vowels="AEIOUaeiou"
x=len(a)
i=0
j=len(b)-1
while i<x or j>=0:
    while i<x and a[i] in vowels:
        i+=1
    if i<x:
        print(a[i],end='')
        i+=1
    while j>=0 and b[j] in vowels:
        j-=1
    if j>=0:
        print(b[j],end='')
        j-=1
