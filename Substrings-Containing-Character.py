"""
The program must accept a string S and a character C as the input. The program must print the count of substrings having a character C as the output.

Boundary Condition(s):
1 <= Length of S <= 10^5

Input Format:
The first line contains S.
The second line contains C.

Output Format:
The first line contains the count of substrings having the character C.

Example Input/Output 1:
Input:
skillrack
k

Output:
23

Explanation:
In the string skillrack, the substrings that have the character k are given below.
sk ski skil skill skillr skillra skillrac skillrack
k ki kil kill killr killra killrac killrack
illrack llrack lrack rack ack ck k
Hence the output is 23

Example Input/Output 2:
Input:
@5Computer5
5

Output:
29

Example Input/Output 3:
Input:
SKY
y

Output:
0
"""
s=input().strip()
c=input().strip()
l=len(s)
count=0
prev=-1
for i in range(l):
    if s[i]==c:
        count+=(l-i)*(i+1-(prev+1))
        prev=i
print(count)
