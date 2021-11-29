"""
The program must accept three integers X, Y and K as the input. The program must form a string with lower case alphabets starting from the Xth alphabet to the Yth alphabet in 
the English alphabet set. The program must stretch the string as short as possible so that the string contains at least K characters. A stretch is to repeat each character in 
a string the same number of times. Then the program must print the resulting string as the output.

Boundary Condition(s):
1 <= X < Y <= 26
1 <= K <= 1000

Input Format:
The first line contains X, Y and K separated by a space.

Output Format:
The first line contains the resulting string.

Example Input/Output 1:
Input:
1 5 13

Output:
aaabbbcccdddeee

Explanation:
Here X = 1, Y = 5 and K = 13.
1st lower case alphabet is 'a'.
5th lower case alphabet is 'e'.
So the string is formed as "abcde".
Then the string is stretched as "aaabbbcccdddeee" whose length is 15 (13 <= 15).

Example Input/Output 2:
Input:
1 5 20

Output:
aaaabbbbccccddddeeee

Example Input/Output 3:
Input:
24 25 9

Output:
xxxxxyyyyy
"""
x,y,k=map(int,input().split())
d=y-x+1
d=k//d + (k%d!=0)
for i in range(x,y+1):
    print(chr(96+i)*d,end='')
