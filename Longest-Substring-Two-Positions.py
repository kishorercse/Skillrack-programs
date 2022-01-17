"""
The program must accept a string S and Q queries as the input. Each query contains two integers X and Y representing the positions of two characters in the string S. For each 
query, the program must print the length of the longest common substring starting from the given two positions X and Y.

Boundary Condiiton(s):
2 <= Length of S <= 100
1 <= Q <= 100
1 <= X, Y <= Length of S

Input Format:
The first line contains S.
The second line contains Q.
The next Q lines, each contains two integers X and Y representing the positions of two characters in the string S.

Output Format:
The first Q lines, each contains the length of the longest common substring starting from the given two positions X and Y.

Example Input/Output 1:
Input:
cdcdcdacdcdcDcDCD
3
1 3
2 7
1 8

Output:
4
0
5

Explanation:
1st query: X = 1 and Y = 3.
The longest common substring is cdcd, whose length is 4.
So 4 is printed as the output.

2nd query: X = 2 and Y = 7.
There is no longest common substring.
So 0 is printed as the output.

3rd query: X = 1 and Y = 8.
The longest common substring is cdcdc, whose length is 5.
So 5 is printed as the output.

Example Input/Output 2:
Input:
cellCellscellcellcell
4
1 5
6 2
10 1
10 14

Output:
0
3
4
8
"""
s=input().strip()
q=int(input())
l=len(s)
for _ in range(q):
    x,y=map(int,input().split())
    res=0
    x-=1
    y-=1
    while x<l and y<l and s[x]==s[y]:
        res+=1
        x+=1
        y+=1
    print(res)
