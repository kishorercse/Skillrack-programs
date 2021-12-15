"""
An array of N integers is passed as input. The program must print the length of the longest set of integers among the N numbers so that the absolute difference between any two 
integers in the set does not exceed 1.

Input Format:
The first line will contain the value of N which represents the count of integers to be passed as input.
The second line will contain N integer value separated by a space.

Output Format:
The first line will contain the integer value denoting the longest set of integers meeting the given criteria.

Constraints:
3 <= N <= 10000

Example Input/Output 1:
Input:
9
1 3 2 1 4 2 1 5 3

Output:
5

Explanation:
The longest set meeting the condition is {1,2,1,2,1}

Example Input/Output 2:
Input:
6
1 2 3 4 5 3

Output:
3

Explanation:
The longest set meeting the condition is {3,4,3}
"""
n=int(input())
l=list(map(int,input().split()))
d={}
for i in l:
    d[i]=d.get(i,0)+1
s=sorted(d)
size=len(s)
mx=d[s[0]]
for i in range(1,size):
    mx=max(mx,d[s[i-1]]+d[s[i]])
print(mx)
