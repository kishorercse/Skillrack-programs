"""
The program must accept N integers as the input. The program must print the integers ending with the most repeated unit digit among the N integers as the output. If more than one 
unit digit have occurred the maximum number of times then print the integers which are having the largest unit digit among those unit digits. 

Boundary Condition(s): 
2 <= N <= 100 
1 <= Each integer value <= 10^5 

Input Format: 
The first line contains N. 
The second line contains N integers separated by a space. 

Output Format: 
The first line contains the integer value(s) separated by a space. 

Example Input/Output 1: 
Input:
7
32 57 41 69 10 48 77 

Output: 
57 77 

Explanation: 
Here, the unit digit 7 is repeated maximum number of times 2. 
So the integers ending with 7 are printed as the output. 

Example Input/Output 2:
Input:
8
92 75 12 86 55 50 82 25 

Output: 
75 55 25 

Explanation: 
Here, the unit digits 2 and 5 are repeated for the same maximum number of times 3. 
So the largest unit digit is 5, hence the integers ending with 5 are printed as the output.
"""
n=int(input())
l=list(map(int,input().split()))
d={}
mx=-1
for i in l:
    t=i%10
    try:
        d[t][0]+=1
        d[t][1].append(i)
    except KeyError:
        d[t]=[1,[i]]
    if d[t][0]>mx:
        mx=d[t][0]
        unit=t
    elif d[t][0]==mx:
        unit=max(unit,t)
print(*d[unit][1])
