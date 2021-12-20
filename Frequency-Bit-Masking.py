"""
The program must accept a string S containing only lower case alphabets as the input. The program must generate integer values based on the following conditions.
- The binary representation of the first integer indicates the presence of first occurrence of alphabets in S.
- The binary representation of the second integer indicates the presence of second occurrence of alphabets in S.
- The binary representation of the third integer indicates the presence of third occurrence of alphabets in S.
- Similarly, the program must generate the integer values for the remaining alphabets.
In each integer value, the 26-bits from LSB(least significant bit) to MSB(most significant bit) are mapped to the 26 lower case alphabets(a-z).
- Each 1 in the binary representation indicates the presence of the corresponding lower case alphabet.
- Each 0 in the binary representation indicates the absence of the corresponding lower case alphabet.

Boundary Condition(s):
1 <= Length of S <= 100

Input Format:
The first line contains S.

Output Format:
The lines, each contains an integer value as per the given conditions.

Example Input/Output 1:
Input:
abcacbca

Output:
7
7
5

Explanation:
The alphabet a occurs thrice.
The alphabet b occurs twice.
The alphabet c occurs thrice.
1st integer: 7 -> 111 (It indicates the presence first occurrence of c b and a).
2nd integer: 7 -> 111 (It indicates the presence second occurrence of c b and a).
3rd integer: 5 -> 101 (It indicates the presence third occurrence of c and a).

Example Input/Output 2:
Input:
skillrack

Output:
396549
3072
"""
s=input().strip()
d={}
mx=-1
for i in s:
    d[i]=d.get(i,0)+1
    mx=max(mx,d[i])
for i in range(mx):
    n=0
    for i in d:
        if d[i]>0:
            n|=(1 << (ord(i)-97))
            d[i]-=1
    print(n)
