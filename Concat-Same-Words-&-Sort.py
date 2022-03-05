"""
The program must accept a string S containing multiple words in lower case as the input. The program must concatenate the words in S based on the following conditions.
- If two words are same in the given string, then the program must concatenate those words as a single word.
- After concatenating all possible words, then the program must print the words in sorted order.

Boundary Condition(s):
3 <= Length of S <= 1000

Input Format:
The first line contains S.

Output Format:
The first line contains the words separated by a space based on the given conditions.

Example Input/Output 1:
Input:
cat code cat code moon earth cat

Output:
cat catcat codecode earth moon

Explanation:
cat + cat = catcat
code + code = codecode
So the words [catcat, codecode, moon, earth, cat] are printed in sorted order.

Example Input/Output 2:
Input:
aa aa a a aaaa

Output:
aa aaaa aaaa

Explanation:
aa + aa = aaaa
a + a = aa
So the words [aaaa, aa, aaaa] are printed in sorted order.

Example Input/Output 3:
Input:
xyz a b c c d e e e a b xyz

Output:
aa bb cc d e ee xyzxyz
"""
s=input().split()
count={}
for i in s:
    count[i]=count.get(i,0)+1
s=[]
for i in count:
    while(count[i]>=2):
        s.append(i*2)
        count[i]-=2
    if (count[i]==1):
        s.append(i)
print(*sorted(s))
