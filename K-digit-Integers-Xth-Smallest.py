"""
The program must accept a list of N unique integers and two integers K, X as the input. The program must print the Xth smallest integer among the K-digit integers in the given 
list. If there is no such integer, then the program must print -1 as the output.

Boundary Condition(s):
1 <= N <= 100
-10^9 <= Each integer value <= 10^9
1 <= K <= 9
1 <= X <= N

Input Format:
The first line contains N.
The second line contains N integers separated by a space.
The third line contains K and X separated by a space.

Output Format:
The first line contains an integer representing the Xth smallest integer among the K-digit integers in the given list or -1.

Example Input/Output 1:
Input:
8
450 87 65 720 616 8 10 536
3 2

Output:
536

Explanation:
Here K = 3 and X = 2.
The three-digit integers are 450, 720, 616 and 536.
The 2nd smallest three-digit integer is 536.
Hence 536 is printed as the output.

Example Input/Output 2:
Input:
6
-95 -5254 -13 -20 -654 -40
2 3

Output:
-20

Example Input/Output 3:
Input:
5
456 78 13 -564 125
3 4

Output:
-1
"""
def length(s):
    if s[0]=='-':
        s=s[1:]
    return len(s)==k
n=int(input())
l=input().split()
k,x=map(int,input().split())
l=sorted(map(int,filter(length,l)))
try:
    print(l[x-1])
except IndexError:
    print(-1)
