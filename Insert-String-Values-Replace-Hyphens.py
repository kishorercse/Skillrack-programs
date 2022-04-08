"""
The program must accept an integer X and N pairs as the input. Each pair contains a string and an integer. The program must form a string S of length X based on the 
following conditions.
- Initially, all the characters in the string must be hyphens.
- For each string-integer pair(string str, integer P), the program must insert the string str into the string S starting from the position P if the string S contains 
L hyphens starting from the position P (where L represents the length of string str). Else the program must not modify the string S.
Finally, the program must print the modified string S as the output.

Boundary Condition(s):
1 <= P <= X <= 100
1 <= N <= 100
1 <= Length of each string <= 30

Input Format:
The first line contains X.
The second line contains N.
The next N lines, each contains a string value str and an integer P.

Output Format:
The first line contains the string S.

Example Input/Output 1:
Input:
9
4
Skill 1
Program 4
Rack 7
Rack 6

Output:
SkillRack

Explanation:
Here X=9 and N=4, the string value S is formed with the hyphens ("-") of length 9.
For the 1st pair, the string Skill is inserted into the string S starting from the position 1. Now the string S becomes Skill----.
For the 2nd pair, the string Program cannot be inserted into the string S starting from the position 4. So the string S remains the same.
For the 3rd pair, the string Rack cannot be inserted into the string S starting from the position 7. So the string S remains the same.
For the 4th pair, the string Rack is inserted into the string S starting from the position 6. Now the string S becomes SkillRack.
Hence the output is
SkillRack

Example Input/Output 2:
Input:
11
5
Tiger 10
Rat 4
Cat 1
Tigers 7
Tiger 7

Output:
CatRatTiger

Example Input/Output 3:
Input:
5
2
year 3
key 2

Output:
-key-
"""
x=int(input())
n=int(input())
res=['-']*x
for _ in range(n):
    s,p=input().split()
    p=int(p)-1
    l=len(s)
    if p+l-1<x and all(res[i]=='-' for i in range(p,p+l)):
        ind=0
        for i in range(p,p+l):
            res[i]=s[ind]
            ind+=1
print(''.join(res))
