"""
The program must accept a string S as the input. The string contains pairs of groups of an equal number of alphabets and digits. The program must expand the string S by repeating 
each alphabet the corresponding digit times. Boundary Condition(s): 2 <= Length of S <= 100 Input Format: The first line contains S. Output Format: The first line contains the 
expanded string. 

Example Input/Output 1: 
Input: 
lion1234cat523 

Output: 
liiooonnnncccccaattt 

Explanation: 
Here S = "lion1234cat523". 
1st group "lion1234": 
l -> 1 -> l 
i -> 2 -> ii
o -> 3 -> ooo
n -> 4 -> nnnn 
2nd group "cat523": 
c -> 5 -> ccccc 
a -> 2 -> aa 
t -> 3 -> ttt 

Example Input/Output 2: 
Input: 
a2bc78xyz105 

Output: 
aabbbbbbbccccccccxzzzzz
"""
s=input().strip()
t=''
for i in s:
    if i.isalpha():
        t+=i
    else:
        print(t[0]*int(i),end='')
        t=t[1:]
