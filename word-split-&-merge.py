"""
The program must accept a string S and an integer K as the input. The string S contains multiple words. The integer K
represents the position of a word in the string. The program must modify the Kth word in S based on the following
conditions.
- The program must split the Kth word into two equal halves. If the word length is odd, then consider the middle character
for both halves.
- Then the program must reverse the first half and then merge the second half and first half into a single word.
- Then the program must replace the Kth word with the obtained word in the string S.
Finally, the program must print the revised string S.


Boundary Condition(s): 
1 <= Length of S <= 1000 
1 <= K <= Number of words in S. 

Input Format:
The first line contains S. 
The second line contains K. 

Output Format: 
The first line contains the revised string S.

Example Input/Output 1: 
Input:
This is the right choice 
4

Output:
This is the ghtgir choice 

Explanation: 
Here K = 4.
The 4th word is right, whose length is odd.
First Half: rig
Second Half: ght
After reversing the first half, rig becomes gir.
After merging the second half and first half, the word becomes ghtgir. 

Example Input/Output 2: 
Input:
This is the right choice 
1

Output: 
ishT is the right choice 

Explanation:
Here K = 1.
The 1st word is This, whose length is even. 
First Half: Th 
Second Half: is 
After reversing the first half, Th becomes hT.
After merging the second half and first half, the word becomes ishT.
"""
s=input().split()
k=int(input())-1
l=len(s[k])
t=l//2
s[k]=s[k][t:]+s[k][:t+l%2][::-1]
print(*s)
