"""
The program must accept N three-digit integers as the input. The value of N is always even. The program must form N/2 integers by merging every two integers (X, Y) among the 
given N integers based on the following condition.
- The order of digits in the resulting integer from merging X and Y must be as follows.
Largest digit in hundreds place, Smallest digit in hundreds place, Largest digit in tens place, Smallest digit in tens place, Largest digit in ones place, Smallest digit in 
ones place.
Finally, the program must print the N/2 integers in sorted order.

Boundary Condition(s):
2 <= N <= 100

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains the N/2 integers in sorted order separated by a space.

Example Input/Output 1:
Input:
4
123 654 237 195

Output:
219375 615243

Explanation:
123 and 654 can be merged as 615243.
237 and 195 can be merged as 219375.
So the resulting two integers are printed in sorted order.

Example Input/Output 2:
Input:
6
856 202 100 504 250 712

Output:
510040 725120 825062
"""
n=int(input())
l=input().split()
res=[]
for i in range(0,n,2):
    num=''
    for j in range(3):
        num+=max(l[i][j],l[i+1][j])+min(l[i][j],l[i+1][j])
    res.append(int(num))
print(*sorted(res))
