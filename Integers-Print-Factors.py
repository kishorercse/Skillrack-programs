"""
An integer array of N integers is passed as the input. Another integer value K is also passed as the input. The program must consider every K integers and form a new integer X
with the unit digits of the K integers considered and print the factors for X. 

Note: If the unit digits of all K integers under consideration is zero, then print 0.

Hint: Optimize your logic to avoid Time Limit Exceeded Error. 

Boundary Condition(s): 
1 <= N <= 100 
1 <= Each integer value <= 10^5
1 <= K <= 8 

Input Format: 
The first line contains N and K separated by a space. 
The second line contains N integers separated by a space.

Output Format: 
The first N/K lines contain the factors separated by a space. 

Example Input/Output 1:
Input: 
7 3
10 20 30 41 50 60 90 

Output: 
0
1 2 4 5 10 20 25 50 100 

Explanation:
Here K=3. 
The first three integers are 10 20 30. The integer formed with the unit digits is 000 which is equal to 0. Hence 0 is printed. 
The next three integers are 41 50 60. The integer formed with the unit digits is 100. The factors of 100 are 1 2 4 5 10 20 25 50 100. 
The seventh value 90 is not considered as we need a set of K=3 integers. 

Example Input/Output 2:
Input: 
12 4
20 81 20 86 61 20 22 54 10 120 21 73

Output:
1 2 53 106 
1 2 4 8 16 32 64 128 256 512 1024
1 13 
"""
n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in range(0,n,k):
    t=0
    for j in range(i,min(n,i+k)):
        t=t*10+l[j]%10
    if n-i>=k:
        if t==0:
            print(0)
        else:
            i=1
            a=[]
            while i*i<=t:
                if t%i==0:
                    print(i,end=' ')
                    if t//i!=i:
                        a.insert(0,t//i)
                i+=1
            print(*a)
