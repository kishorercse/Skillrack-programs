"""
The program must accept a matrix of size R*C containing only digits as the input. The values of R and C are always divisible by 3. For each 3*3 submatrix in the given matrix,
the program must form 8 integers by concatenating the digits as given below.
- Row wise(3 integers - left to right)
- Column wise(3 integers - top to bottom)
- Diagonal wise (2 integers - top-left to bottom-right and top-right to bottom-left)
Finally, the program must print all the integers obtained in sorted order as the output.

Boundary Condition(s):
3 <= R, C <= 48
0 <= Matrix element value <= 9

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C integers separated by a space.

Output Format:
The first line contains ((R/3)*(C/3))*8 integers separated by a space.

Example Input/Output 1:
Input:
3 6
1 2 3 1 4 5
4 5 6 7 2 6
7 8 9 8 9 3

Output:
123 123 145 147 159 178 258 357 369 429 456 528 563 726 789 893

Explanation:
The 8 integers from the first 3*3 submatrix are given below.
123, 456, 789, 147, 258, 369, 159 and 357.

The 8 integers from the second 3*3 submatrix are given below.
145, 726, 893, 178, 429, 563, 123 and 528.

So the resulting 16 integers are printed in sorted order.

Example Input/Output 2:
Input:
6 6
1 2 8 7 0 3
0 7 0 3 9 3
3 1 5 6 7 1
0 4 0 8 7 9
2 9 5 6 4 0
9 6 7 4 7 4

Output:
29 40 57 70 97 97 99 103 128 175 271 295 315 331 393 396 474 496 640 671 703 736 747 791 805 844 864 873 879 904 944 967
"""
r,c=map(int,input().split())
m=[input().split() for _ in range(r)]
res=[]
for i in range(0,r,3):
    for j in range(0,c,3):
        a=[0]*8
        for k in range(3):
            a[0]=a[0]*10+int(m[i][j+k])
            a[1]=a[1]*10+int(m[i+1][j+k])
            a[2]=a[2]*10+int(m[i+2][j+k])
            a[3]=a[3]*10+int(m[i+k][j])
            a[4]=a[4]*10+int(m[i+k][j+1])
            a[5]=a[5]*10+int(m[i+k][j+2])
            a[6]=a[6]*10+int(m[i+k][j+k])
            a[7]=a[7]*10+int(m[i+k][c-(j+k)-1])
        res+=a
print(*sorted(res))
