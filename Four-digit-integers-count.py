"""
The program must accept a string S containing only nonzero digits as the input. The program must find the count of 
unique four-digit integers that can be formed using the digits in S based on the following conditions.
- Exactly four digits must be picked from the string in the same order of their occurence.
- First 2 digits of the integer must be the same, say x.
- Last 2 digits of the integer must be the same, say y.
- The value of the digit y must be x+1

Boundary Conditions(s):
1 <= Length of S <=100

Input Format:
The first line contains S.

Output Format:
The first line contains the count of unique four-digit integers that can be formed using the digits in S.

Example Input/Output 1:
Input:
212112377388

Output:
2

Explanation:
The 2 possible four-digit integers are 2233 and 7788.

Example Input/Output 2:
Input:
112233225456465643298789

Output:
4

Explanation:
The 4 possible four-digit integers are 1122, 2233, 3344 and 5566.
"""
s=input().strip()
a=[[0,0] for _ in range(8)]
count=0
for i in s:  
    if a[0]!=1 and i=='1':  
        a[0][0]+=1   
    elif a[7]!=1 and i=='9':    
        if a[7][0]>=2: 
            a[7][1]+=1  
            if a[7][1]==2:
                count+=1
                if count==8:
                    break
    else: 
        t=int(i)   
        if a[t-1]!=1:
            a[t-1][0]+=1    
        if a[t-2]!=1 and a[t-2][0]>=2:    
            a[t-2][1]+=1       
            if a[t-2][1]==2:         
                count+=1
                if count==8:
                    break
print(count)
