"""
The program must accept two string values S1 and S2 as the input. The string S1 represents a message to be encrypted and it contains only lower case alphabets. The string S2 
represents a key to be used to encrypt the message. The length of the string S2 is always 27 and it contains all 26 lower case alphabets and a dot(.). The program must encrypt 
the string S1 and print the output based on the following conditions.
- The program must form three 3*3 square matrices.
- The program must fill the first square matrix with the first 9 characters of S2.
- The program must fill the second square matrix with the middle 9 characters of S2.
- The program must fill the third square matrix with the last 9 characters of S2.
- For each character CH in the string S1, the program must print the square matrix number, the row number and the column number of the character CH.

Boundary Condition(s):
1 <= Length of S1 <= 100

Input Format:
The first line contains S1.
The second line contains S2.

Output Format:
The first line contains a string representing the encrypted message.

Example Input/Output 1:
Input:
skillrack
abcdefghijklm.nopqrstuvwxyz

Output:
312212133213213311111113212

Explanation:
Here S1 = "skillrack" and S2 = "abcdefghijklm.nopqrstuvwxyz".

The first 3*3 square matrix is formed as
a b c
d e f
g h i

The second 3*3 square matrix is formed as
j k l
m . n
o p q

The third 3*3 square matrix is formed as
r s t
u v w
x y z

s -> 312 (3rd matrix, 1st row, 2nd column)
k -> 212 (2nd matrix, 1st row, 2nd column)
i -> 133 (1st matrix, 3rd row, 3rd column)
l -> 213 (2nd matrix, 1st row, 3rd column)
l -> 213 (2nd matrix, 1st row, 3rd column)
r -> 311 (3rd matrix, 1st row, 1st column)
a -> 111 (1st matrix, 1st row, 1st column)
c -> 113 (1st matrix, 1st row, 3rd column)
k -> 212 (2nd matrix, 1st row, 2nd column)

Example Input/Output 2:
Input:
ultraviolet
zyxwvutsrqponmlkjihgf.edcba

Output:
123223131133333122233213223322131
"""
s1=input().strip()
s2=input().strip()
pos={}
mat=row=col=1
for i in s2:
    pos[i]=str(mat)+str(row)+str(col)
    col+=1
    if col==4:
        col=1
        row+=1
        if row==4:
            mat+=1
            row=1
for i in s1:
    print(pos[i],end='')
