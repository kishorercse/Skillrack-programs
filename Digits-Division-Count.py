"""
A number N is passed as input to the program. The program must print the count of digits which divide the number N without leaving a remainder.

Input Format:
The first line contains N

Output Format:
The first line contains the count of digits which divide N without leaving a remainder.

Boundary Conditions:
1 <= N <= 9999999999


Example Input/Output 1:
Input:
11012

Output:
4

Explanation:
The digits are 1 1 0 1 2. Division by zero is not defined. Hence that is excluded.
Three 1s and the 2 divide 11012 without leaving a remainder. Hence 4 is the output.

Example Input/Output 2:
Input:
209

Output:
0

Explanation:
None of the digits 2 or 9 divide 209 without leaving a remainder. Division by zero is undefined. Hence 0 is printed as the output.
"""
s=input().strip()
n=int(s)
count=0
for i in s:
    if i!='0' and n%(int(i))==0:
        count+=1
print(count)
