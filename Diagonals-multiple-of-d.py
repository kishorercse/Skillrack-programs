"""
The program must accept an integer matrix of size R*C and a nonzero digit D as the input. The program must print the integers till the first occurring multiple of D in each top-left to bottom-right diagonal in separate lines. If there is no multiple of D in a diagonal, then all integers in that diagonal must be printed as the output. Boundary Condition(s): 2 <= R, C <= 25 1 <= D <= 9 Input Format: The first line contains R and C separated by a space. The next R lines, each contains C integers separated by a space. Output Format: The first (R+C-1) lines, each contains the integer values separated by a space. Example Input/Output 1: Input: 5 6 97 87 44 59 21 91 93 91 51 90 68 35 36 24 45 93 74 41 21 15 65 47 78 37 92 77 57 32 59 74 5 Output: 92 21 77 36 15 93 24 65 97 91 45 87 51 93 78 74 44 90 59 68 41 21 35 91 Explanation: Here R = 5 and C = 6, so there are 10 (5+6-1) top-left to bottom-right diagonals are present in the given matrix. The value of D is 5. The integers in all 10 diagonals are given below. 1st diagonal -> 92 2nd diagonal -> 21 77 3rd diagonal -> 36 15 57 4th diagonal -> 93 24 65 32 5th diagonal -> 97 91 45 47 59 6th diagonal -> 87 51 93 78 74 7th diagonal -> 44 90 74 37 8th diagonal -> 59 68 41 9th diagonal -> 21 35 10th diagonal -> 91 So the integers till the first occurring multiple of 5 in each diagonal are printed as the output. Example Input/Output 2: Input: 8 4 99 81 82 48 68 34 51 28 89 92 89 23 58 75 84 48 94 86 91 21 92 58 48 30 27 49 94 88 38 98 16 65 9 Output: 38 27 92 49 16 94 58 94 65 58 86 48 88 89 75 91 30 68 92 84 21 99 81 82 28 48
"""
r,c=map(int,input().split())
m=[list(map(int,input().split())) for _ in range(r)]
d=int(input())
for i in range(r-1,-1,-1):
    a,b=i,0
    while a<r and b<c:
        print(m[a][b],end=' ')
        if m[a][b]%d==0:
            break
        a+=1
        b+=1
    print()
for j in range(1,c):
    a,b=0,j
    while a<r and b<c:
        print(m[a][b],end=' ')
        if m[a][b]%d==0:
            break
        a+=1
        b+=1
    print()
