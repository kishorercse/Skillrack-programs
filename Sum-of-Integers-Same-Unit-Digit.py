"""
The program must accept N integers as the input. The program must print the sum of the integers having the same unit digit (0 to 9) in the given N integers. 

Boundary Condition(s): 
1 <= N <= 1000 
1 <= Each integer value <= 10^5 

Input Format: 
The first line contains N.
The second line contains N integers separated by a space.

Output Format: 
The first line contains the integer value(s) representing the sum of the integers having the same unit digit.

Example Input/Output 1: 
Input:
5
46 20 36 74 60

Output: 
80 74 82

Explanation:
The integers having 0 as the unit digit are 20 and 60. So their sum 80 is printed. 
The integer having 4 as the unit digit is 74. So 74 is printed. 
The integers having 6 as the unit digit are 46 and 36. So their sum 82 is printed.

Example Input/Output 2: 
Input:
10
99 51 52 91 12 46 31 37 26 72 

Output:
173 136 72 37 99
"""
n=int(input())
l=list(map(int,input().split()))
count=[0]*10
for i in l:
    count[i%10]+=i
for i in count:
    if i!=0:
        print(i,end=' ')
