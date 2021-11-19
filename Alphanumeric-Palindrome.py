"""
The program must accept a string S as the input. The program must print YES if all the alphanumeric characters in the string S forms a palindrome. Else the program must print NO 
as the output. 

Note: At least one alphanumeric character is always present in the string S. 

Boundary Condition(s): 
1 <= Length of S <= 100

Input Format: 
The first line contains S. 

Output Format: 
The first line contains YES or NO.

Example Input/Output 1:
Input: 
a#b#c@3cb=a

Output:
YES 

Explanation: 
The alphanumeric characters in the given string are a b c 3 c b a. 
Here the alphanumeric characters forms a palindrome.
Hence the output is YES 

Example Input/Output 2: 
Input:
*R-ack+kca-r 

Output:
NO

Example Input/Output 3: 
Input:
***H2O@O-2-H**

Output: 
YES
"""
s=input().strip()
i,j=0,len(s)-1
while i<j:
    if s[i].isalnum() and s[j].isalnum():
        if s[i]!=s[j]:
            print("NO")
            break
        i+=1
        j-=1
    while not s[i].isalnum():
        i+=1
    while not s[j].isalnum():
        j-=1
else:
    print("YES")
