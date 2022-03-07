"""
The program must accept the source city and the destination city of N buses as the input. The name of a city C is also passed as the input. The program must print the output 
based on the following conditions.
- The program must print the name of the city C and all the cities where the people can go directly from the city C. If there are no buses to go from the city C, then the
program must print -1 as the output.
- Similarly, the program must print the name of the city C and all the cities from which the people can come directly to the city C. If there are no direct buses to come to the
city C, then the program must print -1 as the output.
Note: The names of the cities must be printed in the order of their occurrence.

Boundary Condition(s):
1 <= N <= 100
1 <= Length of each city's name <= 30

Input Format:
The first line contains N.
The next N lines, each contains the source city and the destination city of a bus separated by a space.

Output Format:
The first 2 lines contain the string values based on the given conditions.

Example Input/Output 1:
Input:
8
Chennai Bangalore
Trichy Hosur
Chennai Coimbatore
Bangalore Chennai
Chennai Trichy
Chennai Hyderabad
Bangalore Hyderabad
Trichy Chennai
Chennai

Output:
Chennai -> Bangalore Coimbatore Trichy Hyderabad
Chennai <- Bangalore Trichy

Explanation:
Here C = Chennai.
The cities where people can go directly from Chennai are Bangalore, Coimbatore, Trichy and Hyderabad.
The cities from which the people can come directly to Chennai are Bangalore and Trichy. 

Example Input/Output 2:
Input:
8
Chennai Bangalore
Trichy Hosur
Chennai Coimbatore
Bangalore Chennai
Chennai Trichy
Chennai Hyderabad
Bangalore Hyderabad
Trichy Chennai
Hyderabad

Output:
Hyderabad -> -1
Hyderabad <- Chennai Bangalore 

Example Input/Output 3:
Input:
6
Chennai Bangalore
Chennai Bangalore
Chennai Bangalore
Bangalore Chennai
Bangalore Chennai
Bangalore Chennai
Bangalore

Output:
Bangalore -> Chennai
Bangalore <- Chennai
"""
n=int(input())
s2d={}
d2s={}
for _ in range(n):
    a,b=input().split()
    if b not in s2d.get(a,[]):
        s2d[a]=s2d.get(a,[])+[b]
    if a not in d2s.get(b,[]):
        d2s[b]=d2s.get(b,[])+[a]
c=input().strip()
print(c,"->",*s2d.get(c,[-1]))
print(c,"<-",*d2s.get(c,[-1]))
