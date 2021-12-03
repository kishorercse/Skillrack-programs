"""
The program must accept a string S which contains digits as integer values and words. The program must toggle the digits to words and words to digits in the given string. 
Then the program must print the revised string S as the output.

Boundary Condition(s):
1 <= Length of S <= 100

Input Format:
The first line contains S.

Output Format:
The first line contains the revised string S.

Example Input/Output 1:
Input:
55six7eightninezero1

Output:
fivefive6seven890one

Explanation:
5 -> five
5 -> five
six -> 6
7 -> seven
eight -> 8
nine -> 9
zero -> 0
1 -> one

Example Input/Output 2:
Input:
99447zerooneonethreeeight

Output:
nineninefourfourseven01138
"""
s=input().strip()
l=['zero','one','two','three','four','five','six','seven','eight','nine']
word=''
size=0
for i in s:
    if i.isnumeric():
        print(l[int(i)],end='')
    else:
        word+=i
        size+=1
        if size>=3:
            try:
                print(l.index(word),end='')
                word=''
                size=0
            except ValueError:
                pass
