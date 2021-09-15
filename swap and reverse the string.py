"""
The program must accept a string S as the input. The program must swap the first two characters then swap the next two characters and so on.
The program must print the modified string S in the reverse order as the output. 
Note: The last character is not swapped since it has no pair as the length is odd. 

Boundary Condition(s):
1 <= Length of S <= 10000 

Input Format:
The first line contains the value of string S. 

Output Format: 
The first line contains the modified string value. 

Example Input/Output 1: 
Input: 
elephant 
Output: 
nthaepel 
Explanation: 
The 1st and 2nd characters are e and l, after swapping the characters are l and e 
The 3rd and 4th characters are e and p, after swapping the characters are p and e 
The 5th and 6th characters are h and a, after swapping the characters are a and h 
The 7th and 8th characters are n and t, after swapping the characters are t and n 
The modified string value is lepeahtn. So the reversed string value is lepeahtn 
Hence the output is nthaepel.
Example Input/Output 2: 
Input:
titan 
Output:
ntati
"""
s=list(input().strip())
l=len(s)
for i in range(0,l-l%2,2):
    s[i],s[i+1]=s[i+1],s[i]
print(*s[::-1],sep='')
