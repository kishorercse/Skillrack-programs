"""
In a text editor, the text area shows X lines, where each line contains a maximum of Y characters. The text editor never
breaks a word into multiple lines. Initially, the text editor is empty. The program must accept a string S as the input.
The string S represents the text to be pasted into the text editor. The text editor automatically shows a vertical scroll
bar based on the lengths of the words in the text. In a single scroll (up/down), the text editor moves the text by one line
up/down. The program must print an integer representing the number of times the scroll bar to be moved down to reach the
last line as the output.

Note: The length of each word in S is always less than or equal to Y.

Boundary Condition(s):
1 <= X, Y <= 100
1 <= Length of S <= 100

Input Format:
The first line contains X and Y separated by a space.
The second line contains S.

Output Format:
The first line contains the number of times the scroll bar to be moved down to reach the last line.

Example Input/Output 1:
Input:
4 10
Rat Cat Lion Tiger Elephant Ox Fox Eagle Dog Snake Owl Ostrich

Output:
3
"""
x,y=map(int,input().split())
s=input().strip()
l=len(s)
lines=-x
while s:
    if l<=y or s[y]==' ':
        lines+=1
        s=s[y+1:]
        l=l-(y+1)
    else:
        for i in range(y-1,-1,-1):
            if s[i]==' ':
                s=s[i+1:]
                l=l-(i+1)
                lines+=1
                break
if lines<0:
    print(0)
else:
    print(lines)
