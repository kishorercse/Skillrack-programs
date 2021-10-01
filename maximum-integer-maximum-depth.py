"""
The program must accept a string S as the input. The string S contains parentheses and integers, where each open
parenthesis '(' has a matching close parenthesis ')'. The program must print the integer that occurs in the maximum
depth of nested parentheses in S. If two or more integers occur in same maximum depth, then the program must
print the maximum value among those integers as the output.

Boundary Condition(s):
1 <= Length of S <= 100
1 <= Each integer value <= 10^5

Input Format:
The first line contains S.

Output Format:
The first line contains an integer representing the integer that occurs in the maximum depth of nested parentheses in S.

Example Input/Output 1:
Input:
10((40)30)(50(60(70)))20((80))

Output:
70

Explanation:
10 -> depth = 0
40 -> depth = 2
30 -> depth = 1
50 -> depth = 1
60 -> depth = 2
70 -> depth = 3
20 -> depth = 0
80 -> depth = 2
The integer with the maximum depth is 70.
Hence 70 is printed as the output.

Example Input/Output 2:
Input: 
(12(15)(50)(10(25(32)85)70)33(78((55)8)63)77)((((40)))) 

Output: 
55 

Explanation: 
There are three integers with the same maximum depth 4. 32, 55 and 40.
So the maximum value 55 is printed as the output.
"""
def check(depth,max_depth,t,num):
    if depth>max_depth:
        return depth,int(t)
    if depth==max_depth:
        return depth,max(num,int(t))
    return max_depth,num
s=input().strip()
depth=0
max_depth=0
num=-1
t=''
for i in s:
    if i=='(':
        if t:
            max_depth,num=check(depth,max_depth,t,num)
            t=''
        depth+=1
    elif i==')':
        if t:
            max_depth,num=check(depth,max_depth,t,num)
            t=''
        depth-=1
    else:
        t+=i
if t:
    max_depth,num=check(depth,max_depth,t,num)
print(num)
