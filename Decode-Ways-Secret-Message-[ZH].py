"""
A top secret message string S containing letters from A-Z (only upper case letters) is encoded to numbers using the following mapping:
'A' -> 1, 'B' -> 2 and so on till Z -> '26'

The program has to print the total number of ways in which the received message can be decoded.

Input Format:
The first line contains the string S containing numbers.

Output Format:
The first line contains the number of ways in which S can be decoded.

Boundary Conditions:
1 <= Length of S <= 100

Example Input/Output 1:
Input:
123

Output:
3

Explanation:
1-A 2-B 3-C 12-L 23-W.
Hence 123 can be decoded as ABC or AW or LC, that is in 3 ways.

Example Input/Output 2:
Input:
1290

Output:
0

122410
"""
s=input().strip()
l=len(s)
ans=[0]*(l+1)
ans[0]=ans[1]=1
for i in range(2,l+1):
    if s[i-1]!='0':
        ans[i]=ans[i-1]
    if s[i-2]=='1' or (s[i-2]=='2' and s[i-1]<='6'):
        ans[i]+=ans[i-2]
print(ans[-1])
