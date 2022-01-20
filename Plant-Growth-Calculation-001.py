"""
In a matrix containing R rows and C columns, various plants are planted. The growth of a given plant in a calendar month depends on it's current height at the beginning of the
month. If the current height is a prime number, the height by which the plant grows in that month is equal to the current height minus previous prime number (If there is no
previous prime number consider the previous prime number as zero). If the current height is not a prime number then the height by which the plant grows in that month is equal
to the sum of the unit digits of the adjacent plants height at the beginning of the month (If there is no adjacent plant to left or right consider the value as zero). Given the
current height of the plants at the beginning of first month, print the height of the plants after N months.

Input Format:
The first line contains R and C separated by a space.
Next R lines contains C values representing the height of the plants (with the values separated by a space).
Last line contains N.

Output Format:
R lines containing C values denoting the height of the plants after N months  (with the values separated by a space).

Boundary Conditions:
1 <= R, C <= 999
1 <= N <= 100
1 <= Initial height of the plants <= 100

Example Input/Output 1:
Input:
3 3
1 2 4
6 1 11
5 7 12
2

Output:
4 13 10
9 20 23
9 25 21

Explanation:
After the 1st month, the height of the plants will be
3 4 6
7 8 15
7 9 19

After 2nd month, the height of the plants will be
4 13 10
9 20 23
9 25 21
"""
r,c=map(int,input().split())
m=[list(map(int,input().split())) for _ in range(r)]
n=int(input())
prime=[True if i%2!=0 else False for i in range(1000)]
prime[1]=False
prime[2]=True
p=3
while p*p<=1000:
    if prime[p]:
        for i in range(p**2,1000,p):
            prime[i]=False
    p+=2
primeList=[0,2]+[i for i in range(3,1000,2) if prime[i]]
for _ in range(n):
    for i in range(r):
        prev=m[i][0]
        for j in range(c):
            curr=m[i][j]
            if prime[m[i][j]]:
                m[i][j]+=m[i][j]-primeList[primeList.index(m[i][j])-1]
            else:
                if j>=1:
                    m[i][j]+=prev%10
                if j<c-1:
                    m[i][j]+=m[i][j+1]%10
            prev=curr
for i in m:
    print(*i)
