"""
The program must accept N distinct digits as the input. The program must print all possible prime numbers (1, 2 or 3 digits) that can be formed with these N digits. The prime 
numbers must be sorted.

Boundary Condition(s):
2 <= N <= 10

Input Format:
The first line contains N.
The second line contains N digits separated by a space.

Output Format:
The first line contains all possible prime numbers that can be formed with the given N digits.

Example Input/Output 1:
Input:
4
3 0 1 7

Output:
3 7 13 17 31 37 71 73 103 107 137 173 307 317 701

Explanation:
Here N=4 and the given 4 digits are 3, 0, 1 and 7.
All the possible prime numbers(containing unique digits) that can be formed with the digits 3, 0, 1 and 7 are given below
3 7 13 17 31 37 71 73 103 107 137 173 307 317 701

Example Input/Output 2:
Input:
5
1 0 2 5 8

Output:
2 5 251 281 521 821
"""
def isPrime(num):
    if num<=1:
        return False
    if num<=3:
        return True
    if num%2==0 or num%3==0:
        return False
    i=5
    while i*i<=num:
        if num%i==0 or num%(i+2)==0:
            return False
        i+=6
    return True
def create(num, arr, dig):
    if isPrime(int(num)):
        ans.append(int(num))
    if dig==3:
        return
    for i in range(n-dig):
        create(num+arr[i],arr[:i]+arr[i+1:],dig+1)
n=int(input())
l=input().split()
ans=[]
for i in range(n):
    if l[i]!='0':
        create(l[i],l[:i]+l[i+1:],1)
print(*sorted(ans))
