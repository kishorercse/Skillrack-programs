"""
The program must accept a matrix of size N*N representing a chessboard. The chessboard contains a certain number of queens(Q), a king(K) and the remaining empty cells are marked
by the asterisks. The program must print the shortest distance between the king and a queen (i.e. the nearest queen that can attack the king directly). If no queen attacks the 
king, the program must print -1 as the output. 

Queen: In Chess, a queen can move any direction diagonally. The queen can also move left or right along the row it is present. The queen can also move up or down along the column
it is present. The movement can happen till the end of the board is reached or another piece (like Rook, Knight, Bishop, Pawn etc is encountered). 

Boundary Condition(s): 
2 <= N <= 50 

Input Format:
The first line contains N.
The next N lines each contains N characters separated by a space representing the chessboard.

Output Format:
The first line contains an integer value representing the shortest distance between the king and a queen.

Example Input/Output 1:
Input: 
8
* * * * * * * *
* * * * Q * * *
* * * * * * * *
* * * K * * * *
* * * * * * * *
* Q * * * * * *
* * * * * * Q *
* * * * * * * *

Output: 
2 

Explanation: 
There are 3 queens in the chessboard that occur in the positions (2, 5), (6, 2) and (7, 7).
The 2nd and 3rd queens can attack the king. 
The distance between the king and the 2nd queen is 2. 
The distance between the king and the 3rd queen is 3. 
The shortest distance is 2 which is printed as the output.

Example Input/Output 2:
Input:
7
* * * * * * *
Q * * * * Q Q
* * * Q * Q Q
* K * * Q * Q
* * * * * * *
* * * * * * *
* * Q Q * * *

Output:
3 

Example Input/Output 3: 
Input:
4
* Q * *
* * * K
* * * *
Q * * *

Output:
-1
"""
n=int(input())
m=[]
for i in range(n):
    t=input().split()
    m.append(t)
    try:
        b=t.index('K')
        a=i
    except ValueError:
        pass
min_distance=n
for i in range(n):
    for j in range(n):
        if m[i][j]=='Q':
            if i==a:
                min_distance=min(abs(j-b),min_distance)
            elif j==b:
                min_distance=min(abs(i-a),min_distance)
            elif abs(i-a)==abs(j-b):
                min_distance=min(abs(i-a),min_distance)
if min_distance==n:
    print(-1)
else:
    print(min_distance)
