"""
The program must accept integer values in L-shape or inverted L-shape as the input. The program must flip the given shape diagonally and print the integers as the output. The 
empty spaces must be printed as asterisks. 
Note: Both the edges of L and inverted L have an equal length (i.e., an equal number of integers in both the edges). 

Input Format: 
The lines contain the integer values in L-shape or inverted L-shape. 

Output Format:
The lines contain the integer values and asterisks based on the given conditions. 

Example Input/Output 1: 
Input:
1 2 3 4 5
6
7
8
9

Output:
* * * * 5 
* * * * 4 
* * * * 3 
* * * * 2 
9 8 7 6 1 

Explanation:
The integers occur in the inverted L-shape. So they are flipped diagonally and printed as the output.

Example Input/Output 2: 
Input: 
1 
2
3
4 5 6 7

Output: 
1 2 3 4 
* * * 5
* * * 6 
* * * 7

Explanation: 
The integers occur in the L-shape. So they are flipped diagonally and printed as the output.
"""
l=input().split()
t=len(l)
if t>1:
    l=[l]
    s='*'*(t-1)
    for i in range(t-1,0,-1):
        l.append(input().strip())
        print(*s,l[0][i])
    l[0]=l[0][0]
    for i in range(t-1,-1,-1):
        print(l[i],end=' ')
else:
    i=1
    print(l[0],end=' ')
    while True:
        s=input().split()
        if len(s)>1:
            break
        print(s[0],end=' ')
        i+=1
    print(s[0])
    t='*'*i
    for j in range(1,i+1):
        print(*t,s[j])
