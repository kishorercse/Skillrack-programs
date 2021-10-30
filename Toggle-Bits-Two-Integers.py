"""
The program must accept two integers X and Y as the input. The program must find the binary representations of X and Y. Then the program must toggle the bits in X if there are set
bits in Y at the same position from LSB(Least Significant Bit). Then the program must print the revised value of X as the output.

Boundary Condition(s): 
1 <= Y <= X <= 10^8 

Input Format: 
The first line contains X and Y separated by a space. 

Output Format: 
The first line contains the revised value of X. 

Example Input/Output 1: 
Input:
11 5 

Output:
14 

Explanation: 
X = 11 -> 1011.
Y = 5 -> 0101. 
The 1st bit and 3rd bit from LSB are the set bits in Y. 
So the 1st bit and 3rd bit from LSB are toggled in X. 
X -> 1011 -> 1110 -> 14. 

Example Input/Output 2: 
Input: 
615 218 

Output: 
701
"""
x,y=map(int,input().split())
t=1
while y>0:
    if y&1==1:
        x=x^t
    t=t<<1
    y=y>>1
print(x)
