"""
The program must accept a list of integers as the input. 
The program must find the number of integers N in the given list. 
The program must print the sum of every X integers in the list, where X is the second largest factor of N. 
Boundary Condition(s): 
2 <= Number of integers in the list <= 1000 
Input Format: 
The line(s), each contains an integer. 
Output Format: 
The first line contains N/X integers separated by a space. 
Example Input/Output 1: 
Input: 
10 
20 
15 
50 
22 
11 
Output: 
45 83 
Explanation: 
There are 6 integers in the given list. So the value of N = 6. The second largest factor X of 6 is 3. 
The sum of the first three integers in the list is 45 (10+20+15). 
The sum of the next three integers in the list is 83 (50+22+11). 
Hence the output is 45 83
Example Input/Output 2: 
Input:
8 
7 
1 
5 
7 
Output: 
8 7 1 5 7 
"""
n=0
l=[]
while True:
    try:
        l.append(int(input()))
        n+=1
    except:
        break
for i in range(2,n//2+1):
    if n%i==0:
        t=n//i
        break
else:
    t=1
while l:
    print(sum(l[:t]),end=' ')
    l=l[t:]
