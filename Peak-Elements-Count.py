"""
N integers are passed as input. The program must print the count of peak elements among the N integers. An element is a peak element if it is greater than it's neighbours 
(the elements to the left and right). The elements present in the extreme left and right can never be peak elements.

Input Format:
The first line contains N. The second line contains N integer values separated by a space.

Output Format:
The first line contains the count of peak elements.

Boundary Conditions:
2 <= N <= 1000

Example Input/Output 1:
Input:
5
1 2 3 1 3
Output:
1

Example Input/Output 2:
Input:
5
1 2 3 4 5
Output:
0
"""
n=int(input())
l=list(map(int,input().split()))
count=0
for i in range(1,n-1):
    if l[i]>l[i-1] and l[i]>l[i+1]:
        count+=1
print(count)
