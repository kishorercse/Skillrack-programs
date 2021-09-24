"""
The program must accept N string values having an integer and an alphabet. Then the program must order the string
values based on the alphabets in ascending order (ignoring the case). The program must print Yes if the corresponding
integer values are strictly increasing. Else the program must print No as the output.

Note: The alphabets in the given N string values are always unique.

Boundary condition(s):
1 <= N <=26

Input Format:
The first line contains N. 
The next N lines contain the string values. 

Output Format: 
The first line contains Yes or No. 

Example Input/Output 1: 
Input: 
4 
5B 
2a 
15x 
11w 

Output: 
Yes 

Explanation: 
Ordering the string values based on the alphabets(ignoring the case), the order is 2a 5B 11w 15x. 
Here the integer values are strictly increasing. Hence Yes is printed. 

Example Input/Output 2: 
Input: 
4 
5B 
2a 
15x 
201w

Output: 
No 

Explanation: 
Ordering the string values based on the alphabets(ignoring the case), the order is 2a 5B 201w 15x. 
Here 15 is less than 201. Hence No is printed. 

Example Input/Output 3: 
Input: 
4 
5B 
2a 
15x 
15w 

Output: 
No
"""
n=int(input())
l=[]
for i in range(n):
    t=input().strip()
    l.append([int(t[:-1]),t[-1].lower()])
l.sort(key=lambda x:x[-1])
for i in range(1,n):
    if l[i-1][0]>=l[i][0]:
        print("No")
        break
else:
    print("Yes")
