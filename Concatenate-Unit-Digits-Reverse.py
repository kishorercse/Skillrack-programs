"""
The program must accept N integers as the input. The program must form an integer X by concatenating the unit digits of the N integers in reverse order. Then the program must 
print the integer X as the output. Note: The integer X should not have any leading zeros. 

Boundary Condition(s):
1 <= N <= 18
1 <= Each integer value <= 1000

Input Format:
The first line contains N. 
The second line contains N integers. 

Output Format:
The first line contains the integer X.

Example Input/Output 1:
Input:
3 
45 78 19 

Output:
985 

Explanation: 
The unit digits of 45, 78 and 19 are 5, 8 and 9 respectively. So the integer X will be 985. 

Example Input/Output 2: 
Input: 
5
223 74 90 88 10

Output:
8043
"""
n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(n-1,-1,-1):
    s=s*10+l[i]%10
print(s)
