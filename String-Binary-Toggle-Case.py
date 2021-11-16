"""
The program must accept a string S and an integer X as the input. The program must print two string values based on the following conditions. 
- For each 1s from MSB in the binary representation of X, the program must toggle the characters in the same position to upper case and for each 0s, the program must toggle the 
characters to lower case. The remaining characters in the string S must not be altered. Then the program must print the modified string in the first line of output.
- For each 1s from LSB in the binary representation of X, the program must toggle the characters in the same position to upper case and for each 0s, the program must toggle the
characters to lower case. The remaining characters in the string S must not be altered. Then the program must print the modified string in the second line of output.

Note: 
The length of the string S is always greater than or equal to the number of bits in the binary representation of X. 

Boundary Condition(s): 
1 <= Length of S <= 100 
1 <= X <= 10^8 

Input Format:
The first line contains S.
The second line contains X. 

Output Format:
The first line contains a string value. 
The second line contains a string value.

Example Input/Output 1:
Input:
BasketBall 
23 

Output: 
BaSKEtBall
BaskeTbALL

Explanation: 
Here the given string is BasketBall and the value of K is 23. 
The binary representation of 23 is 10111. 
BasketBall -> BaSKEtBall
BasketBall -> BaskeTbALL 

Example Input/Output 2: 
Input:
PAPER 
10 

Output:
PaPeR
PApEr
"""
s=list(input().strip())
temp=s[:]
x=int(input())
t=bin(x)[2:]
a=0
b=len(s)-len(t)
for i in t:
    if i=='1':
        s[a]=s[a].upper()
        temp[b]=temp[b].upper()
    else:
        s[a]=s[a].lower()
        temp[b]=temp[b].lower()
    a+=1
    b+=1
print(*s,sep='')
print(*temp,sep='')
