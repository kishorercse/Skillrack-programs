"""
The program must accept a string S containing only alphabets and digits as the input. The program must reverse every
group of alphabets and every group of digits in the string S. Then the program must print the revised string S as the
output.

Boundary Condition(s):
1 <= Length of S <= 1000

Input Format:
The first line contains S. 

Output Format: 
The first line contains the revised string.

Example Input/Output 1:
Input: 
abcd1234skillrack994xyz 

Output: 
dcba4321kcarlliks499zyx

Explanation: 
1st group (alphabets): abcd -> dcba 
2nd group (digits): 1234 -> 4321 
3rd group (alphabets): skillrack -> kcarlliks 
4th group (digits): 994 -> 499 
5th group (alphabets): xyz -> zyx 

Example Input/Output 2: 
Input: 
a1b10cd4ef56 

Output:
a1b01dc4fe6
"""
s=input().strip()
t=s[0]
for i in s[1:]:
    if i.isdigit()==t[-1].isdigit():
        t=i+t
    else:
        print(t,end='')
        t=i
print(t)
