"""
The program must accept N integers as the input. For each X among the N integers, the program must find the bit score based on the following conditions.
- For each digit D in the integer X, the program must find the product of D and the binary representation of D (i.e., consider the binary representation D as a decimal value
when multiplying with D). 
- The sum of the digit-binary products obtained is the bit score of the integer X. Then the program must sort the integers based on the bit score in ascending order. If two 
or more integers have the same bit score, then the program must sort those integers in ascending order. Finally, the program must print the N sorted integers as the output. 

Boundary Condition(s):
1 <= N <= 100
1 <= Each integer value <= 10^8

Input Format:
The first line contains N.
The second line contains N integers separated by a space. 

Output Format:
The first line contains N integers separated by a space representing the N sorted integers. 

Example Input/Output 1: 
Input: 
4
313 22 15 133 

Output: 
22 133 313 15 

Explanation:
313 -> (3*11 + 1*1 + 3*11) -> 33 + 1 + 33 = 67.
22 -> (2*10 + 2*10) -> 20 + 20 = 40.
15 -> (1*1 + 5*101) -> 1 + 505 = 506. 
133 -> (1*1 + 3*11+ 3*11)->1 +33+33  = 67.
After sorting the integer values based on the given conditions, the integers become 
22 133 313 15 

Example Input/Output 2:
Input:
5 
28 3322 2332 7 3232 

Output:
2332 3232 3322 7 28 
"""
def bit(n):
    n=str(n)
    s=0
    for i in n:
        t=int(i)
        s+=t*int(bin(t)[2:])
    return s
n=int(input())
l=[[bit(i),i] for i in list(map(int,input().split()))]
for i,j in sorted(l):
    print(j,end=' ')
