"""
The program must accept N integers and an integer K as the input. For each digit D in K, the program must find the smallest integer that contains the digit D. If there is no 
integer with the digit D, then consider 0 for that digit. Finally, the program must print the sum of resulting integers as the output.

Boundary Condition(s):
1 <= N <= 100
1 <= Each integer value, K <= 10^7

Input Format:
The first line contains N.
The second line contains N integers separated by a space.
The third line contains K.

Output Format:
The first line contains an integer representing the sum of resulting integers based on the given conditions.

Example Input/Output 1:
Input:
7
909 880 283 205 790 495 922
248

Output:
983

Explanation:
Here K = 248.
1st digit is 2: The smallest integer having the digit 2 is 205.
2nd digit is 4: The smallest integer having the digit 4 is 495.
3rd digit is 8: The smallest integer having the digit 8 is 283.
205 + 495 + 283 = 983.
Hence 983 is printed as the output.

Example Input/Output 2:
Input:
5
96 23 43 113 6
31517

Output:
249

Explanation:
Here K = 31517.
1st digit is 3: The smallest integer having the digit 3 is 23.
2nd digit is 1: The smallest integer having the digit 1 is 113.
3rd digit is 5: There is no integer with the digit 5.
4th digit is 1: The smallest integer having the digit 1 is 113.
5th digit is 7: There is no integer with the digit 7.
23 + 113 + 0 + 113 + 0 = 249.
Hence 249 is printed as the output.
"""
n=int(input())
l=input().split()
k=input().strip()
d={}
for i in l:
    for j in i:
        d[int(j)]=min(int(i),d.get(int(j),99999999))
s=0
for i in k:
    s+=d.get(int(i),0)
print(s)
