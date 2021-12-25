"""
The program must accept a string S as the input. The string S contains only parentheses, where each open parenthesis '(' has a matching close parenthesis ')'. The program must split the string S into as many substrings as possible, where the parentheses in each substring must be balanced. Then the program must sort the balanced substrings based on their nesting level. If two or more balanced substrings have the same nesting level, then the program must sort those balanced substrings in the order of their occurrence. Finally, the program must print the sorted balanced substrings as the output.

Boundary Condition(s):
2 <= Length of S <= 100

Input Format:
The first line contains S.

Output Format:
The first line contains the sorted balanced substrings separated by a space.

Example Input/Output 1:
Input:
((())(())())()((()((())))())((()))(()()()()()())

Output:
() (()()()()()()) ((())(())()) ((())) ((()((())))())

Explanation:
There are 5 balanced substrings in the given string S.
((())(())()) -> Nesting Level 3
() -> Nesting Level 1
((()((())))()) -> Nesting Level 5
((())) -> Nesting Level 3
(()()()()()()) -> Nesting Level 2
After sorting the balanced substrings based on their nesting level, the substrings become

Example Input/Output 2:
Input:
(((())))((((()))))()(())((()))

Output:
() (()) ((())) (((()))) ((((()))))
"""
s=input().strip()
l=len(s)
res=[]
sub=""
nest=0
bal=0
for i in range(l):
    if s[i]=='(':
        bal+=1
    else:
        bal-=1
    nest=max(bal,nest)
    sub+=s[i]
    if bal==0:
        res.append([sub,nest])
        sub=""
        nest=0
res=sorted(res,key=lambda x:x[1])
for i in res:
    print(i[0],end=' ')
