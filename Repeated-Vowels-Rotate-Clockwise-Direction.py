"""
The program must accept a string S containing only lower case alphabets as the input. The program must rotate the repeated vowels in the string S by 1 position in the clockwise
direction. Then the program must print the modified string S as the output.

Boundary Condition(s):
4 <= Length of S <= 1000

Input Format:
The first line contains S.

Output Format:
The first line contains the modified string S.

Example Input/Output 1:
Input:
administration

Output:
idminastritaon

Explanation:
The repeated vowels in the given string are highlighted below.
administration
After rotating those repeated vowels by 1 position in the clockwise direction, the string becomes "idminastritaon".
Hence output is idminastritaon

Example Input/Output 2:
Input:
correspondent

Output:
cerrospendont

Example Input/Output 3:
Input:
deal

Output:
deal
"""
s=list(input().strip())
l=len(s)
arr=[]
d={'a':-1,'e':-1,'i':-1,'o':-1,'u':-1}
count={'a':0,'e':0,'i':0,'o':0,'u':0}
vowels=0
for i in range(l):
    if s[i] in "aeiou":
        if d[s[i]]==-1:
            d[s[i]]=i
        else:
            arr.append(i)
            vowels+=1
        count[s[i]]+=1
for i in d:
    if count[i]>1:
        arr.append(d[i])
        vowels+=1
if arr:
    arr.sort()
    ch=s[arr[0]]
    for i in range(vowels-1):
        s[arr[i]]=s[arr[i+1]]
    s[arr[vowels-1]]=ch
print(*s,sep='')
