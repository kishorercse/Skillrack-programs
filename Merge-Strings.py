"""
Two strings S1 and S2 can be concatenated to form string S3. If certain characters of the first part of S2 matches with those characters in the last part of S1, they can be 
merged to occur only once.
Given S1 and S2 as the input, the program must print the minimum possible length of S3.

Input Format:
The first line contains S1.
The second line contains S2.

Output Format:
The first line contains the integer value representing the minimum possible length of S3.

Boundary Conditions:
1 <= Length of S1 and S2 <= 1000

Example Input/Output 1:
Input:
abcdef
efghij

Output:
10

Explanation:
The common part is ef and hence S3 becomes abcdefghij whose length is 10.
"""
a=input().strip()
b=input().strip()
l1=len(a)
l2=len(b)
for i in range(l1):
    if a[i:]==b[:l1-i]:
        print(l1+l2-(l1-i))
        break
else:
    print(l1+l2)
