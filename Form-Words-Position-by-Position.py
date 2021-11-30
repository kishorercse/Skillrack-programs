"""
The program must accept a space separated string S and must form the first word by considering the first letter of all the words in S. The program must form the second word by
considering the second letter of all the words in S and so on. Finally the program must print all the words thus formed.

Boundary Condition(s):
1 <= Length of S <= 1000

Input Format:
The first line contains S.

Output Format:
The first line contains the words formed from the string S.

Example Input/Output 1:
Input:
Please get up in the morning

Output:
Pguitm lepnho eter an si en g

Explanation:
1st word: Pguitm (1st letter of the words in "Please get up in the morning")
2nd word: lepnho (2nd letter of the words in "Please get up in the morning")
3rd word: eter (3rd letter of the words in "Please get up in the morning")
4th word: an (4th letter of the words in "Please get up in the morning")
5th word: si (5th letter of the words in "Please get up in the morning")
6th word: en (6th letter of the words in "Please get up in the morning")
7th word: g (7th letter of the words in "Please get up in the morning")

Example Input/Output 2:
Input:
A OX RAT BEAR MOUSE SPIDER GIRAFFE KANGAROO CROCODILE RHINOCEROS

Output:
AORBMSGKCR XAEOPIARH TAUIRNOI RSDAGCN EEFAOO RFRDC EOIE OLR EO S
"""
lst=input().split()
n=len(lst)
maxLen=len(max(lst,key=len))
res=['']*maxLen
for i in range(maxLen):
    for j in range(n):
        try:
            res[i]+=lst[j][i]
        except IndexError:
            pass
print(*res)
