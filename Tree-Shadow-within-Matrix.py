"""
Certain number of trees are planted in a rectangular matrix field. The trees were planted in an R*C rectangular matrix but certain trees did not grow due to lack of 
ground water. Hence the cells in the matrix which have the trees are indicated by 1 and the cells which do not have trees in it are indicated by 0.

The shadow of the trees always falls on the adjacent cell depending on the direction of the sunlight (The direction of the sunlight can be left-L, right-R, front-F 
and back-B of the rectangular field). The shadow of a tree does not fall on the ground within the rectangular field if the adjacent cell has a tree. The program must
print the count of trees whose shadow falls within the rectangular field (The trees whose shadow falls outside the rectangular matrix field must not be counted. This
happens when the trees are along the border and their shadow is outside the rectangular matrix field).

Input Format:
The first line contains R and C separated by a space.
Next R lines contain C values (either 1 or 0) indicating the presence of trees.
(R+2)th line contains the direction of the sunlight.

Output Format:
The first line contains the count of the trees whose shadow falls within the rectangular matrix field.

Boundary Conditions:
2 <= R, C <= 50

Example Input/Output 1:
Input:
3 5
1 0 0 1 0
0 1 0 1 1
1 1 1 0 0
L

Output:
4

Explanation:
The position of the sun is left with respect to the rectangular matrix field. Hence the trees whose shadow will be to the right of the trees. The trees whose shadow 
fall on the ground within the rectangular matrix field are indicated by X.

X 0 0 X 0
0 X 0 1 1
1 1 X 0 0

Example Input/Output 2:
Input:
3 5
1 0 0 1 0
0 1 0 1 1
1 1 1 0 0
B
 
Output:
3

Explanation:
The position of the sun is behind the rectangular matrix field. Hence the shadow will fall in the opposite direction. Hence the trees whose shadow fall on the ground 
within the rectangular matrix field are indicated by X.
    
X 0 0 1 0
0 1 0 X X
1 1 1 0 0
"""
r,c=map(int,input().split())
m=[input().split() for _ in range(r)]
d=input().strip()
count=0
if d=='L':
    a,b=0,1
elif d=='R':
    a,b=0,-1
elif d=='B':
    a,b=1,0
else:
    a,b=-1,0
for i in range(r):
    for j in range(c):
        if m[i][j]=='1':
            x,y=a+i,b+j
            if x>=0 and x<r and y>=0 and y<c and m[x][y]=='0':
                count+=1
print(count)
