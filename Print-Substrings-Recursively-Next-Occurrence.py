"""
The program must accept a string S as the input. The program must print the output based on the following conditions.
- The program must print the substring from the first letter to its next occurrence in the string S.
- Then the program must print the substring from the second letter of the previously printed substring to its next occurrence in the string S.
- The program must repeat the above process till there is no next occurrence of the second letter of the previously printed substring.

Note: There will be at least two occurrences of the first letter in the string S.

Boundary Condition(s):
2 <= Length of S <= 1000

Input Format:
The first line contains S.

Output Format:
The lines, each contains a string value representing the substrings of S based on the given conditions.

Example Input/Output 1:
Input:
abcdebabcd

Output:
abcdeba
bcdeb
cdebabc
debabcd

Explanation:
S = "abcdebabcd" -> The first letter is a. So the 1st substring is formed from a to its next occurrence.
1st substring: abcdeba -> The second letter is b. So the 2nd substring is formed from b to its next occurrence.
2nd substring: bcdeb -> The second letter is c. So the 3rd substring is formed from c to its next occurrence.
3rd substring: cdebabc -> The second letter is d. So the 4th substring is formed from d to its next occurrence.
4th substring: debabcd -> The second letter is e. There is no next occurrence of e.

Example Input/Output 2:
Input:
moonmonkey

Output:
moonm
oo
onmo
nmon
"""
s=input().strip()
d={}
l=len(s)
for i in range(l):
    d[s[i]]=d.get(s[i],[])+[i]
ind=0
while True:
    try:
        a,b=ind,d[s[ind]][1]
        d[s[ind]]=d[s[ind]][1:]
        print(s[a:b+1])
        ind+=1
    except IndexError:
        break
