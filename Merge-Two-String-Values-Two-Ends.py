"""
The program must accept two string values S1 and S2 containing only lower case alphabets as the input. The program must form a string S3 of length L based on the following
conditions.
- The length of S3, L = Length of S1 + Length of S2.
- The program must compare the alphabets at the same positions in S1 and S2 from left to right. The alphabet with least ASCII value must be added to S3 starting from the left
and the other alphabet must be added to S3 starting from the right.
- If the length of S1 is not equal to the length of S2, then the remaining alphabets in the longest string must be filled in the remaining positions in S3 from left to right.
Finally, the program must print the string S3 as the output.

Boundary Condition(s):
1 <= Length of S1, S2 <= 100

Input Format:
The first line contains S1.
The second line contains S2.

Output Format:
The first line contains S3.

Example Input/Output 1:
Input:
code
online

Output:
cndeneiloo

Explanation:
Here S1 = code and S2 = online.
At the 1st position: The ASCII value of 'c' is less than 'o'. S3 = cndeneiloo.
At the 2nd position: The ASCII value of 'n' is less than 'o'. S3 = cndeneiloo.
At the 3rd position: The ASCII value of 'd' is less than 'l'. S3 = cndeneiloo.
At the 4th position: The ASCII value of 'e' is less than 'i'. S3 = cndeneiloo.
The remaining alphabets ('n' and 'e') are filled in the remaining positions in S3 (cndeneiloo).
Hence the output is
cndeneiloo

Example Input/Output 2:
Input:
abcxyz
pqrdef

Output:
abcdefzyxrqp
"""
s1=input().strip()
s2=input().strip()
s3f=s3r=''
a=len(s1)
b=len(s2)
m=min(a,b)
for i in range(m):
    if s1[i]<s2[i]:
        s3f+=s1[i]
        s3r=s2[i]+s3r
    else:
        s3f+=s2[i]
        s3r=s1[i]+s3r
s3f+=s1[m:]+s2[m:]
print(s3f+s3r)
