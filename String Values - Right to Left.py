"""
The program must accept N string values as the input. The program must print the last characters of all N string values. Then the program must print the last but one characters of
all N string values. Then the program must print the last but two characters of all N string values. Similarly, the program must print the remaining characters of all N string 
values as the output.

Boundary Condition(s): 
2 <= N <= 100 
1 <= Length of each string <= 100 

Input Format: 
The first line contains N. 
The next N lines, each contains a string value. 

Output Format: 
The first line contains a string value representing the characters of N string values based on the given conditions. 

Example Input/Output 1: 
Input: 
4 
Pencil 
paper
NOTEBOOK 
crayons 

Output:
lrKsieOncpOonaByepEaPTrOcN 

Explanation: 
The given 4 strings are Pencil, paper, NOTEBOOK and crayons. 
The last characters of the 4 string values are l, r, K and s. So lrKs is printed. 
The last but one characters of the 4 string values are i, e, O and n. So ieOn is printed. 
Similarly, the remaining characters are printed. 
Hence the output is lrKsieOncpOonaByepEaPTrOcN 

Example Input/Output 2: 
Input: 
5 
cookie
TEA 
Noodles 
Candy 
CoFFee 

Output: 
eAsyeiEedekTlnFodaFooCocoCN
"""
n=int(input())
a=[]
mx=0
for _ in range(n):
    s=input().strip()
    mx=max(len(s),mx)
    a.append(s)
pos=-1
mx=-mx
while pos>=mx:
    for i in range(n):
        try:
            print(a[i][pos],end='')
        except IndexError:
            pass
    pos-=1
