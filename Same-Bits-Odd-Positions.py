"""
The program must accept two integers X and Y as the input. The program must print an integer C whose binary representation indicates the same bits at the odd positions from
LSB(Least Significant Bit) of the integers X and Y. If there are no bits same at odd positions, then the program must print -1 as the output.

Boundary Condition(s):
1 <= X, Y <= 10^8

Input Format:
The first line contains X and Y separated by a space.

Output Format:
The first line contains C.

Example Input/Output 1:
Input:
109 107

Output:
5

Explanation:
109 -> 1101101
107 -> 1101011
1st position from LSB: Same bit 1
3rd position from LSB: Different bits
5th position from LSB: Same bit 0
7th position from LSB: Same bit 1
101 -> 5

Example Input/Output 2:
Input:
206 27

Output:
-1

Explanation:
206 -> 11001110
27 -> 00011011
1st position from LSB: Different bits
3rd position from LSB: Different bits
5th position from LSB: Different bits
7th position from LSB: Different bits
So -1 is printed.

Example Input/Output 3:
Input:
337 347

Output:
29

Explanation:
337 -> 101010001
347 -> 101011011
1st position from LSB: Same bit 1
3rd position from LSB: Same bit 0
5th position from LSB: Same bit 1
7th position from LSB: Same bit 1
9th position from LSB: Same bit 1
11101 -> 29
"""
x,y=map(int,input().split())
ans=0
p=1
while x>0 and y>0:
    if (x&1==y&1):
        ans+=p*(x&1)
        p=p<<1
    x=x>>2
    y=y>>2
if p==1:
    print(-1)
else:
    print(ans)
