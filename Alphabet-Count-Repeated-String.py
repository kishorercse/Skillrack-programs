"""
A string S is passed as input to the program. The string S is repeated till the repeated string R is of length N. The program must print the count of a specific 
alphabet A which is passed as the input in the repeated string R.

Input Format:
The first line contains S.
The second line contains N.
The third line contains A.

Output Format:
The first line contains the count of the alphabet A in the repeated string R.

Boundary Conditions:
1 <= Length of S <= 50
1 <= N <= 9999999
A is from a to z

Example Input/Output 1:
Input:
abcd
10
b

Output:
3

Explanation:
abcd when repeated till length 10 is abcdabcdab in which the alphabet b occurs 3 times.
"""
s=input().strip()
n=int(input())
a=input().strip()
l=len(s)
c=s.count(a)
print(c*(n//l)+s.count(a,0,n%l))
