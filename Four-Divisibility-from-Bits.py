"""
The program must accept the last three or more bits of an integer N as the input. The program must print Yes if N is divisible by four. Else the program must print No as the 
output.

Boundary Condition(s):
3 <= Number of bits in the binary representation of N <= 30

Input Format:
The first line contains the last three or more bits of the integer N.

Output Format:
The first line contains Yes or No.

Example Input/Output 1:
Input:
1110

Output:
No

Explanation:
The binary representation of any integer ending with 1110 is not divisible by 4.
Hence the output is No

Example Input/Output 2:
Input:
111100

Output:
Yes

Example Input/Output 3:
Input:
11111

Output:
No
"""
if int(input(),2)%4==0:
    print("Yes")
else:
    print("No")
