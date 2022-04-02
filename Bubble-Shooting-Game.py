"""
In a bubble shooting game, there are N*N bubbles in Red, Green and Blue. The program must accept a character matrix of size N*N representing the colors of the bubbles
and Q queries as the input. Each query contains three values D, P and C.
- D represents the direction in which the player can shoot (L - Left, R - Right, T - Top, B - Bottom).
- P represents the position of a row or column in which the player can shoot.
- C represents the color of the bullet given to the player.
For each query, the player plays the game with the following rules.
- The player can shoot a bubble using a bullet with the same color in the specified direction D and the specified position P.
- If two or more bubbles have the same color, then the first occurring bubble in the specified direction will explode.
- If there is no bubble to shoot with the given bullet, then the player will ignore the bullet.
Finally, the program must print the modified matrix and the number of bullets he ignored as the output.
Note: The empty spaces in the matrix must be replaced with asterisks.

Boundary Condition(s):
2 <= N <= 50
1 <= P <= N
1 <= Q <= 1000

Input Format:
The first line contains N.
The next N lines, each contains N characters separated by a space representing the colors of the bubbles.
The N+2nd line contains Q.
The next Q lines, each contains D, P and C separated by a space.

Output Format:
The first N lines, each contains N characters separated by a space.
The N+1st line contains an integer representing the number of bullets the player ignored.

Example Input/Output 1:
Input:
5
R G G B G
B B R R R
G R B B B
R R R G R
G B R B G
6
T 3 R
L 2 R
R 4 B
B 1 G
R 3 R
T 1 G

Output:
R G G B G
B B * * R
* * B B B
R R R G R
* B R B G
1

Explanation:
Here Q = 6.
1st query -> The player can shoot the first occurring Red bubble from the Top in the 3rd column.
2nd query -> The player can shoot the first occurring Red bubble from the Left in the 2nd row.
3rd query -> There is no Blue bubble in the 4th row. He ignores the Blue bullet.
4th query -> The player can shoot the first occurring Green bubble from the Bottom in the 1st column.
5th query -> The player can shoot the only Red bubble from the Right in the 3rd row.
6th query -> The player can shoot the only Green bubble from the Top in the 1st column.
The remaining bubbles in the matrix are given below.
R G G B G
B B * * R
* * B B B
R R R G R
* B R B G
The player ignores only 1 bullet, so 1 is printed in the last line.

Example Input/Output 2:
Input:
4
R B G G
R B R G
B B B R
B G B R
8
T 1 R
T 2 G
B 3 B
B 4 R
L 1 G
L 2 B
R 3 R
R 4 B

Output:
* B * G
R * R G
B B B *
* * * *
0
"""
n=int(input())
mat=[input().split() for _ in range(n)]
q=int(input())
ignored=0
for _ in range(q):
    d,p,c=input().split()
    p=int(p)-1
    s,e,diff=0,n,1
    if d in "BR":
        s,e,diff=n-1,-1,-1
    if d in "TB":
        for i in range(s,e,diff):
            if mat[i][p]==c:
                mat[i][p]='*'
                break
        else:
            ignored+=1
    else:
        for j in range(s,e,diff):
            if mat[p][j]==c:
                mat[p][j]='*'
                break
        else:
            ignored+=1
for i in mat:
    print(*i)
print(ignored)
