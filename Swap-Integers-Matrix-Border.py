"""
The program must accept an integer matrix of size R*C and two integers X, Y as the input. The program must find the Xth integer and the Yth in the border of the given matrix. 
Consider the border elements of the matrix circularly in the clockwise direction when finding the Xth and Yth integers. Then the program must swap those two integers in the
matrix. Finally, the program must print the revised matrix as the output.

Boundary Condition(s):
2 <= R, C <= 50
1 <= Matrix element value <= 1000
1 <= X, Y <= 10^6

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C integer values separated by a space.
The R+2nd line contains X and Y separated by a space.

Output Format:
The first R lines contain the revised matrix.

Example Input/Output 1:
Input:
5 4
46 14 63 96
36 85 67 41
77 81 91 60
83 13 57 56
97 80 72 68
3 24

Output:
46 14 80 96
36 85 67 41
77 81 91 60
83 13 57 56
97 63 72 68

Explanation:
Here X = 3 and Y = 24.
The 3rd integer in the border is 63.
The 24th integer in the border is 80.
After swapping the integers 63 and 80, the matrix becomes
46 14 80 96
36 85 67 41
77 81 91 60
83 13 57 56
97 63 72 68

Example Input/Output 2:
Input:
3 3
1 2 3
4 5 6
7 8 9
9 20

Output:
6 2 3
4 5 1
7 8 9
"""
def findPosition(p):
    if p<c:
        return (0,p)
    elif p<c+r-1:
        return (p-(c-1),c-1)
    elif p<2*c+r-2:
        return (r-1,c-(p-c-(r-1))-2)
    else:
        return (r-(p-c-(r-1)-(c-1))-2,0)
r,c=map(int,input().split())
m=[input().split() for _ in range(r)]
x,y=map(int,input().split())
n=2*(r+c-2)
x=(x-1)%n
y=(y-1)%n
a1,b1=findPosition(x)
a2,b2=findPosition(y)
m[a1][b1],m[a2][b2]=m[a2][b2],m[a1][b1]
for i in m:
    print(*i)
