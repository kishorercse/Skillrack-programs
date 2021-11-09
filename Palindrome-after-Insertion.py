"""
The program must accept two string values S1 and S2 containing only lower case alphabets as the input. The program must check if a palindrome can be formed by inserting S1 once 
after any alphabet in S2. If a palindrome can be formed then the program must print YES. Else the program must print NO as the output. 

Boundary Condition(s):
1 <= Length of S1, S2 <= 100 

Input Format: 
The first line contains S1.
The second line contains S2.

Output Format: 
The first line contains either YES or NO. 

Example Input/Output 1:
Input:
hjk 
abkjhba 

Output: 
YES 

Explanation: 
The string values that can be formed by inserting "hjk" after each alphabet in "abkjhba" are 
ahjkbkjhba 
abhjkkjhba
abkhjkjhba
abkjhjkhba
abkjhhjkba
abkjhbhjka
abkjhbahjk
Here the second string abhjkkjhba and the fifth string abkjhhjkba are palindromes.
Hence the output is YES 

Example Input/Output 2: 
Input: 
baba 
ab 

Output: 
NO
"""
def isPalindrome(s):
    i,j=0,len(s)-1
    while i<j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True
a=input().strip()
b=input().strip()
l=len(b)
for i in range(l+1):
    t=b[:i]+a+b[i:]
    if isPalindrome(t):
        print("YES")
        break
else:
    print("NO")
