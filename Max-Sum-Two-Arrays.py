"""
The program must accept two arrays of size N and then for each element position, the program must print find the sum of odd elements till that position for both the arrays and
then print the sum which is higher.

Boundary Condition(s):
1 <= N <= 100
1 <= Each integer value <= 10^5

Input Format:
The first line contains N.
The second line contains N integers representing the first array separated by a space.
The third line contains N integers representing the second array separated by a space.

Output Format:
The first line contains N integer values based on the given conditions.

Example Input/Output 1:
Input:
6
8 1 7 8 2 1
1 3 2 5 6 2

Output:
1 4 8 9 9 9

Explanation:
Here N = 6.
Till position 1:
Sum of odd integers in the 1st array is 0.
Sum of odd integers in the 2nd array is 1.
Here 1 is the maximum which is printed as the output.

Till position 2:
Sum of odd integers in the 1st array is 1.
Sum of odd integers in the 2nd array is 4.
Here 4 is the maximum which is printed as the output.

Till position 3:
Sum of odd integers in the 1st array is 8.
Sum of odd integers in the 2nd array is 4.
Here 8 is the maximum which is printed as the output.

Till position 4:
Sum of odd integers in the 1st array is 8.
Sum of odd integers in the 2nd array is 9.
Here 9 is the maximum which is printed as the output.

Till position 5:
Sum of odd integers in the 1st array is 8.
Sum of odd integers in the 2nd array is 9.
Here 9 is the maximum which is printed as the output.

Till position 6:
Sum of odd integers in the 1st array is 9.
Sum of odd integers in the 2nd array is 9.
Here 9 is the maximum which is printed as the output.

Example Input/Output 2:
10
9 16 3 26 14 19 181 6 29 12
17 11 13 24 30 10 2 156 22 20

Output:
17 28 41 41 41 41 212 212 241 241
"""
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
aSum=[0]*n
bSum=[0]*n
if a[0]%2!=0:
    aSum[0]=a[0]
if b[0]%2!=0:
    bSum[0]=b[0]
print(max(aSum[0],bSum[0]),end=' ')
for i in range(1,n):
    if a[i]%2!=0:
        aSum[i]=a[i]
    if b[i]%2!=0:
        bSum[i]=b[i]
    aSum[i]+=aSum[i-1]
    bSum[i]+=bSum[i-1]
    print(max(aSum[i],bSum[i]),end=' ')
