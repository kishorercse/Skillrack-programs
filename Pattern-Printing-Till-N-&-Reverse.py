"""
The program must accept an integer N and print 2N lines as shown in the Example Input/Output.

Input Format:
The first line contains N.

Output Format:
2N lines as shown in the Example Input/Output.

Boundary Conditions:
2 <=  N <= 100

Example Input/Output 1:
4

Output:
1
22
333
4444
4444
333
22
1

Example Input/Output 2:
7

Output:
1
22
333
4444
55555
666666
7777777
7777777
666666
55555
4444
333
22
1
"""
n=int(input())
l=[]
for i in range(1,n+1):
    s=''
    for j in range(1,i+1):
        s+=str(i)
        print(i,end='')
    print()
    l.insert(0,s)
print(*l,sep='\n')
