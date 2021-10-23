"""
The program must accept N integers representing an incomplete row of Pascal's triangle as the input. Pascal's triangle is a triangular array constructed by summing adjacent 
integers in preceding rows. The program must complete the row by finding the missing integers in the row. Then the program must print the complete row of Pascal's triangle 
as the output. 

Boundary Condition(s):
2 <= N <= 30

Input Format: 
The first line contains N. 
The second line contains N integers separated by a space.

Output Format:
The first line contains the integer values representing the complete row of Pascal's triangle. 

Example Input/Output 1:
Input: 
4 
1 6 15 20 

Output: 
1 6 15 20 15 6 1 

Explanation: 
The given 4 integers represent the 7th row of Pascal's triangle. 
The first 7 rows of Pascal's triangle are given below. 
1 
1 1 
1 2 1
1 3 3 1
1 4 6 4 1 
1 5 10 10 5 1 
1 6 15 20 15 6 1 
The missing integers in the 7th row are 15, 6 and 1.
Hence the complete 7th row is printed as the output. 
1 6 15 20 15 6 1 

Example Input/Output 2:
Input:
2 
1 3

Output:
1 3 3 1 

Explanation:
The given 2 integers represent the 4th row of Pascal's triangle. Hence the complete 4th row is printed as the output.
1 3 3 1
"""
n=int(input())
l=list(map(int,input().split()))
row=l[1]
print(*l,end=' ')
prev=l[-1]
for i in range(n,row+1):
    curr=(prev * (row-i+1))//i
    prev=curr
    print(curr,end=' ')
