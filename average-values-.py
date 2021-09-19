"""
The program must accept N integers and an integer K as the input. The program must print the average of all the integers 
which are greater than or equal to K with the precision up to two decimal places as the output.

Boundary Condition(s): 
1 <= N <= 10^5 
-10^3 <= K, Each Integer Value <= 10^3 

Input Format: 
The first line contains two integers N and K separated by a space. 
The second line contains N integers separated by space(s). 

Output Format:
The first line contains the average of all the integers which are greater than or equal to K 
with the precision up to two decimal places. 

Example Input/Output 1: 
Input: 
5 25 
10 43 21 25 29 

Output: 
32.33 

Explanation: 
The integers which are greater than or equal to 25 are 43, 25 and 29. 
So the average 43, 25 and 29 is 32.33.
Hence the output is 32.33

Example Input/Output 2: 
Input: 
4 -10 
-12 10 -45 -5 

Output: 2.50
"""
n,k=map(int,input().split())
l=list(map(int,input().split()))
s = count = 0
for i in l:
    if i>=k:
        s+=i
        count+=1
print("%.2f"%(s/count))
