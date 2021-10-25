"""
There are N stones in a row. A boy is standing on the 1st stone and J jumping instructions are given to boy. The boy jumps on the stones based on the given instructions. He can 
only jump from one stone to the next or to the previous stone at a time. The value of N and the J instructions are passed as the input. The program must print the way the boy 
jumps on the N stones as the output. The stones must be printed as hyphens and the boy must be printed as an asterisk. 

Boundary Condition(s): 
2 <= N <= 50 
1 <= J <= 50 

Input Format: 
The first line contains N. 
The second line contains J. 
The third line contains J integer values separated by a space.

Output Format: 
The lines contain the way the boy jumps on the N stones.

Example Input/Output 1: 
Input: 
5 
5 
3 1 4 5 3 

Output: 
* - - - - 
- * - - -
- - * - -
- * - - -
* - - - -
- * - - -
- - * - -
- - - * -
- - - - *
- - - * -
- - * - -

Explanation:
Initial position of the boy is 1.
1 -> 3 -> 1 -> 4 -> 5 -> 3. 

Example Input/Output 2: 
Input: 
6 
5 
2 3 6 1 4 

Output: 
* - - - - -
- * - - - -
- - * - - -
- - - * - -
- - - - * -
- - - - - *
- - - - * -
- - - * - -
- - * - - -
- * - - - -
* - - - - -
- * - - - -
- - * - - -
- - - * - -
"""
n=int(input())
j=int(input())
l=list(map(int,input().split()))
s=['-']*n
pos=0
for i in l:
    p=s[:]
    if i>=pos:
        for j in range(pos+1,i+1):
            p[j-1]='*'
            print(*p)
            p=s[:]
    else:
        for j in range(pos-1,i-1,-1):
            p[j-1]='*'
            print(*p)
            p=s[:]
    pos=i
