"""
The program must accept a string S as the input. The program must print the number of times the alphabet toggles from lower case to upper case and vice versa.

Boundary Condition(s):
1 <= Length of S <= 10^4

Input Format:
The first line contains S.

Output Format:
The first line contains an integer value representing the number of times the alphabet toggles from lower case to upper case and vice versa in the given string S.

Example Input/Output 1:
Input:
oRangE is Good.

Output:
4

Explanation:
Here the given string is oRangE is Good.
Initially, the toggle count is 0.
The alphabet toggles from lower case 'o' to upper case 'R', so the toggle count becomes 1.
The alphabet toggles from upper case 'R' to lower case 'a', so the toggle count becomes 2.
The alphabet toggles from lower case 'g' to upper case 'E', so the toggle count becomes 3.
The alphabet toggles from upper case 'G' to lower case 'o', so the toggle count becomes 4.
So 4 is printed as the output.

Example Input/Output 2:
Input:
aaa bbb cccDDD

Output:
1

Example Input/Output 3:
Input:
aa5BBC6def

Output:
0

Example Input/Output 4:
Input:
aa5BBC6dEf

Output:
2
"""
s=input().strip()
l=len(s)
ans=0
for i in range(1,l):
    if (s[i-1].islower() and s[i].isupper()) or (s[i-1].isupper() and s[i].islower()):
        ans+=1
print(ans)
