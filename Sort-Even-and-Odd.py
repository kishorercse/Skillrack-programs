"""
The program must accept N integers as the input. The program must print all the even integers among the N integers in ascending order. Then the program must print all the odd 
integers among the N integers in ascending order.

Boundary Condition(s): 
2 <= N <= 100
1 <= Each integer value <= 10^5 

Input Format: 
The first line contains N. 
The second line contains N integers separated by a space. 

Output Format:
The first line contains N integers separated by a space. 

Example Input/Output 1: 
Input:
8
3 8 9 12 7 5 10 13 

Output: 
8 10 12 3 5 7 9 13 

Explanation: 
In the given 8 integers, the even integers are 8 12 10. After sorting those even integers, they are printed as the output. 
In the given 8 integers, the odd integers are 3 9 7 5 13. After sorting those odd integers, they are printed as the output. 

Example Input/Output 2: 
Input:
5
41 32 23 68 10

Output: 
10 32 68 23 41
"""
n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in l:
    if i%2==0:
        a.append(i)
    else:
        b.append(i)
print(*sorted(a),*sorted(b))
