"""
The program must accept an integer N as the input. The program must find the binary representation of the integer N. Then the program must form a new number X based on the
following conditions.
- The program must find the octal equivalent of three bits from LSB. Then the program must find the hexadecimal equivalent of the next four bits. Then the program must find the
octal equivalent of the next three bits, and so on.
- Then the program must combine the resulting digits to create the number X.
Finally, the program must print the value of X as the output.

Boundary Condition(s):
1 <= N <= 10^8

Input Format:
The first line contains N.

Output Format:
The first line contains X.

Example Input/Output 1:
Input:
5980

Output:
56B4

Explanation:
Here N = 5980.
5980 -> 1011101011100 -> 0101 110 1011 100
100 -> 4 (octal)
1011 -> B (hexadecimal)
110 -> 6 (octal)
0101 -> 5 (hexadecimal)
After combining the resulting digits, the value of X becomes 56B4.
Hence the output is 56B4.

Example Input/Output 2:
Input:
108799

Output:
6A1F7

Explanation:
Here N = 108799.
108799 -> 11010100011111111 -> 110 1010 001 1111 111
111 -> 7 (octal)
1111 -> F (hexadecimal)
001 -> 1 (octal)
1010 -> A (hexadecimal)
110 -> 6 (octal)
After combining the resulting digits, the value of X becomes 6A1F7.
Hence the output is 6A1F7.
"""
def base(n,b):
    ans=0
    t=1
    while n:
        if n[-1]=='1':
            ans|=t
        n=n[:-1]
        t<<=1
    if b==16 and ans>9:
        return chr(ans+55)
    return str(ans)
n=bin(int(input()))[2:]
s=''
f=True
while n:
    if f:
        s=base(n[-3:],8)+s
        n=n[:-3]
    else:
        s=base(n[-4:],16)+s
        n=n[:-4]
    f=not f
print(s)
