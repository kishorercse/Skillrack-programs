"""
N string values are passed as input to the program. Each string will contain only the alphabets a-z in lower case. A given alphabet may be repeated any number of times. The 
program must print the count C of the alphabets that are present in all the N string values.

Input Format:
The first line contains N.
Next N lines contain the N string values.

Output Format:
The first line contains C.

Boundary Conditions:
2 <= N <= 500
1 <= Length of the string value <= 1000

Example Input/Output 1:
Input:
3
mnppqqr
ajkmnnm
poormanagement

Output:
2

Explanation:
Only 2 alphabets m and n are present in all the three string values.
"""
n=int(input())
d={}
for i in range(1,n+1):
    s=input().strip()
    for ch in s:
        if d.get(ch,0)==i-1:
            d[ch]=i
count=0
for i in d:
    if d[i]==n:
        count+=1
print(count)
