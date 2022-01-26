"""
The program must accept a string S containing only lower case alphabets as the input. The program must replace each sequence of repeated alphabets in S with the sequence of 
English alphabets starting from the repeated alphabet. Consider the English alphabets in circular fashion when replacing the repeated alphabets in S. Finally the program must
print the revised string S as the output.

Boundary Condition(s):
1 <= Length of S <= 1000

Input Format:
The first line contains S.

Output Format:
The first line contains the revised string S.

Example Input/Output 1:
Input:
breezzzeeee

Output:
brefzabefgh

Explanation:
Here the given string is breezzzeeee.
The first sequence of repeated alphabets is ee, which is replaced with ef.
The second sequence of repeated alphabets is zzz, which is replaced with zab.
The third sequence of repeated alphabets is eeee, which is replaced with efgh.
So the string becomes brefzabefgh.

Example Input/Output 2:
Input:
bookkeeper

Output:
bopklefper
"""
s=input().strip()
l=len(s)
t=s[0]
print(s[0],end='')
count=1
for i in range(1,l):
    if s[i]==t:
        print(chr(97+(ord(t)+count-97)%26),end='')
        count+=1
    else:
        print(s[i],end='')
        count=1
        t=s[i]
