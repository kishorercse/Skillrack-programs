"""
To begin the game, let us say a word W is considered as the first word. The second word is the word which has the last letter of the first word as it's first letter. So for any
following word, it's first letter must be equal to the last letter of the previous word.

The first word and a positive integer value C is passed as the input. The program must print the Cth word.

Input Format:
The first line will contain N.
Next N lines will contain N words.
(N+2)nd line will contain C.
(N+3)rd line will contain W.

Output Format:
The first line will contain the Cth word as per the game rules described above.

Boundary Conditions:
2 <= N <= 26

Example Input/Output 1:
Input:
6
egg
tiger
rampage
goat
wrist
mirror
3
egg

Output:
tiger

Explanation:
The words in the game sequence are egg, goat, tiger, rampage, egg  and so on. So the 3rd word tiger is printed as the output.
"""
n=int(input())
l=[input().strip() for _ in range(n)]
c=int(input())
w=input().strip()
for i in range(c-1):
    for j in range(n):
        if w[-1]==l[j][0]:
            w=l[j]
            break
print(w)
