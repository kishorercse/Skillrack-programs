"""
N integers are passed as input to the program. The program must print the GCD (HCF) of these N integers.

Input Format:
The first line contains N.
The second line contains N integers each separated by a space.

Output Format:
The first line contains the HCF of these N numbers.

Boundary Conditions:
2 <= N <= 100

Example Input/Output 1:
Input:
4
15 20 30 50

Output:
5
"""
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
n=int(input())
l=list(map(int,input().split()))
res=l[0]
for i in range(1,n):
    res=gcd(l[i],res)
print(res)
