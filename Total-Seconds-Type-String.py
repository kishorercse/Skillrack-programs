"""
The program must accept a string K containing all 26 lower case alphabets representing the keys in a keyboard as the input. All the keys in the keyboard are arranged in a row. 
A boy wants to type the string S using the keyboard. The value of S is also passed as the input to the program. The program must find the total seconds required to type the 
string S based on the following conditions.
- Initially, the boy is pointing to the key that he wants to type first (i.e., The first alphabet of the string S).
- The boy can only move from the current key to its adjacent keys.
- Moving from the current key to its adjacent keys(possibly two adjacents) take 1 second.
- To press any key it takes 0 seconds.
Finally, the program must print the total number of seconds required to type the string S as the output.

Boundary Condition(s):
1 <= Length of S <= 1000

Input Format:
The first line contains K.
The second line contains S.

Output Format:
The first line contains an integer value representing the total number of seconds required to type the string S based on the given conditions.

Example Input/Output 1:
Input:
abcdefghijklmnopqrstuvwxyz
notebook

Output:
41

Explanation:
The 26 keys are arranged as abcdefghijklmnopqrstuvwxyz.
The given string is notebook.
Initially the boy is pointing to the key 'n'.
n -> o (1 second).
o -> t (5 seconds).
t -> e (15 seconds).
e -> b (3 seconds).
b -> o (13 seconds).
o -> o (0 seconds).
o -> k (4 seconds).
The total seconds required to type the word notebook is 41 (1+5+15+3+13+4).
So 41 is printed as the output.

Example Input/Output 2:
Input:
zyxwvutsrqponabcdefghijklm
bookkeeper

Output:
44
"""
k=input().strip()
s=input().strip()
seconds=0
pos={}
for i in range(len(k)):
    pos[k[i]]=i
ind=pos[s[0]]
for i in range(1,len(s)):
    seconds+=abs(pos[s[i]]-ind)
    ind=pos[s[i]]
print(seconds)
