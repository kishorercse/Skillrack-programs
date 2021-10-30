"""
The program must accept N string values and an integer X as the input. The program must print the count of string values having at least X non repeated characters as the output. 

Boundary Condition(s):
1 <= N <= 1000 
1 <= X <= 65 
1 <= Length of each string <= 100 

Input Format: 
The first line contains N and X separated by a space. 
The next N lines, each contains a string. 

Output Format: 
The first line contains the count of string values having at least X non repeated characters. 

Example Input/Output 1: 
Input: 
4 6 
flamingo 
penguin 
cuckoo 
woodpecker 

Output: 
2 

Explanation: 
The string "flamingo" has 8 non repeated characters.
The string "penguin" has 5 non repeated characters. 
The string "cuckoo" has 2 non repeated characters. 
The string "woodpecker" has 6 non repeated characters.
So only 2 string values (flamingo and woodpecker) having at least 6 non repeated characters.
Hence the output is 2 

Example Input/Output 2: 
Input: 
6 7 
apples 
blueberries 
cherries 
12345678 
#@* 
watermelon 

Output:
2
"""
n,x=map(int,input().split())
count=0
while n>0:
    s=input().strip()
    c=0
    d={}
    for i in s:
        try:
            d[i]+=1
        except:
            d[i]=1
    for i in s:
        if d[i]==1:
            c+=1
    if c>=x:
        count+=1
    n-=1
print(count)
