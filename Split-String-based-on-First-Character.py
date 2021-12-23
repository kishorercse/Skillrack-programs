"""
The program must accept a string S as the input. The program must split the string S into as many substrings as possible so that each substring starts with the first character 
of S. Then the program must print those substrings in sorted order as the output.

Boundary Condition(s):
2 <= Length of S <= 100

Input Format:
The first line contains S.

Output Format:
The first line contains the substrings of S separated by a space based on the given conditions.

Example Input/Output 1:
Input:
owloxlion

Output:
on owl oxli

Explanation:
The first character of the given string is o.
The substrings that start with the character o are given below.
owl oxli on
So they are printed in sorted order.

Example Input/Output 2:
Input:
bookbankbloodbaby

Output:
ba bank blood book by
"""
s=input().strip()
l=len(s)
end=l
ans=[]
for i in range(l-1,-1,-1):
    if s[0]==s[i]:
        ans.append(s[i:end])
        end=i
print(*sorted(ans))
