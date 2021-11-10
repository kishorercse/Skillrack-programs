"""
The program must accept an integer N as the input. To display each digit in N, a seven segment display is used. Each seven segment display has seven switches named a, b, c, d, e, 
f, g and each switch corresponds to a segment to be displayed as given below. 
Top segment - a 
Top-right segment - b 
Bottom-right segment - c 
Bottom segment - d 
Bottom-left segment - e 
Top-left segment - f 
Middle segment - g 
The states of 7 switches(1 - ON, 0 - OFF) to display 10 digits are given below. 
0 -> 1111110 
1 -> 0110000 
2 -> 1101101 
3 -> 1111001 
4 -> 0110011 
5 -> 1011011 
6 -> 1011111 
7 -> 1110000 
8 -> 1111111 
9 -> 1111011 
The program must form an integer D by concatenating the states of seven switches to display each digit in N. Then the program must print the value of D as the output.

Boundary Condition(s):
1 <= N < 10^9 

Input Format: 
The first line contains N.

Output Format: 
The first line contains D.

Example Input/Output 1:
Input: 
504 

Output: 
1507123 

Explanation:
5 -> 1011011
0 -> 1111110
4 -> 0110011
504 -> 101101111111100110011 -> 1507123 

Example Input/Output 2:
Input: 
618235 

Output: 
3277328186587 

Explanation:
6 -> 1011111
1 -> 0110000
8 -> 1111111
2 -> 1101101
3 -> 1111001
5 -> 1011011
618235 -> 101111101100001111111110110111110011011011 -> 3277328186587 
"""
n=input().strip()
l=['1111110','0110000','1101101','1111001','0110011','1011011','1011111','1110000','1111111','1111011']
s=''
for i in n:
    s+=l[int(i)]
print(int(s,2))
