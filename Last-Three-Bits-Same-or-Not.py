"""
The program must accept N integers as the input. For each integer X among the N integers, the program must find the last 3 bits in the binary representation of X and print the
integer X if the last three bits are same. If there is no such integer, the program must print -1 as the output. 

Boundary Condition(s): 
1 <= N <= 100
4 <= Each integer value <= 10^8 

Input Format: 
The first line contains N. 
The second line contains N integers separated by a space. 

Output Format: 
The first line contains the integers as per the given condition separated by a space or -1.

Example Input/Output 1:
Input: 
5
4 7 6 8 10 

Output:
7 8 

Explanation:
The binary representation of 4 is 100. Here the last 3 bits are not same. So 4 is NOT printed. 
The binary representation of 7 is 111. Here the last 3 bits are same. So 7 is printed. 
The binary representation of 6 is 110. Here the last 3 bits are not same. So 6 is NOT printed. 
The binary representation of 8 is 1000. Here the last 3 bits are same. So 8 is printed. 
The binary representation of 10 is 1010. Here the last 3 bits are not same. So 10 is NOT printed.

Example Input/Output 2:
Input:
4
62 57 19 81

Output:
-1
"""
n=int(input())
l=list(map(int,input().split()))
f=False
for i in range(n):
    x=l[i]
    t=l[i]&1
    l[i]=l[i]>>1
    for ctr in range(2):
        if t!=l[i]&1:
            break
        l[i]=l[i]>>1
    else:
        f=True
        print(x,end=' ')
if not f:
    print(-1)
