"""
The program must accept a string S as the input. The program must remove the first occurrence of all the repeated vowels in the string S. Then the program must print the 
modified string S as the output.

Boundary Condition(s):
3 <= Length of S <= 1000

Input Format:
The first line contains S.

Output Format: 
The first line contains the modified string S. 

Example Input/Output 1:
Input: 
certificate

Output: 
crtficate

Explanation:
The repeated vowels in the string certificate are e and i.
So the first occurrence of both the vowels are removed from the string certificate. 
Hence the output is crtficate 

Example Input/Output 2:
Input:
Mango

Output:
Mango 

Example Input/Output 3:
Input:
OccurrencE@123 

Output:
OccurrencE@123
"""
s=list(input().strip())
d={}
l=len(s)
for i in range(l):
    if s[i] in "aeiouAEIOU":
        ch=s[i]
        if ch not in d:
            d[ch]=i
        else:
            if d[ch]!=-1:
                s[d[ch]]=''
                d[ch]=-1
print(*s,sep='')
