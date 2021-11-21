"""
The program must accept a string S and Q queries as the input. The query can be S+X or X+S where X is an integer. For each query, the program must modify the string S based on 
the following conditions. 
- If the query is S+X, then the program must append the last X characters to the same string.
- If the query is X+S, then the program must prepend the first X characters to the same string. 
Finally, the program must print the modified string S as the output. 

Note: If there are no X characters in S to perform the append or prepend operation, then consider the entire string to perform the operation.

Boundary Condition(s):
1 <= X, Length of S <= 100
1 <= Q <= 50 

Input Format: 
The first line contains S. 
The second line contains Q.
The next Q lines, each contains a query. 

Output Format:
The first line contains the modified string S.

Example Input/Output 1:
Input: 
SkillRack
5
S+1
2+S
S+4
S+1
3+S

Output: 
SkSSkSkillRackkackkk 

Explanation:
The given string S is SkillRack. 
After the first query S+1, the string becomes SkillRackk.
After the second query 2+S, the string becomes SkSkillRackk.
After the third query S+4, the string becomes SkSkillRackkackk.
After the fourth query S+1, the string becomes SkSkillRackkackkk.
After the fifth query 3+S, the string becomes SkSSkSkillRackkackkk.

Example Input/Output 2:
Input:
Programming
3
S+13 
7+S 
S+2 

Output: 
ProgramProgrammingProgrammingng
"""
s=input().strip()
q=int(input())
while q>0:
    a,b=input().split('+')
    if a.isnumeric():
        s=s[:int(a)]+s
    else:
        s=s+s[-int(b):]
    q-=1
print(s)
