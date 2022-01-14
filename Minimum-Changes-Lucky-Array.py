"""
The program must accept an array of N integers as the input. The value of N is always even. An array is called lucky if and only if each integer in the first half of the array 
can be paired with the corresponding integer in the second half of the array based on one of the following three conditions.
- In each pair, the integer from the first half is strictly greater than the integer from the second half.
- In each pair, the integer from the first half is strictly less than the integer from the second half.
- In each pair, the integer from the first half is strictly equal to the integer from the second half.
The program must print the minimum number of changes required to make the given array lucky.

Boundary Condition(s):
2 <= N <= 1000
1 <= Each integer value <= 10^5

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains an integer value representing the minimum number of changes required to make the given array lucky.

Example Input/Output 1:
Input:
6
10 10 11 11 11 11

Output:
1

Explanation:
To make the array lucky using the 1st condition, the number of changes required is 3.
To make the array lucky using the 2nd condition, the number of changes required is 1.
To make the array lucky using the 3rd condition, the number of changes required is 2.
The minimum number of changes required is 1 (using the 2nd condition).
Hence 1 is printed as the output.

Example Input/Output 2:
Input:
8
15 10 15 14 14 15 14 14

Output:
2

Example Input/Output 3:
Input:
6
10 15 10 10 14 10

Output:
1
"""
n=int(input())
l=list(map(int,input().split()))
i,j=0,n//2
great=equal=less=0
while j<n:
    if l[i]>=l[j]:
        less+=1
    if l[i]<=l[j]:
        great+=1
    if l[i]!=l[j]:
        equal+=1
    i+=1
    j+=1
print(min(great,less,equal))
