"""
The program must accept three integers X, Y and Z, where the unit digits of two integers are always the same. The program must find those two integers and print them in ascending 
order as the output.

Boundary Condition(s): 
1 <= X, Y, Z <= 1000 

Input Format: 
The first line contains X, Y and Z separated by a space.

Output Format: 
The first line contains two integers having the same unit digit in ascending order. 

Example Input/Output 1: 
Input:
45 20 35 

Output: 
35 45 

Explanation: 
The unit digits of 45 and 35 are the same. So they are printed in ascending order. 

Example Input/Output 2: 
Input: 
66 482 12 

Output:
12 482
"""
a=sorted(list(map(int,input().split())))
if a[0]%10==a[1]%10:
    print(a[0],a[1])
elif a[0]%10==a[2]%10:
    print(a[0],a[2])
else:
    print(a[1],a[2])
