"""
The program must accept a string S as the input. The program must print "YES" if the given string a sandwich string. Else the program must print "NO" as the output. A sandwich string is a string that is formed by two identical ends and a different middle. The sandwich string contains only 2 unique characters. 

Boundary Condition(s): 
1 <= Length of S <= 100 

Input Format: 
The first line contains S. 

Output Format: 
The first line contains YES or NO.

Example Input/Output 1: 
Input: 
XXYYYXX 

Output: 
YES 

Explanation: 
Here the given string is XXYYYXX. The given string has two identical ends as XX and the different middle as YYY. So YES is printed as the output. 

Example Input/Output 2: 
Input: 
5@@5 

Output: 
YES 

Example Input/Output 3: 
Input: 
abababa 

Output: 
NO 

Example Input/Output 4: 
Input: 
aaaqqqaa 

Output: 
NO 
"""
s=input().strip()
i,j=0,len(s)-1
while i<j and s[i]==s[j] and s[i]==s[0]:
    i+=1
    j-=1
if len(set(s))==2 and len(set(s[i:j+1]))==1:
    print("YES")
else:
    print("NO")
