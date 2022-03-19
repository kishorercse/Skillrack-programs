"""
There are R*C cities arranged as a matrix. A boy wants to visit the cities starting from the city (X, Y). Then the boy visits the rest of the cities according to the
instructions given.
- If it is N, then he goes to the next non-visited city in the direction North.
- If it is E, then he goes to the next non-visited city in the direction East.
- If it is W, then he goes to the next non-visited city in the direction West.
- If it is S, then he goes to the next non-visited city in the direction South.
- If there is no next non-visited city in a given direction, then he goes to the last city in that direction.
The program must accept the values of R, C, X, Y and a string S representing the instructions given to the boy as the input. The program must print the position of 
the city in which he is located after processing the given instructions as the output.

Boundary Condition(s):
2 <= R, C <= 25
1 <= X <= R
1 <= Y <= C
1 <= Length of S <= 50

Input Format:
The first line contains R, C, X and Y separated by a space.
The second line contains S.

Output Format:
The first line contains two integers separated by a space representing the position of the city based on the given conditions.

Example Input/Output 1:
Input:
5 5 4 3
NNESWWES

Output:
4 5

Explanation:
Here R = 5, C = 5, X = 4 and Y = 3.
The boy starts from the city (4, 3).
N -> The next non-visited city in the direction North is (3, 3).
N -> The next non-visited city in the direction North is (2, 3).
E -> The next non-visited city in the direction East is (2, 4).
S -> The next non-visited city in the direction South is (3, 4).
W -> The next non-visited city in the direction West is (3, 2).
W -> The next non-visited city in the direction West is (3, 1).
E -> The next non-visited city in the direction East is (3, 5).
S -> The next non-visited city in the direction South is (4, 5).
Now the boy is in the city (4, 5).
Hence the output is
4 5

Example Input/Output 2:
Input:
2 4 1 1
SEEEWNESEN

Output:
1 4
"""
r,c,x,y=map(int,input().split())
s=input().strip()
x-=1
y-=1
m=[[False for j in range(c)]for i in range(r)]
m[x][y]=True
for ch in s:
    if ch=='N':
        rd,cd=-1,0
    elif ch=='S':
        rd,cd=1,0
    elif ch=='E':
        rd,cd=0,1
    else:
        rd,cd=0,-1
    while x>=0 and x<r and y>=0 and y<c and m[x][y]:
        x+=rd
        y+=cd
    if x<0 or x>=r or y<0 or y>=c:
        x-=rd
        y-=cd
    else:
        m[x][y]=True
print(x+1,y+1)
