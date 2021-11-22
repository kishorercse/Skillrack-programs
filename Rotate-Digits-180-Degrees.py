"""
The program must accept an integer N as the input. The program must form an integer X by rotating the each digit 180 degrees based on the following conditions.
- The digits 2 and 5 rotate to each other.
- The digits 6 and 9 rotate to each other.
- For the remaining digits (0, 1, 3, 4, 7 and 8), they remain the same. 
Finally, the program must print the sum of N and X as the output.

Boundary Condition(s):
1 <= N <= 10^8

Input Format:
The first line contains N. 

Output Format:
The first line contains the sum of N and X. 

Example Input/Output 1: 
Input: 
10672 

Output:
21647 

Explanation:
Here N = 10672.
After rotating each digit by 180 degrees, the integer becomes 10975.
The sum of 10672 and 10975 is 21647. 
So 21647 is printed as the output. 

Example Input/Output 2: 
Input: 
5599

Output: 
7865
"""
s=input().strip()
x=''
for i in s:
    if i=='2':
        x+='5'
    elif i=='5':
        x+='2'
    elif i=='6':
        x+='9'
    elif i=='9':
        x+='6'
    else:
        x+=i
print(int(s)+int(x))
